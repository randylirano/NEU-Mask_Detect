# import necessary packages
# pandas framework for csv file reading
import pandas as pd
import numpy as np
import tensorflow as tf
import os
from sklearn.model_selection import train_test_split

# read the csv file
labels = pd.read_csv('data/train_labels_cleaned.csv')
# print(labels.head())

# concatenate the path name with the file name
filepath = [[filename, 'data/images/' + filename] for filename in labels['filename']]
# print(file_paths)

# save the paths to a pandas dataframe
pd_filepath = pd.DataFrame(filepath, columns=['filename', 'filepaths'])
# print(pd_filepath.head())

data = pd.merge(pd_filepath, labels, how='inner', on='filename')
# print(data.head())

# train, test, validation split, with a random seed of 42
train_val_set, test_set = train_test_split(data, test_size=0.1, random_state=42)
train_set, val_set = train_test_split(train_val_set, test_size=0.2, random_state=42)


