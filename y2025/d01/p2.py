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
 
def getInputData(inputFile):
    raw = getStrings(inputFile)
    
    
    processed=[(entry[0], int(entry[1:])) for entry in raw]

    return processed 

def solution(inputFile):
    result = 0
    
    oldPos = pos = 50
    inputData = getInputData(inputFile)

    for move in inputData:
        result += (move[1] - move[1]%100)/100
        pos = (pos+ (move[1] if move[0] == 'R' else -move[1]))%100
        
        if pos==0 or (oldPos!=0 and ((move[0] == 'L' and pos>oldPos) or (move[0] == 'R' and pos<oldPos))):
            result+=1

        log(move, oldPos, pos, result)
        oldPos = pos 

    # log(red())
    return (result, EXPECTED_RESULT)