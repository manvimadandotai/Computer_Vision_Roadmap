#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense


# In[2]:


# Initialising the CNN
classifier = Sequential()


# In[3]:


# Convolution
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))


# In[4]:


# Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))


# In[5]:



# Adding a second convolutional layer
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))


# In[6]:


# Step 3 - Flattening
classifier.add(Flatten())


# In[7]:


# Step 4 - Full connection
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))


# In[8]:


# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


# In[9]:


# Fitting the CNN to the images

from keras.preprocessing.image import ImageDataGenerator


# In[10]:


train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)


# In[11]:


test_datagen = ImageDataGenerator(rescale = 1./255)


# In[19]:


training_data_path = '....../dataset/training_set'


# In[20]:


training_data_path = '....../dataset/training_set'training_set = train_datagen.flow_from_directory(training_data_path,
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')


# In[21]:


test_data_path = '....../dataset/test_set'


# In[22]:


test_set = test_datagen.flow_from_directory(test_data_path,
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')


# In[23]:


classifier.fit_generator(training_set,
                         steps_per_epoch = 8000,
                         epochs = 25,
                         validation_data = test_set,
                         validation_steps = 2000)


# In[48]:


import numpy as np
from keras.preprocessing import image
 
test_image = image.load_img('....../dataset/Dog or Cat ? Predict/cat_or_dog_1.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
    prediction = 'dog'
else:
    prediction = 'cat'


# In[49]:


prediction


# In[50]:


from IPython.display import Image
Image(filename='....../dataset/Dog or Cat ? Predict/cat_or_dog_1.jpg') 


# In[ ]:





# In[ ]:




