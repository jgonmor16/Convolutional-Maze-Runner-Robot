from atar import *
from encoder import *
from conv import *
from blue import *

def main():

    # Conv Neural Network
    maze = conv(3)
    print(maze)
   
    # A* Pathfinding Algorithm
    start = (7, 0)
    end = (1, 0)
    path = astar(maze, start, end)
    print(path)

    # Encoder
    orders = encoder(path)
    print(orders)

    # Send orders via Bluetooth
    blue(orders)

if __name__ == '__main__':
    main()

