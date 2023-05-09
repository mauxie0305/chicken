# chicken
Monitoring the dispersion and movement of chicken using optical flow and machine learning

## Introduction
### Background
Taiwan has a significant poultry industry. According to statistical data, there were 51 million broilers raised in 2022. The production value is 56.1 billion TWD which accounts for 28% of total production value in 21 different livestock. In terms of the results, I believe that investing in the poultry industry is well worth it.
### Problems
Taiwan is facing several problems in the poultry industry including labor shortages and an aging population. So we need to find ways to overcome these challenges and maintain productivity.
### Traditional Approach
Traditionally, manual labor was used to check the chicken coops. 
For farmers, the condition of the chicken coop can be determined by observing the chickens sitting on their haunches. A chicken's activity level may be influenced by its health condition, temperature, humidity, or the condition of the bedding material. 
When they feel uncomfortable, they tend to walk less and huddle together. Therefore, the dispersion and movement of the chickens can serve as crucial indicators for monitoring the health condition of chickens. 
All of this is labor-intensive, time-consuming, and prone to human error.  With the problems mentioned before, we want to propose a solution to it. 
## Objectives
Our research objective is to monitor chicken coops automatically, which can be divided into two parts: 1) Detecting chickens using deep learning models, and 2) Quantifying chicken's movement and dispersion to analyze their health conditions.

## Method
### Data Acquistion
For data acquisition, we designed an embedded system which includes a Raspberry Pi 3 and a fisheye camera. It was installed on the column of the chicken coop. We hope that by applying the fisheye camera, we can get the biggest field of view with the least number of cameras.

We record high-quality videos of chicken coops, enabling us to monitor the chickens without disturbing them.
On the right hand side is the annotated image.We now only extracted 25 of frames from these videos and annotated them with the positions and boundaries of individual chickens to create a dataset for model training.
### Model Training
Next, we trained a YOLOv7  model to detect chickens. YOLOv7 is a state-of-the-art object detection model known for its high accuracy and real-time performance. Our model is trained to detect and predict the positions of individual chickens. Here are my learning details.

In the training process, we first applied various data augmentation techniques to enhance the model's robustness and generalization capabilities. These techniques include flip right and left, mix-up, mosaic and shear.
### Calibration
Although we can get a better field of the view using fisheye cameras, the videos have distortion at the edges. Therefore, we need to calibrate those videos. In our research, we chose the OpenCV fisheye model to correct the distortion in the videos. However, we still use uncalibrated videos for model training since the shape of the chickens is distorted if we calibrate at first. After the model prediction is done, we then calibrate the results. By doing so, we can obtain calibrated bounding boxes and accurately quantify the values we want to research, such as dispersion and movement.
### Nearest Neighbor index
To evaluate the dispersion of chickens, we calculated the Nearest Neighbor Index (NNI). NNI is a spatial statistic that measures the degree of clustering or dispersion in a given area. 
If the index is less than 1, the pattern exhibits clustering; If the index is greater than 1, the trend is toward dispersion.
We will apply the result of the calibrated YOLOv7 prediction to quantify NNI.
### Optical Flow
For tracking the movement of the chickens, we utilized optical flow, which computes the motion vectors between consecutive frames in a video sequence. In our research, we employed the Gunnar Farneback algorithm, which is a dense optical flow method. Although it is slightly slower, it provides greater accuracy. By calculating the magnitude of vectors for each frame, we can monitor the chickens' movement and identify any unusual patterns that might warrant further investigation.
## Result
### YOLOv7 performance
Our YOLOv7 model achieved an impressive mean average precision (mAP) of 89% demonstrating its effectiveness in detecting and predicting the positions of chickens.
### Optical Flow
the results obtained using the optical flow. It seems that it can track the chicken’s movement precisely. 
Nevertheless, we still need to prove the movement calculated by optical flow can be used.

## Discussion
However, there are a few instances where the detection is not perfect. 
We believe this may be due to two reasons: first, the chickens might be moving too quickly to be detected accurately; and second, overlapping of chickens may be causing detection challenges.

To prove we can use optical flow as a indicator of movement, we refer to a previous research that quantifies movement using Simple Online and Realtime Tracking (SORT), which is a lightweight and efficient algorithm for object tracking in video streams. Our goal is to determine if there is any correlation between these two methods.

This image indicates a strong positive correlation between the two methods. Based on this comparison, we opted for the optical flow algorithm for movement analysis over YOLOv7 for several reasons.

Firstly, Optical flow is computationally more efficient, as it directly processes motion information in the video, rather than relying on object detection in each frame. This leads to faster real-time tracking of chicken movement.
Secondly, the optical flow algorithm is better at handling overlapping chickens compared to YOLOv7, as it concentrates on motion patterns instead of detecting individual chickens. 

Lastly, we compared the results of dispersion and movement and attempted to find a correlation between them. 
We can find that there are wired high points in both charts.
Therefore, we pick the video at that time.
Looking into the video, We can see that a farmer walked in and chickens were running and clustered in an area. As for the findings, it is reasonable for the weird high value of dispersion and movement.

## Conclusion
In conclusion, our system shows promise in providing real-time monitoring and early detection of potential issues in poultry farms. 

## Future works
As our next steps, we will continue refining the model, improving the calculating speed of optical flow and exploring ways to quantify the dispersion and movement in chicken coops for more efficient and effective poultry monitoring.



