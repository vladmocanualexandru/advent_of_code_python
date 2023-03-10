import sys, os

from more_itertools import interleave

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def getInputData(inputFile):
    raw = getTuples_numbers(inputFile,' players; last marble is worth ', ' points'])
    
    processed=(raw[0][0], raw[0][1])

    return processed 


def interweave(arr1,arr2):
    i1=i2=0
    result = []

    while i1<len(arr1) and i2<len(arr2):
        result.append(arr1[i1])
        result.append(arr2[i2])

        i1+=1
        i2+=1

    result += arr1[i1:]

    return (result

def solution(inputFile):
    inputData = getInputData(inputFile)

    arr = [9,17,11,15,50,58,66,33,37,99,107,45,55,140,148,156,73,77,189,197,88,95,226,238,246,252,117,279,287,128,10,139,328,336,343,64,369,377,385,74,76,418,426,434,3,14,467,475,211,89,508,516,524,100,101,557,565,247,250,594,606,614,620,120,647,655,124,290,294,696,704,711,312,737,745,753,330,334,786,794,802,352,356,835,843,71,374,876,884,892,392,396,925,933,175,410,962,974,982,988,80,1015,1023,447,194,196,1064,1072,1079,86,1105,1113,1121,38,93,1154,1162,1170,505,221,1203,1211,530,227,1244,1252,1260,547,550,1293,1301,566,569,1330,1342,1350,1356,591,1383,1391,110,609,613,1432,1440,1447,631,1473,1481,1489,649,653,1522,1530,1538,671,675,1571,1579,685,693,1612,1620,1628,130,715,1661,1669,133,314,1698,1710,1718,1724,326,1751,1759,766,137,60,1800,1808,1815,339,1841,1849,1857,803,351,1890,1898,1906,153,65,1939,1947,364,848,1980,1988,1996,866,164,2029,2037,885,888,2066,2078,2086,2092,910,2119,2127,919,928,932,2168,2176,2183,950,2209,2217,2225,968,972,2258,2266,2274,990,994,2307,2315,1004,1008,2348,2356,2364,444,446,2397,2405,450,195,2434,2446,2454,2460,458,2487,2495,1085,469,471,2536,2544,2551,1103,2577,2585,2593,488,489,2626,2634,2642,1145,1148,2675,2683,501,1167,2716,2724,2732,1185,1189,2765,2773,1204,1207,2802,2814,2822,2828,1229,2855,2863,233,1247,1251,2904,2912,2919,1269,2945,2953,2961,42,1291,2994,3002,3010,564,1313,3043,3051,1323,576,3084,3092]
  
    for l in range(20,len(arr)):
        for l2 in range(0,len(arr),l):
            arr1 = arr[l2:l2+l]
            arr2 = arr[l2+l:l2+2*l]

            diffs = []
            if len(arr1) == len(arr2) == l:
                diffs = [arr1[i] - arr2[i] for i in range(l)]

            log(l)
            log(diffs)

        time.sleep(1)


    result = None
    return (result

 

