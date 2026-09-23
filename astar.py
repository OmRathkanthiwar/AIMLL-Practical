import heapq
import os

# MAZE

maze = [
    list("###############"),
    list("#P     #     G#"),
    list("# ###     ### #"),
    list("#             #"),
    list("###############")
]

ROWS = len(maze)
COLS = len(maze[0])


# CLEAR SCREEN

def clear():
    os.system("cls" if os.name == "nt" else "clear")


# DISPLAY MAZE

def printMaze():
    clear()

    for row in maze:
        print("".join(row))


# FIND POSITION

def find(ch):

    for i in range(ROWS):
        for j in range(COLS):

            if maze[i][j] == ch:
                return (i, j)


# HEURISTIC

def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


# GET NEIGHBOURS

def getNeighbors(node):

    r, c = node

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    neighbors = []

    for dr, dc in moves:

        nr = r + dr
        nc = c + dc

        if 0 <= nr < ROWS and 0 <= nc < COLS:

            if maze[nr][nc] != '#':
                neighbors.append((nr, nc))

    return neighbors


# REMOVE HINT

def clearStars():

    for i in range(ROWS):
        for j in range(COLS):

            if maze[i][j] == '*':
                maze[i][j] = ' '


# A* HINT

def hint():

    start = find('P')
    goal = find('G')

    clearStars()

    bestF = float("inf")
    bestNode = None

    print("\nCurrent Position:", start)
    print("\nPossible Moves")
    print("Direction\tg\th\tf")

    for nextNode in getNeighbors(start):

        g = 1
        h = heuristic(nextNode, goal)
        f = g + h

        if nextNode[0] < start[0]:
            direction = "Up"

        elif nextNode[0] > start[0]:
            direction = "Down"

        elif nextNode[1] < start[1]:
            direction = "Left"

        else:
            direction = "Right"

        print(direction, "\t\t", g, "\t", h, "\t", f)

        if f < bestF:
            bestF = f
            bestNode = nextNode

    if bestNode:

        r, c = bestNode
        maze[r][c] = '*'

        print("\nBest Move:", bestNode)
        print("Minimum f:", bestF)

    input("\nPress Enter...")


# GAME

while True:

    printMaze()

    print("\nControls")
    print("W = Up")
    print("S = Down")
    print("A = Left")
    print("D = Right")
    print("H = Hint")
    print("Q = Quit")

    move = input("\nEnter Choice: ").lower()

    if move == 'q':
        break

    if move == 'h':
        hint()
        continue

    clearStars()

    r, c = find('P')

    nr = r
    nc = c

    if move == 'w':
        nr -= 1

    elif move == 's':
        nr += 1

    elif move == 'a':
        nc -= 1

    elif move == 'd':
        nc += 1

    else:
        continue

    if maze[nr][nc] == '#':
        continue

    if maze[nr][nc] == 'G':

        maze[r][c] = ' '
        maze[nr][nc] = 'P'

        printMaze()

        print("\nCongratulations!")
        print("You reached the Goal.")

        break

    maze[r][c] = ' '
    maze[nr][nc] = 'P'