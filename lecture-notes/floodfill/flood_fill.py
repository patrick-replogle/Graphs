from os import system
import time

image = [
    list("...#######......."),
    list("...#.....#......."),
    list("...#.....#......."),
    list("...#...####......"),
    list("...#####...#####."),
    list("...#...........#."),
    list("...#############."),
    list(".................")
]


def print_image():
    for line in image:
        print("".join(line))


# visual representation of the stack
depth = 0


def floodfill(row, col, c):
    global depth

    depth += 1
    # this is just to watch the floodfilling live
    system('clear')
    print_image()
    print(">" * depth)
    time.sleep(0.25)
    # first check if row and col are in bounds
    if row < 0 or row > len(image) - 1 or col < 0 or col > len(image[0]) - 1:
        depth -= 1
        return
        # base case to see if coordinate is already floodfilled
    if image[row][col] != ".":
        depth -= 1
        return
    # fill the coordinate
    image[row][col] = c

    # recursively try to fill each neighbor pixel
    floodfill(row - 1, col, c)
    floodfill(row+1, col, c)
    floodfill(row, col+1, c)
    floodfill(row, col-1, c)

    depth -= 1


floodfill(2, 5, '*')
floodfill(5, 5, '$')
floodfill(0, 2, '!')
