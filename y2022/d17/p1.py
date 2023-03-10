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
 
ROCK_COUNT = 2022

def getInputData(inputFile):
    raw = getText(inputFile)

    rocks = []

    rocks.append([(0,0),(0,1),(0,2),(0,3)])
    rocks.append([(0,1),(1,0),(1,1),(1,2),(2,1)])
    rocks.append([(0,2),(1,2),(2,0),(2,1),(2,2)])
    rocks.append([(0,0),(1,0),(2,0),(3,0)])
    rocks.append([(0,0),(0,1),(1,0),(1,1)])
    
    processed=(rocks, raw)

    return processed 

def solution(inputFile):
    (rocks, gusts) = getInputData(inputFile)

    # init cave
    cave = matrixUtils.generate(1, 9, '-')
    cave[0][0] = '+'
    cave[0][8] = '+'

    gustIndex = 0
    result=0
    # simulate ROCK_COUNT rocks
    for rockIndex in range(ROCK_COUNT):
        # logMatrix(cave)

        rockY = 0
        rockX = 3

        # create new rock at top
        rock = rocks[rockIndex%len(rocks)]
        for lineIndex in range(len(cave)):
            if cave[lineIndex]!=['|','.','.','.','.','.','.','.','|']:
                rockHeight = max([coord[0] for coord in rock])+1

                if (rockHeight+3-lineIndex)<0:
                    rockY=0-(rockHeight+3-lineIndex)
                cave = [['|','.','.','.','.','.','.','.','|'] for i in range(rockHeight+3-lineIndex)] + cave
                break

        # let rock settle
        rockSettled = False
        while not rockSettled:
            # apply wind gust
            gustValue = -1 if gusts[gustIndex] == '<' else 1
            gustIndex=(gustIndex+1)%len(gusts)
            
            for (coordY, coordX) in rock:
                if cave[rockY+coordY][rockX+coordX+gustValue] != '.':
                    break
            else:
                rockX+=gustValue

            # apply gravity
            for (coordY, coordX) in rock:
                # log(len(cave), coordY)
                if cave[rockY+coordY+1][rockX+coordX] != '.':
                    rockSettled = True
                    break
            else:
                rockY+=1

        # add rock to cave
        for (coordY, coordX) in rock:
            cave[rockY+coordY][rockX+coordX] = '#'

        for lineIndex in range(0,len(cave)):
            if cave[lineIndex]==['|','#','#','#','#','#','#','#','|']:
                result+=len(cave)-lineIndex-1
                cave = cave[:lineIndex]+[['+','-','-','-','-','-','-','-','+']]
                break


    for lineIndex in range(len(cave)):
        if cave[lineIndex]!=['|','.','.','.','.','.','.','.','|']:
            result += (len(cave)-lineIndex)-1
            break

    return result