from atar import *
from encoder import *

def main():

    #maze = pix2pix(img)
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 8)



    path = astar(maze, start, end)
    print(path)

    orders = encoder(path)
    print(orders)

if __name__ == '__main__':
    main()
:
