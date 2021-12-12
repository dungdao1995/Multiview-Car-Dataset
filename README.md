# Multiview-Car-Dataset
The dataset on this page contains 20 sequences of cars as they rotate by 360 degrees. There is one image approximately every 3-4 degrees. Using the time of capture information from the photos, it is possible to calculate the approximate rotation angle of the car.

The photos have been captured using a Nikon D70 camera on a tripod at the Geneva International Motor Show ’08. The lens used is Nikkor 12-24mm DX f/4. The focal length was kept constant during a single sequence (showing a single car) but varies from sequence to sequence. The focus was set to manual, approx. at the hyperfocal distance.

All videos and images available from this page are copyrighted by CVLab – EPFL. You are free to use them for research purposes. If you use them to publish results, please cite the reference below.
<img width="612" alt="Screen Shot 2021-12-12 at 6 56 30 PM" src="https://user-images.githubusercontent.com/53828158/145723786-fccf1bd0-10b3-46f1-af66-125643fd39c4.png">


#https://www.epfl.ch/labs/cvlab/data/data-pose-index-php/

#Result
<img width="458" alt="Screen Shot 2021-12-12 at 6 57 54 PM" src="https://user-images.githubusercontent.com/53828158/145723832-a3b12236-cac9-4edd-b959-773da3755fd2.png">

#Process

A. The first problem I get is Data Preprocessing. The dataset for the last
model is not good enough to build, so I have clarified the exact degree(angle) of the car for each image. According to that, I have split the data into 4 classes (front, rear, left side, right side) for training and validation processes => The quantity and quality of dataset are better.
B
Secondly, in the Data Augmentation phase, I got a mistake when using the built-in library ImageDataGenerator. I used the Rotation and horizontal_flip parameters to generating new images to train the model, but I got the wrong result because the newly generated images are too different from original images. Therefore, I just choose some parameters for data augmentation phase:
• width_shift_range=0.2
• height_shift_range=0.2
The value 0.2 because I still have the car in the new image even though it is randomly shifted vertically or
• zoom_range=[0.3, 1] : A randomly zoom less than 1.0 magnifies the image
• shear_range = 0.2: Shear' means that the image will be distorted along an axis, mostly to create or rectify the perception angles. It's usually used to augment images so that computers can see how humans see things from different angles.
• fill_mode='nearest',:
the default option where the closest pixel
value is chosen and repeated for all the empty values
• rescale=1./255: This method multiplies the values of any data before any additional processing. We know the original images consists of 0-255 in RGB coefficients, which is very high for our models to process. Because of which we scaled our images with 1. /255 factors.
#Conclusion
From the model, I figure out that the most important of building the new model is clean input data. We need to clean and have enough quantity of images to build the model. Besides that, when I want to use data augmentation, I need to consider parameters in the ImageDataGenerator because it can make the new images are too different from our original images and it leads to the bad result.
