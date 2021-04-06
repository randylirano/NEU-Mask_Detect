# import necessary packages
# pandas framework for csv file reading
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers

# read the csv file
labels = pd.read_csv('data/train_labels_cleaned.csv')
# print(labels.head())

# select binary labels only and rename them
binary_labels = labels[['filename', 'label (0/1)']]
label_only = labels[['label (0/1)']]
binary_labels = binary_labels.rename(columns={'label (0/1)': 'label'})

# concatenate the path name with the file name
data_dir = 'data/images/'
filepath = [[filename, data_dir + filename] for filename in labels['filename']]
# print(file_paths)

# save the paths to a pandas dataframe
pd_filepath = pd.DataFrame(filepath, columns=['filename', 'filepath'])
# print(pd_filepath.head())

# this data table contains file name, file path, and labels
data = pd.merge(pd_filepath, binary_labels, how='inner', on='filename')


# print(data.head())

# convert an image file to an array
def decode_img(img):
    # https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg
    # please see the above link for the following function: tf.image.decode_jpeg
    img = tf.image.decode_jpeg(img, channels=3)
    # uniform the picture size, this parameter can be changed
    return tf.image.resize(img, [100, 100])

# x is the array of images
x = []
# y is the array of labels
y = []

# iterate through the data table
for index, row in data.iterrows():
    # read image according the filepath
    img = tf.io.read_file(row['filepath'])
    # decode, than convert to numpy format
    img = decode_img(img).numpy()
    # read label
    label = row['label']
    # append them to the arrays
    x.append(img)
    y.append(label)

# convert x, y to numpy arrays
y = np.array(y)
x = np.array(x)

# train, validation split
# no test data since we will use real images as our test data
# random_state=42, 42 is the golden standard for random seed
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=42)

# model, the items in this part can be changed
# to improve the model, feel feel to adjust/add/delete the following layers
model = tf.keras.Sequential([
    layers.experimental.preprocessing.Rescaling(1. / 255),
    layers.Conv2D(32, 3, activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# not sure about the loss function, it can be changed
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# epochs can be changed
model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=3)
model.save("model_save")
