import os
os.environ["TFHUB_CACHE_DIR"] = "some_dir"
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import numpy as np

import tensorflow as tf
assert tf.__version__.startswith('2')

from tflite_model_maker import model_spec
from tflite_model_maker import image_classifier
from tflite_model_maker.config import ExportFormat
from tflite_model_maker.config import QuantizationConfig
from tflite_model_maker.image_classifier import DataLoader
import matplotlib.pyplot as plt


#getting the working directory
working_directory = os.getcwd()

image_path = os.path.join(working_directory,"input")
print(image_path)
dataset = DataLoader.from_folder(image_path)
print(dataset)

train_data, rest_data = dataset.split(0.8)
validation_data, test_data = rest_data.split(0.5)

#Following code used when retraining efficientnet_lite0
efficient_model = image_classifier.create(train_data, validation_data = validation_data)#EfficientNet is default

#Following code used when retraining mobilenet_v2
mobile_model = image_classifier.create(train_data,
                                model_spec = 'mobilenet_v2',
                                validation_data = validation_data)

#Following code used when retraining resnet_50
res_model = image_classifier.create(train_data,
                                model_spec = 'resnet_50',
                                validation_data = validation_data)

#Following code is used to show a summary of each neural network, give the loss and accuracy for the networks
#and save the models to their specified file
efficient_model.summary()

loss_efficient, accuracy_efficient = efficient_model.evaluate(test_data)

efficient_model.export(export_dir='.', tflite_filename='efficientRetrained.tflite')


mobile_model.summary()

loss_mobile, accuracy_mobile = mobile_model.evaluate(test_data)

mobile_model.export(export_dir='.', tflite_filename='mobileRetrained.tflite')


res_model.summary()

loss_res, accuracy_res = res_model.evaluate(test_data)

res_model.export(export_dir='.', tflite_filename='resRetrained.tflite')