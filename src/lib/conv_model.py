###############################################################################
# LIBRARIES AND VARIABLES
###############################################################################
import tensorflow as tf
from tensorflow.keras import *
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
import os
import csv
import numpy as np
### PATHS ###
ROOT_PATH = os.getcwd().replace('src','')
DATA_DIR = ROOT_PATH + "/data/"
TEST_DIR = ROOT_PATH + "/img/"

CHECKPOINT_PATH = DATA_DIR + "/cp-{epoch:04d}.ckpt"
CHECKPOINT_DIR = os.path.dirname(CHECKPOINT_PATH)

IMG_SIZE = 256

###############################################################################
# LABEL IMAGES
###############################################################################
def label_img(img, label_data):
  index = int(img.split('.')[1])
  start = index*8
  end = (index+1)*8

  result = np.array(label_data[start:end,:])

  return result

###############################################################################
# CREATE TRAINING DATA
###############################################################################
def create_training_data():
  X = []
  y = []
  data = csv.reader(open(DATA_DIR + 'tr_data.csv', "rt"),
                      delimiter=",")
  x = list(data)
  label_data = np.array(x).astype("float32")

  for img in tqdm(os.listdir(DATA_DIR)):
    y.append(label_img(img, label_data))
    path = os.path.join(DATA_DIR, img)
    X.append(cv2.imread(path, cv2.IMREAD_GRAYSCALE))

  X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
  y = np.array(y).reshape(-1, 8, 8, 1) #8x8xN

  return X, y

###############################################################################
# LOAD TEST IMG
###############################################################################
def load_test_img(num):
  y = []
  data = csv.reader(open(TEST_DIR + 'ts_data.csv', "rt"),
                      delimiter=",")
  x = list(data)
  label_data = np.array(x).astype("float32")

  img = TEST_DIR + 'fab.' + str(num) + '.jpg'

  y.append(label_img(img, label_data))
  y = np.array(y).reshape(-1, 8, 8, 1)

  return y
###############################################################################
# NEURAL NETWORK FUNCTIONS
###############################################################################
# Convolutional Sample Layer
def downsample(filters, kernel_size, strides):
  result = Sequential()

  # Convolutional Layer
  result.add(Conv2D(filters,
                    kernel_size,  #(4x4)
                    strides,
                    padding='same'))
  # Activation Layer
  result.add(tf.keras.layers.ReLU())
  # MaxPooling2D Layer
  result.add(MaxPool2D(pool_size=2))

  return result

# Last Convolutional Layer
def downsample_last(filters, kernel_size, strides):
  result = Sequential()

  result.add(Conv2D(filters,
                    kernel_size,  #(4x4)
                    strides,
                    padding = 'same',
                    activation = 'sigmoid'))

  return result

### NETWORK FUNCTION ###
def Convolutional():
  inputs = tf.keras.layers.Input(shape=[256,256,1])

  down_stack = [                 # Starting DIMENSION   # (bs, 256, 256, 1)
                downsample(128,4,1),                    # (bs, 128, 128, 128)
                downsample(128,4,1),                    # (bs,  64,  64, 128)
                downsample(64,4,1),                     # (bs,  32,  32, 64)
                downsample(32,4,1),                     # (bs,  16,  16, 32)
                downsample_last(1,4,2)                  # (bs,   8,   8, 1)
  ]

  initializer = tf.random_normal_initializer(0, 0.02)
  iter_resut = inputs

  # Propragation through layers
  for down in down_stack:
    iter_resut = down(iter_resut)


  return Model(inputs=inputs, outputs=iter_resut)

###############################################################################
# CONVOLUTIONAL NETWORK MODEL
###############################################################################
def conv_model():
  conv = Convolutional()

  conv.compile(optimizer='adam',
               loss='binary_crossentropy',
               metrics=['accuracy'])

  return conv

def train_conv_model(conv, epochs, X, y, batch_size):
  # Create a callback that saves the model's weights
  cp_callback = tf.keras.callbacks.ModelCheckpoint(
                    filepath=CHECKPOINT_PATH,
                    save_weights_only=True,
                    monitor='val_accuracy',
                    mode='max',
                    save_best_only=True,
                    verbose=1)
  
  # Train model
  history = conv.fit(X, y,            # Train and validation data
                     batch_size,
                     epochs=epochs,
                     validation_split=0.25,
                     callbacks=[cp_callback])
  
  return history

def plot_train_results(history, epochs):
  acc = history.history['accuracy']
  val_acc = history.history['val_accuracy']
  
  loss = history.history['loss']
  val_loss = history.history['val_loss']
  
  epochs_range = range(epochs)
  
  plt.figure(figsize=(8, 8))
  plt.subplot(1, 2, 1)
  plt.plot(epochs_range, acc, label='Training Accuracy')
  plt.plot(epochs_range, val_acc, label='Validation Accuracy')
  plt.legend(loc='lower right')
  plt.title('Training and Validation Accuracy')
  
  plt.subplot(1, 2, 2)
  plt.plot(epochs_range, loss, label='Training Loss')
  plt.plot(epochs_range, val_loss, label='Validation Loss')
  plt.legend(loc='upper right')
  plt.title('Training and Validation Loss')
  plt.show()

def plot_results(ts_img, predict, y):
  sol = y.reshape(-1,8,8,1)
  plt.subplot(1, 3, 1)
  plt.imshow(ts_img[0,...,-1], cmap='gray')
  plt.title('Image')
  plt.subplot(1, 3, 2)
  plt.imshow(predict[0,...,-1]*255, cmap='gray')
  plt.title('Prediction')
  plt.subplot(1, 3, 3)
  plt.imshow(sol[0,...,-1]*255, cmap='gray')
  plt.title('Reality')
  plt.show()
