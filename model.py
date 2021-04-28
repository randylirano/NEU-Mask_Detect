# please make sure all packages are installed on local machine
# if not, use pip install
# pandas framework for reading csv file
# numpy for storing decoded images
# tensorflow for CNN training
# train_test_split for train validation split
# cv2 for enabling camera
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
import cv2

# read the csv label file from local disk
labels = pd.read_csv('data/train_labels_cleaned.csv')

# select binary labels only and rename them
binary_labels = labels[['filename', 'label (0/1)']]
label_only = labels[['label (0/1)']]
binary_labels = binary_labels.rename(columns={'label (0/1)': 'label'})

# concatenate the path name with the file name
data_dir = 'data/images/'
filepath = [[filename, data_dir + filename] for filename in labels['filename']]

# save the paths to a pandas dataframe
pd_filepath = pd.DataFrame(filepath, columns=['filename', 'filepath'])

# this data table contains file name, file path, and labels
data = pd.merge(pd_filepath, binary_labels, how='inner', on='filename')


# print(data.head())

# convert an image file to an array
def decode_img(img):
    # https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg
    # please see the above link for the following function: tf.image.decode_jpeg
    img = tf.image.decode_jpeg(img, channels=3)
    # uniform picture sizes, this parameter can be tuned
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

# model, the layers in this part can be tuned
# to improve the model, feel free to adjust/add/delete the following layers
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

# binary crossentropy is a loss function that is used in binary classification tasks
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# epochs can be tuned
model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=3)
model.save("model_save")


# create a video capture
cap = cv2.VideoCapture(0)


def camera_input_color(cap):
    status = ""
    while True:
        # capture frame
        ret, frame = cap.read()

        font = cv2.FONT_HERSHEY_SIMPLEX

        # use putText() method for inserting text on video
        cv2.putText(frame, status, (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4)

        color = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        # display the frame
        cv2.imshow('frame', color)
        # save the image continuously on local disk
        cv2.imwrite('data/captured_images/c1.jpg', frame)
        # read the image
        captured_img = tf.io.read_file('data/captured_images/c1.jpg')
        # decode the image and store it in a numpy array
        captured_img = decode_img(captured_img).numpy()
        # create a batch
        captured_img = (np.expand_dims(captured_img, 0))
        # predict the image
        prob = model.predict(captured_img)
        # 0.9 can be tuned
        if prob[0][0] > 0.9:
            status = "With mask"
        else:
            status = "No mask"

        # turn off the camera on signal "q"
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def release_camera(cap):
    # release the capture
    cap.release()
    cv2.destroyAllWindows()


camera_input_color(cap)
release_camera(cap)
