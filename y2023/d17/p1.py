import sys, os, math
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils, numberUtils, geometryUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *

EXPECTED_RESULT = None

STRAIGHT_MAX_LENGTH = 3

DIRECTIONS = [
    (-1, 0), # North
    (0, 1), # East
    (1, 0), # South
    (0, -1), # West
]
 
def getInputData(inputFile):
    raw = getTuples_numbers(inputFile, "")
    
    return raw 

bestCost = 0
def travel(map, y, x, lines, cols, direction, straightLen, cost, visitedLocations, pathMap):
    # log(y,x)


    global bestCost

    if (y,x) in visitedLocations or cost>=bestCost or y==-1 or x == -1 or y == lines or x == cols:
        return

    newPathMap = matrixUtils.clone(pathMap)
    newPathMap[y][x] = 'x'
    logMatrix(newPathMap)
    time.sleep(0.3)

    if y == lines-1 and x == cols-1:
        log(blue("New best cost", cost))
        bestCost = cost
        return
    
    
    cost += map[y][x]

    leftDir = (direction-1)%len(DIRECTIONS)
    rightDir = (direction+1)%len(DIRECTIONS)

    if straightLen<STRAIGHT_MAX_LENGTH:
        travel(map, y+DIRECTIONS[direction][0], x+DIRECTIONS[direction][1], lines, cols, direction, straightLen+1, cost, visitedLocations+[(y,x)], newPathMap)
    
    travel(map, y+DIRECTIONS[leftDir][0], x+DIRECTIONS[leftDir][1], lines, cols, leftDir, 1, cost, visitedLocations+[(y,x)], newPathMap)

    travel(map, y+DIRECTIONS[rightDir][0], x+DIRECTIONS[rightDir][1], lines, cols, rightDir, 1, cost, visitedLocations+[(y,x)], newPathMap)

def solution(inputFile):
    result = 0
    
    map = getInputData(inputFile)
    (lines, cols) = matrixUtils.getDimensions(map)
    # logMatrix(map)

    # calculate an initial cost value
    global bestCost
    y = x = 0
    increaseY = False
    while (y<lines and x<cols):
        bestCost += map[y][x]
        if increaseY:
            y+=1
        else:
            x+=1

        increaseY = not increaseY
    
    log(purple("Initial best cost", bestCost))

    # start searching going east
    travel(map, 0, 0, lines, cols, 1, 1, 0, [], matrixUtils.generate(lines, cols, '.'))

    # start searching going south
    travel(map, 0, 0, lines, cols, 2, 1, 0, [], matrixUtils.generate(lines, cols, '.'))

    log(green("Final best cost",bestCost))

    # log(red())
    return (result, EXPECTED_RESULT)