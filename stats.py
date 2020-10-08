'''Stats Exam 2'''
from math import *
from itertools import permutations
from itertools import combinations

'''Chapter 4'''
'Section 4'
def nCr(n, r):
    f = factorial
    return f(n) // f(r) // f(n - r)

def nPr(n, r):
    f = factorial
    return f(n) // f(n - r)

'''Chapter 5'''
'Section 1'
def meanOfTable(xList, pXList):
    sumOfProducts = []
    for i in range(len(xList)):
        sumOfProducts.append(xList[i] * pXList[i])
    return round(sum(sumOfProducts), 1)

def stdDevOfTable(xList, pXList):
    sumOfProducts = []
    for i in range(len(xList)):
        sumOfProducts.append(pow(xList[i], 2) * pXList[i])
    
    meanValue = meanOfTable(xList, pXList)
    return round(sqrt(sum(sumOfProducts) - pow(meanValue, 2)), 1)


'Section 2'
def binomialExact(n, p, x):
    return nCr(n, x) * pow(p, x) * pow((1-p), (n - x))

def binomialAtMost(n, p, x):
    result = 0
    for i in range(x + 1):
        result += binomialExact(n, p, i)
    return result

def binomialAtLeast(n, p, x):
    return 1 - binomialAtMost(n, p, x-1)

def meanNP(n, p):
    return n * p

def stdDevNP(n, p):
    return sqrt(meanNP(n, p) * (1 - p))

def rangeRule(n, p):
    sigLow = meanNP(n, p) - (2 * stdDevNP(n, p))
    sigHigh = meanNP(n, p) + (2 * stdDevNP(n, p))
    print('Significantly low values <= mean - 2stddev: ', sigLow)
    print('Significantly high values >= mean + 2stddev: ', sigHigh)
    return (sigLow, sigHigh)

'''Chapter 6'''
'Section 1'

'Section 2'
def zScore(xValue, meanValue, sdValue):
    return (xValue - meanValue) / sdValue

'Section 3'
def sampleMean(pair, sampleSize):
    return (pair[0] + pair[1]) / sampleSize

def sampleVariance(pair, pairMean, sampleSize):
    x = pow((pair[0] - pairMean), 2)
    y = pow((pair[1] - pairMean), 2)
    return (x + y) / (sampleSize - 1)

def sampleRange(pair):
    return abs(pair[0] - pair[1])

def sampleTable(pairList, sampleSize):
    meanList = []
    s2List = []
    samRange = []
    print("pair   median   variance   range")
    for i in range(len(pairList)):
        meanList.append(sampleMean(pairList[i], sampleSize))
        s2List.append(sampleVariance(pairList[i], meanList[-1], sampleSize))
        samRange.append(sampleRange(pairList[i]))
        print(pairList[i], ' ', meanList[-1], ' ', s2List[-1], '   ', samRange[-1])
    print("mean of sample variance: ", (sum(s2List) / len(s2List)))
    print("mean of sample median: " , (sum(meanList) / len(meanList)))
    print("mean of sample range: ", (sum(samRange) / len(samRange)))
        
        
def populationVariance(numList):
    sd = sum(numList) / len(numList)
    l = []
    for i in range(len(numList)):
        l.append(pow(numList[i] - sd, 2))
    return sum(l) / len(numList)
