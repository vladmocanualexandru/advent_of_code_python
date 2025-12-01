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
    
    pos = 50
    inputData = getInputData(inputFile)

    for move in inputData:
        pos = (pos+ (move[1] if move[0] == 'R' else -move[1]))%100
        if pos == 0: result+=1
        log(move, pos)

    # log(red())
    return (result, EXPECTED_RESULT)