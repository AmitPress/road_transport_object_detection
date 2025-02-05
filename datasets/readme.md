# Dataset Overview

Here, we will have a brief look at the folder structurte itself and try to comprehend which file does what thing.

#### Preprocessing
The `preprocessing.ipynb` file is reponsible for all the preprocessing related work. The full dataset is made from scratch. And now we want to make the relevant format with the clean data. For resnet50 we just need the relevant images of a class to be in the folder that is named after that class only. This way we just get a standard dataset which we can change via the library we are using such as tensorflow or pytorch.

Again, the `labels.txt` enlists 10 classes one after other in a dictionary order and this order is also maintained in the inference list as well.

#### Raw Datasets
The `road_transport_dataset_yolo_v3.zip` file is the raw dataset for the yolo inference. And, the `road_transport_dataset.zip` is for the road transport data itself which will be consumed by any vision model.