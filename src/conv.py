###############################################################################
# LIBRRARIES AND DIRECTORIES
###############################################################################
#import cv2
import numpy as np
import os
import csv
import cv2
#import matplotlib.pyplot as plt
import sys
import tensorflow as tf

### PATHS ###
ROOT_PATH = os.getcwd().replace('src','')
DATA_DIR = ROOT_PATH + "/data/"
TEST_DIR = ROOT_PATH + "/img/"

CHECKPOINT_PATH = DATA_DIR + "/cp-{epoch:04d}.ckpt"
CHECKPOINT_DIR = os.path.dirname(CHECKPOINT_PATH)

IMG_SIZE = 256

### CUSTOM LIBRARIES ###
sys.path.append(ROOT_PATH + '/src/lib')
from conv_model import *

### To prevent Unwanted Warnings ###
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

###############################################################################
# TRAINING AND RUNNING FUNCTIONS
###############################################################################
def train_conv_network(conv, X, y, epochs=100):
    print("Data Loaded -> Starting Training")
    # Train model
    batch_size = 1
    history = train_conv_model(conv, epochs, X, y, batch_size)
    # Plot results
    plot_train_results(history, epochs)

def run_conv_network(conv, sol, num):
    # Load weights
    latest = tf.train.latest_checkpoint(CHECKPOINT_DIR)
    conv.load_weights(latest).expect_partial()
    
    # Iterate over test images
    img = 'fab.' + str(num) + '.jpg'
    img_path = os.path.join(TEST_DIR, img)
    ts_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    ts_img = np.array(ts_img).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    ts_img = ts_img/255.0

    # Predict
    predict = conv.predict(ts_img)
    #plot_results(ts_img, predict, sol)

    return predict

###############################################################################
# CONVOLUTIONAL NEURAL NETWORK FUNCTION
###############################################################################
def conv(num=0, train=False):
  # Create Model and define parameters
  conv = conv_model()
  conv.summary()
  predict = None

  if train:
    print("Images available to train the model: " 
            + str(len(os.listdir(DATA_DIR))))
    X, y = create_training_data()
    X = X/255.0
    train_conv_network(conv, X, y, 300)
  else:
    sol = load_test_img(num)
    predict = run_conv_network(conv, sol, num)
    predict = predict.reshape(8,8)
    predict = np.int_(np.rint(predict))

  return predict
