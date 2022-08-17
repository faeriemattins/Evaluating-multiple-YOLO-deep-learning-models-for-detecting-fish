# Evaluating-multiple-YOLO-deep-learning-models-for-detecting-fish
Used various YOLO models like Yolov4, Yolov5, YoloR and Yolov7 for detecting fish. This work was presented in Dalhousie Computer Science In-House Conference 2022 (DCSI'22). The link to the paper is https://dcsi.cs.dal.ca/wp-content/uploads/2022/07/DCSI-2022_paper_2008.pdf. 

### Dataset
The dataset is taken from https://github.com/perceivelab/FishCLEF-2015. This dataset consist of 15 different species of fish. However, for simplicity, only the top 5 fish species with the highest number of fishes in the dataset were considered. There are 3 folder, Train, Test and Valid. In train and valid, the folder short refers to 5 species of fish, the other label folder refers to the complete labels with 15 species.

### Confusion Matrix
The ground truth and the prediction file must be in a certian format for the code to work. The format is :

"tvid23_frame139.jpg -> Dascyllus Reticulatus"

"tvid3_frame24.jpg -> "
