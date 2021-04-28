import tensorflow as tf

data_dir = 'data/Augmented_Images'
train_ds = tf.keras.preprocessing.image_dataset_from_directory(data_dir, validation_split=0.2,
                                                               subset="training", seed=123, image_size=(100, 100))

val_ds = tf.keras.preprocessing.image_dataset_from_directory(data_dir, validation_split=0.2,
                                                             subset="validation", seed=123, image_size=(100, 100))

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

num_classes = 2

model = Sequential([
  layers.experimental.preprocessing.Rescaling(1./255, input_shape=(100, 100, 3)),
  layers.Conv2D(16, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Flatten(),
  layers.Dense(128, activation='relu'),
  layers.Dense(num_classes)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

epochs = 1
history = model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=epochs
)
# AUTOTUNE = tf.data.AUTOTUNE
#
# train_ds = ds.cache().prefetch(buffer_size=AUTOTUNE)
# model = tf.keras.models.load_model("model_save")
#
score, acc = model.evaluate(val_ds)
print(f"Score is {score}")
print(f"Acc is {acc}")

# import os
#
# import tensorflow as tf
# import numpy as np
#
#
#
# def decode_img(img):
#     # https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg
#     # please see the above link for the following function: tf.image.decode_jpeg
#     img = tf.image.decode_jpeg(img, channels=3)
#     # uniform the picture size, this parameter can be changed
#     return tf.image.resize(img, [100, 100])
#
#
# model = tf.keras.models.load_model("model_save")
# x_test = []
# y_test = []
#
# ALLOWED_FORMATS = ["jpg", "jpeg", "png", "gif", "bmp"]
#
# for filename in os.listdir("data/Augmented_Images/noMaskAugmented"):
#     if filename.split(".")[1] in ALLOWED_FORMATS:
#         tf_file = tf.io.read_file(os.path.join("data/Augmented_Images/noMaskAugmented", filename))
#         img = decode_img(tf_file).numpy()
#         x_test.append(img)
#         y_test.append(0)
#
#
# for filename in os.listdir("data/Augmented_Images/MaskAugmented"):
#     if filename.split(".")[1] in ALLOWED_FORMATS:
#         tf_file = tf.io.read_file(os.path.join("data/Augmented_Images/MaskAugmented", filename))
#         img = decode_img(tf_file).numpy()
#         x_test.append(img)
#         y_test.append(1)
#
# x_test = np.array(x_test)
# y_test = np.array(y_test)
#
# score, acc = model.evaluate(x_test, y_test, batch_size=50)
# print(f"Score is {score}")
# print(f"Acc is {acc}")
