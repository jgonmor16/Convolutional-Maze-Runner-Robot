# PROYECTO 

ABOUT
----
The idea behind this proyect is to create a system able to control the movement
of a robot around its factory. This system, when given an starting and an
ending point, will:
* Take a "picture" of the currente status of the factory
* Then usean IA to codify it
* Run an A* Pathfinding Algorithm to find the shortest route
* Encode then
* Send then via Bluetooth to the robot

LIBRARIES REQUIERED
-------------------
A buch of python3 libraries are requiered to run this proyect.:
* OpenCV:
```
pip3 install opencv-python
```
* tqdm:
```
pip3 install tqdm
```

SRC
---
* *main.py*: Main file
* *conv.py*: Convolutional Neural Network
* *atar.py*: A* Pathfinding Algorithm
* *encoder.py*: Encoder of  intructions
* *blue.py*: Bluetooth comunication with Arduino

### SRC/LIB
Custom libreries requiered to run conv.py
* *conv\_model.py*: Model functions
* *img\_data.py*: Loading/labeling data functions

DOC
---
Documentation of proyect.

DATA
----
Checkpoints achieved by model (the later, the better) containg the wheight of
each neural network node.

IMG
---
* *\*.jpg*: Images generated to test the proyect
* *ts\_data.csv*: Expected solution from images used to check the output of
neural network model

README.md
---------
This file
