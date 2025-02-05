import cv2

from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator

model = YOLO("./best.pt") # our trained weights
names = model.names # its a list of classes that we want to detect
cap = cv2.VideoCapture(0) # it will use your native web cam , so plugit it in

fps = cap.get(int(cv2.CAP_PROP_FPS))
while True: # do it again and again
    ret, frame = cap.read() # returns if camera is faulty
    if not ret:
        break

    annotator = Annotator(frame) # using the ultralytics annotator for easy inference in this casse
    results = model.predict(frame)
    boxes = results[0].boxes.xyxy.cpu()
    klass_list = results[0].boxes.cls.cpu().tolist()

    for box, klass in zip(boxes, klass_list):
        annotator.box_label(box=box, label=names[int(klass)] + f" FPS: {fps:.2f}")

    cv2.imshow("Bondstein Pre-interview Task", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release() # release the buffer
cv2.destroyAllWindows() # release all the memory