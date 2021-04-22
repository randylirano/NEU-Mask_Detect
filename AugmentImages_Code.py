#!/usr/bin/env python
# coding: utf-8

# In[54]:


get_ipython().system('pip install Keras')
get_ipython().system('pip install tensorflow')

# Importing necessary functions
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
   
# Initialising the ImageDataGenerator class.
# We will pass in the augmentation parameters in the constructor.
datagen = ImageDataGenerator(
        rotation_range = 40,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True,
        brightness_range = (0.5, 1.5))

import glob

list_of_files = glob.glob('Desktop/mask5/*.jpg')

for file in list_of_files:
    # Loading a sample image 
    img = load_img(file) 
    # Converting the input sample image to an array
    x = img_to_array(img)
    # Reshaping the input image
    x = x.reshape((1, ) + x.shape) 

    # Generating and saving 5 augmented samples 
    # using the above defined parameters. 
    i = 0
    for batch in datagen.flow(x, batch_size = 1, shuffle=True, save_to_dir ='Desktop/MaskAugmented', save_prefix ='image_Mask5', save_format ='jpeg'):
        i += 1
        if i > 3:
            break


# In[ ]:




