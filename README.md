# Computer Vision Roadmap
This repository contains the process I am following to learn Computer Vision. I am starting from the very beginning, so the level of projects would behind from most basic and hopefully become somewhat advanced as this repository evolves. Follow along if you are keen to explore the fantastic projects you can make using Computer Vision capabilities along with Deep Learning.

# Requirements for Face Detection
1. Download [Anaconda](https://anaconda.org)
2. Download the [Installation](https://github.com/manvimadan12/Computer_Vision_Roadmap/tree/main/Face%20Recognition/Installations) files from the [Face Detection](https://github.com/manvimadan12/Computer_Vision_Roadmap/tree/main/Face%20Recognition) folder in the repository
3. Mac and Linux users, fire up the terminal. Windows users can open Anaconda Prompt after downloading Anaconda
4. Navigate to the folder with installation files using cd command
5. Run this command for setting up dependencies on Mac: `conda env create -f virtual_platform_mac.yml` 
6. Windows and Linux users can run the same command as `conda env create -f virtual_platform_windows.yml` and `conda env create -f virtual_platform_linux.yml` , respectively. 
7. This will setup a virtual_platform on your system with all the dependencies 
8. Go to Anaconda application on your machine and on the top left where you can see root, select Virtual_Platform from the drop down list
9. Download the 2 xml files, namely  haarcascade_eye.xml and harcascade_frontalface_default.xml to a known location on your machine.
10. Change the reference location of these 2 xml files while running the face_detection.py script

# Requirements for Object Detection

1. Download [Anaconda](https://anaconda.org)
2. Download the [Installation](https://github.com/manvimadan12/Computer_Vision_Roadmap/tree/main/Face%20Recognition/Installations) files from the [Face Detection](https://github.com/manvimadan12/Computer_Vision_Roadmap/tree/main/Face%20Recognition) folder in the repository
3. Mac and Linux users, fire up the terminal. Windows users can open Anaconda Prompt after downloading Anaconda
4. Navigate to the folder with installation files using cd command
5. Run this command for setting up dependencies on Mac: `conda env create -f virtual_platform_mac.yml` 
6. Windows and Linux users can run the same command as `conda env create -f virtual_platform_windows.yml` and `conda env create -f virtual_platform_linux.yml` , respectively. 
7. This will setup a virtual_platform on your system with all the dependencies 
8. Go to Anaconda application on your machine and on the top left where you can see root, select Virtual_Platform from the drop down list
9. Download the 2 xml files, namely  haarcascade_eye.xml and harcascade_frontalface_default.xml to a known location on your machine.
10. Change the reference location of these 2 xml files while running the face_detection.py script
11. Take all the files inside the Object Detection folder from Github Repository and upload them onto jupyter notebook home. ( all the files except Output, obviously!)
12. Now run the cells one-by-one in the Object Detection jupyter notebook.
13. You will see an output file being generated. Open the file and enjoy the video! 
# Results

1. Face Detection
![Face detection](https://github.com/manvimadan12/Computer_Vision_Roadmap/blob/main/Face%20Recognition/Results/Screen%20Shot%201.png "Face detection")
![Face and eyes Detection](https://github.com/manvimadan12/Computer_Vision_Roadmap/blob/main/Face%20Recognition/Results/Screen%20Shot%202.png "Face and eyes Detection")

2. Object Detection 
![Real Time Object Detection](https://github.com/manvimadan12/Computer_Vision_Roadmap/blob/main/Object%20Detection/Output/Object_detection_output_snip.png)
[Output Video](https://github.com/manvimadan12/Computer_Vision_Roadmap/blob/main/Object%20Detection/Output/output.mp4)


# Books
* [Deep Learning with Python](https://www.manning.com/books/deep-learning-with-python) 
* [Deep Learning by Ian Goodfellow and Yoshua Benjio and Aaron Cornville](https://www.deeplearningbook.org)

# Courses

# Interesting Blog Posts
* Everything you need to know about Computer Vision - [Link](https://towardsdatascience.com/everything-you-ever-wanted-to-know-about-computer-vision-heres-a-look-why-it-s-so-awesome-e8a58dfb641e)
* Viola Jones Algorithm for face detection - [Link](https://towardsdatascience.com/the-intuition-behind-facial-detection-the-viola-jones-algorithm-29d9106b6999)
* OpenCV3 Object Detection - [Link](https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Object_Detection_Face_Detection_Haar_Cascade_Classifiers.php)
* SSD - [Link](https://jonathan-hui.medium.com/ssd-object-detection-single-shot-multibox-detector-for-real-time-processing-9bd8deac0e06)
* GANs - [Link](https://hackernoon.com/how-do-gans-intuitively-work-2dda07f247a1)
# Research Papers
* [SSD](https://github.com/manvimadan12/ML-Research-Papers-/blob/master/Computer%20Vision/1512.02325.pdf)
* [Viola Jones](https://github.com/manvimadan12/ML-Research-Papers-/blob/master/Computer%20Vision/Rapid%20Object%20Detection.pdf)
