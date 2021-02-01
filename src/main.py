from atar import *
from encoder import *
from conv import *
from blue import *
from load import *
import time as t

def main():

    while(1):
        while (load("on")=="1" and load("auto")=="1"):
            # Load Data
            coord = load("coord").split(' ')
            x0, y0 = int(coord[0]), int(coord[1])
            x1, y1 = int(coord[2]), int(coord[3])

            # Conv Neural Network
            maze = conv(3)
            print(maze)
           
            # A* Pathfinding Algorithm
            start = (x0, y0)
            end = (x1, y1)
            path = astar(maze, start, end)
            print(path)

            # Encoder
            orders = encoder(path)
            print(orders)

            # Send orders via Bluetooth
            blue(orders)

            # Cambiamos a modo OFF
            
        while (load("on")=="1" and load("auto")=="0"):
            # Division en coordenadas
            move = load("move")
            # Enviar por bluetoooth
            blue(move)
            # Comprobar OFF o AUTO
            t.sleep(0.1)

        t.sleep(0.3)


if __name__ == '__main__':
    main()

