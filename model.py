# import necessary packages
# pandas framework for csv file reading
import pathlib

import pandas as pd
import numpy as np
import tensorflow as tf
import os
from sklearn.model_selection import train_test_split


# read the csv file
labels = pd.read_csv('data/train_labels_cleaned.csv')
# print(labels.head())

# select binary labels only and rename them
binary_labels = labels[['filename', 'label (0/1)']]
binary_labels = binary_labels.rename(columns={'label (0/1)': 'label'})

# concatenate the path name with the file name

data_dir = 'data/images/'
filepath = [[filename, data_dir + filename] for filename in labels['filename']]
# print(file_paths)

# save the paths to a pandas dataframe
pd_filepath = pd.DataFrame(filepath, columns=['filename', 'filepaths'])
# print(pd_filepath.head())

data = pd.merge(pd_filepath, binary_labels, how='inner', on='filename')

# train, test, validation split, with a random seed of 42
# train_val_set, test_set = train_test_split(data, test_size=0.1, random_state=42)
# train_set, val_set = train_test_split(train_val_set, test_size=0.2, random_state=42)
image_data = []

# pip install pillow
import PIL
from PIL import Image
image = tf.keras.preprocessing.image.load_img('data')







"""
# for i in range(len(data)):

import cv2
image_size = 100      # image size taken is 100 here. one can take other size too
for i in range(len(data)):
    img_array = cv2.imread(data['filepaths'][i], cv2.IMREAD_GRAYSCALE)  # converting the image to gray scale

    new_img_array = cv2.resize(img_array, (image_size, image_size))      # resizing the image array
    # print(new_img_array)
    # encoding the labels. with_mask = 1 and without_mask = 0
    if data['label'][i] == 1:
        image_data.append([new_img_array, 1])
    else:
        image_data.append([new_img_array, 0])

# print(data[0])

image_data = np.array(image_data)
np.random.shuffle(image_data)

x = []
y = []
for image in image_data:
  x.append(image[0])
  y.append(image[1])

# converting x & y to numpy array as they are list
x = np.array(x)
y = np.array(y)

x = x / 255

X_train, X_val, y_train, y_val = train_test_split(x,y,test_size=0.3, random_state = 42)

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(100, 100)),    # flattening the image
    tf.keras.layers.Dense(100, activation='relu'),
    tf.keras.layers.Dense(50, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10, batch_size = 20)

model.evaluate(X_val, y_val)
"""



