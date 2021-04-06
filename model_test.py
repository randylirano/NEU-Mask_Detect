import os

import tensorflow as tf
import numpy as np



def decode_img(img):
    # https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg
    # please see the above link for the following function: tf.image.decode_jpeg
    img = tf.image.decode_jpeg(img, channels=3)
    # uniform the picture size, this parameter can be changed
    return tf.image.resize(img, [100, 100])


model = tf.keras.models.load_model("model_save")
x_test = []
y_test = []

ALLOWED_FORMATS = ["jpg", "jpeg", "png", "gif", "bmp"]

for filename in os.listdir("data/test_images/non_mask"):
    if filename.split(".")[1] in ALLOWED_FORMATS:
        tf_file = tf.io.read_file(os.path.join("data/test_images/non_mask", filename))
        img = decode_img(tf_file).numpy()
        x_test.append(img)
        y_test.append(0)


for filename in os.listdir("data/test_images/mask"):
    if filename.split(".")[1] in ALLOWED_FORMATS:
        tf_file = tf.io.read_file(os.path.join("data/test_images/mask", filename))
        img = decode_img(tf_file).numpy()
        x_test.append(img)
        y_test.append(1)

x_test = np.array(x_test)
y_test = np.array(y_test)

score, acc = model.evaluate(x_test, y_test, batch_size=50)
print(f"Score is {score}")
print(f"Acc is {acc}")
