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

# Results

1. Face Detection
![Face detection](https://github.com/manvimadan12/Computer_Vision_Roadmap/blob/main/Face%20Recognition/Results/Screen%20Shot%202020-10-27%20at%209.17.42%20PM.png)
![Face and eyes Detection](https://github.com/manvimadan12/Computer_Vision_Roadmap/blob/main/Face%20Recognition/Results/Screen%20Shot%202020-10-27%20at%209.17.56%20PM.png)

# Interesting Blog Posts
* Everything you need to know about Computer Vision - [Link](https://towardsdatascience.com/everything-you-ever-wanted-to-know-about-computer-vision-heres-a-look-why-it-s-so-awesome-e8a58dfb641e)
* Viola Jones Algorithm for face detection - [Link](https://towardsdatascience.com/the-intuition-behind-facial-detection-the-viola-jones-algorithm-29d9106b6999)
* OpenCV3 Object Detection - [Link](https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Object_Detection_Face_Detection_Haar_Cascade_Classifiers.php)


