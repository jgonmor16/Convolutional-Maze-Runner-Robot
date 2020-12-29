# PROYECTO 

ABOUT
----
The idea behind this project is to create a system able to control the movement
of a robot around its factory. This system, when given an starting and an
ending point, will:
* Take a "picture" of the current status of the factory
* Then use an Convolutional Neural Network to codify it as a maze
* Run an A* Pathfinding Algorithm to find the shortest route
* Encode the resulting route as instructions
* Send then via Bluetooth to the Arduino moduled attached to the robot

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

PROJECT DIRECTORY STRUCTURE
---------------------------

### src/
* *main.py:* Main file
* *conv.py:* Convolutional Neural Network
* *atar.py:* A\* Pathfinding Algorithm
* *encoder.py:* Encoder of intructions
* *blue.py:* Bluetooth comunication with Arduino

#### src/lib/
Custom libreries requiered to run conv.py
* *conv_model.py:* Model functions
* *img_data.py:* Loading/labeling data functions

### doc/
Documentation of project.

### data/
Checkpoints achieved by model (the later, the better) containg the wheight of
each neural network node.

### img/
Please note that this folder is not included in repo. Must be provided by user.
* _\*.jpg:_ Images generated to test the project. Naming: *fab.<n>.jpg*
* *ts_data.csv:* Expected solution from images used to check the output of
neural network model

### README.md
This file
