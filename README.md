# CONVOLUTIONAL MAZE RUNNER ROBOT 

ABOUT
-----
The idea behind this project is to create a system able to control the
movement of a robot around its factory. This system, when given an starting
and an ending point, will:
* Take a "picture" of the current status of the factory
* Use a trained Convolutional Neural Network to codify the picture into a
maze
* Run the A* Pathfinding Algorithm to find the shortest route
* Encode the resulting route as instructions
* Send the instructuions via Bluetooth to the Arduino moduled attached to the
robot

LIBRARIES REQUIERED
-------------------
Python3 libraries requiered to run this project:
* OpenCV:
```
pip3 install opencv-python
```
* tqdm:
```
pip3 install tqdm
```
* numpy:
```
pip3 install numpy
```
* pybluez
```
pip3 install pybluez
```

Bluetooth and its libreries are also required to pair with the the HC-05
bluetooth device (connected to the arduino robot):
* bluetooth:
```
sudo apt-get install bluetooth libbluetooth-dev
```

Please follow this tutorial to connect and pair the raspberry with the
HC-05 device: <https://dev.to/ivanmoreno/how-to-connect-raspberry-pi-with-hc-05-bluetooth-module-arduino-programm-3h7a#pair-with-hc05-module>

### RaspAP Control Panel
This modified configuration portal is used to change between AUTO and
MANUAL modes, to control directions during manual control and to set the
starting and ending coordinates when AUTO mode is selected.

To install RaspAP (<https://github.com/RaspAP/raspap-webgui>):
1. Go to <https://github.com/RaspAP/raspap-webgui#prerequisites> and
perform the requiered steps to perform the quick installation.
2. Copy modified files to their destination:
```
cp <proj dir>/html/i_dashboard.php /var/www/html/includes/dashboard.php
cp <proj dir>/html/t_dashboard.php /var/www/html/templates/dashboard.php
cp <proj dir>/html/proj /var/www/html/config/
chown -R www-data:www-data /var/www/html/*
```

PROJECT DIRECTORY STRUCTURE
---------------------------

### src/
* *main.py:* Main file
* *conv.py:* Convolutional Neural Network
* *atar.py:* A\* Pathfinding Algorithm
* *encoder.py:* Intructions Encoder
* *blue.py:* Bluetooth communication with Robot

#### src/lib/
Custom libreries requiered to run *conv.py*
* *conv_model.py:* Model functions
* *img_data.py:* Loading/labeling data functions

### data/
Checkpoints achieved by model (the later, the better) containg the wheights
of each neural network node.

### img/
Please note that this folder is not included in repo. Must be provided by
user.
* _\*.jpg:_ Images generated to test the project. Naming: *fab.\<n\>.jpg*
* *ts_data.csv:* Expected solution from images used to check the output of
neural network model

### html/
* *i\_dashboard.php:* Modified RaspAP file to control robot (configuration)
* *t\_dashboard.php:* Modified RaspAP file to control robot (display)

#### html/proj
* *auto:* Control file (Auto or Manual mode)
* *coord:* Control file (Starting and Ending coords)
* *move:* Control file (Manual Movement)
* *on:* Control file (On/Off Switch)

### README.md
This file
