from atar import *
from encoder import *
from conv import *
from blue import *
from load import *
import time as t

def main():
    move_old = load("move")
    auto_old = load("auto")
    on_old = load("on")
    superdecorate("CONVOLUTIONAL MAZE RUNNER ROBOT")
    imp(None, on_old)
    imp(auto_old, None)
    
    while(1):
        # Check if there is any change in mode or status
        on, auto = load("on"), load("auto")
        if(on != on_old):
            imp(None, on)
        if(auto != auto_old):
            imp(auto, None)

        while (load("on")=="1" and load("auto")=="1"):
            # Load Data
            decorate("Loading Data")
            coord = load("coord").split(' ')
            x0, y0 = int(coord[0]), int(coord[1])
            x1, y1 = int(coord[2]), int(coord[3])
            print("Starting Point: (" + str(x0) + "," + str(y0) + ")")
            print("Ending Point: (" + str(x1) + "," + str(y1) + ")")

            # Conv Neural Network
            decorate("Running Convolutional Neural Network")
            maze = conv(0)
            print("Walls detected:")
            print(maze)
            
            # A* Pathfinding Algorithm
            decorate("Running A* Pathfinding Algorithm")
            start = (x0, y0)
            end = (x1, y1)
            path = astar(maze, start, end)
            print("Shortest path found: " + str(path))

            # Encoder
            decorate("Encoding Data")
            orders = encoder(path)
            print("Orders encoded: " + str(orders))

            # Send orders via Bluetooth
            decorate("Sending orders to Robot")
            #blue_auto(orders)
            print("Orders sent")

            # Change mode to OFF
            write("on",0)

        while (load("on")=="1" and load("auto")=="0"):
            # Load manual control
            move = load("move")
            if (move != move_old):
                imp(move, None)
                # Send orther via bluetoooth
                #blue_manual(move)
            t.sleep(0.5)
            move_old = move

        t.sleep(0.5)
        on_old, auto_old = on, auto


if __name__ == '__main__':
    main()

