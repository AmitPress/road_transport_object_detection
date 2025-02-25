## Project Overview

#### Applications
Here we have two working examples of AI applications. One is a web application and other is a desktop application. Both are very minimal and not
production ready and don't claim to be. But both of them are nice enough for a minimal viable concept product. These two prototypes illustrates the capability of the models that are created.

You can access the live inference app in the `apps/live_inference_app` folder. Please head to there and read the `readme.md` file for a clear picture. Again, you can find the web app `apps/huggingface_space_app` that is also deployed in the 🤗spaces. But you can run it locally as well.

#### Dataset
The dataset is totally handcrafted. I have feteched the data from the internet and make the full datasets for consumption in both the yolo and resnet model.
Please head to the datasets folder and have some more idea on that and please read the `reports/dataset.pdf` for more depthwise understanding.

#### Codes
There are 3 types of code snippets. One is for utility workings like preprocessing or insights derivations. Other two are for training and inference.
You can find the training, inference and preprocessing code at `source_codes` folder. Please read the readme.md file there to have a better picture.

#### Reports
The reports folder have the below products,
- Report on dataset
- Report on training and testing the models
- Report on background studies

#### Reference Papers
The `reference_papers` folder holds the literatures that are being reviewed in the background studies report. So, the folder is only for the resources.

Please let me know if anything went incomprehensible. I will try to clearify that as well.

# Source Codes Overview

### RESNET50 Model
The `rtds-pretrained.ipynb` file is reponsible for fine-tuning the resnet50 model for our application. In this file we have used the popular `fastai` module by Jeremy Howard. This module is basically a wrapper around the pytorch module. So, it abstracts away many setup procedures of pytorch itself.

#### Why FastAI than pytorch or other?
FastAI itself does not make the inference or training fast but the development is by far the fastest if we consider other frameworks while training a new model. We are basically interested in making a prototype rathar than a full-fledge solution. So, for this rapid prototyping and developement scheme of our operation, we better use the FastAI and again I am bound to deliver the project with the due time. Thats why it is best for the business.

#### Aftermath of Using the library
It made the development way faster. When development speed is fast, the debugging and feature implementation also tends to get influenced and be faster alongside. So, I felt that this way of training the model for just implementing a simple idea is the best.

#### What else is good about the trainign session?
The good thing is that I ran a GradCam session and found out the focusing area of the learner without any special preparation.
![alt gradcam](/reports/resources/resnet50/output.png)
So, here above 7you can see that the original image is of all four wheelers where the gradcam is focusing is also on the section of the four wheelers. Although it is not that accurate but isnt this the point? We want to see the discrepancy and improve.


### YOLO model
YOLO is an updated version of SSD. Basically in yolo you can easily detect the object. And in the code we have basically used the module by `ultralytics`s YOLO implementation which is SOTA of its time.
The `training-1-yolo.ipynb` file is reponsible for training the full model with 100 epoch.

And again, the `yolo_inference.py` file gives you the commands in commented format.
