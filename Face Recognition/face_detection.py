#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Importing the Open CV library
import cv2


# In[3]:


#Loading XMLs with haar- like features for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 


# In[4]:


#Loading XMLs with haar- like features for eye detection
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 


# In[5]:


#Function for face detection
def detect(gray, frame):  
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
    for (x, y, w, h) in faces: 
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) 
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = frame[y:y+h, x:x+w] 
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3) 
        for (ex, ey, ew, eh) in eyes: 
            cv2.rectangle(roi_color,(ex, ey),(ex+ew, ey+eh), (0, 255, 0), 2) 
    return frame 


# In[6]:


#Use camera on the machine to capture real-time video
video_capture = cv2.VideoCapture(0) 


# In[7]:


#Keep detecting face till the user presses q
while True: 
    _, frame = video_capture.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    canvas = detect(gray, frame) 
    cv2.imshow('Video', canvas) 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 


# In[9]:


#When user presses q, release the video capture and close windows
video_capture.release() 
cv2.destroyAllWindows() 


# In[ ]:





# In[ ]:




