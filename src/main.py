from atar import *
from encoder import *
from conv import *

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

if __name__ == '__main__':
    main()

