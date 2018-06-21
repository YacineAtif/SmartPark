import csv
from datetime import datetime
import random
import scipy
from numpy import genfromtxt
import sklearn.preprocessing
import networkx as nx
import pandas as pd
# from graphviz import Digraph
# import pydotplus
import numpy as np
import Draw

import collections

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Total = 100  # no of parking spots
#StatePercenetage = 0.2  # growth ratio of availability per increasing state
#ArrivalRate = 10
# cars arriving per minute, all ariving cars park within the minute
# We assumeno cars leave during the observed period
# Cars leave if parking full

#InitalAvailabilityRate = 0.9  # Initial availablity rate

#PeriodLength = 5
#N = 10  # no of samples



def createSimilarPeriods(PeriodLength, N, Total, ArrivalRate, InitalAvailabilityRate):
    file = open('Data/Periods.csv', 'w')
    for i in range(N):
        random.seed(datetime.now())
        x = np.random.randint(0, InitalAvailabilityRate * Total)
        for i in range(PeriodLength):
            file.write(str(x) + '\n')
            if x > ArrivalRate:
                x = np.random.randint(x - ArrivalRate, x)
            else:
                x = 0
            # file.write("----" + '\n')


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def createStateMatrix(Total, PeriodLength, N, StatePercenetage):
    n = genfromtxt("Data/Periods.csv", delimiter='\n')
    m = n.astype(int)
    ll = list(chunks(m, 5))
    #print(ll)
    # #ll=m.flatten()
    # #n = [0] * PeriodLength

    a = [[0] * (PeriodLength + 1)] * N
    a = np.asarray(a)

    for i in range(len(ll)):
        for j in range(len(ll[i])):
            element = ll[i][j]
            if 0 < element < Total * StatePercenetage:
                a[i][j] = 1
            elif Total * StatePercenetage < element < Total * StatePercenetage * 2:
                a[i][j] = 2
            elif Total * StatePercenetage * 2 < element < Total * StatePercenetage * 3:
                a[i][j] = 3
            elif Total * StatePercenetage * 3 < element < Total * StatePercenetage * 4:
                a[i][j] = 4
            elif Total * StatePercenetage * 4 < element < Total * StatePercenetage * 5:
                a[i][j] = 5

    return a


def createFrequencyMatrix(a, PeriodLength):
    #b = [PeriodLength + 1][PeriodLength + 1]
    c = [[0] * (PeriodLength + 1)] * (PeriodLength + 1)
    c = np.asarray(c)
    for i in range(len(a)):
        for j in range(len(a[i])-1):
                c[a[i][j]][a[i][j+1]]+=1


    return(c)



# createSimilarPeriods()

def createParkingStatesWithinPeriod(totalSpots, availabilityGrowth, periodLength,
                                 numSamples):
    a = createStateMatrix(totalSpots, periodLength, numSamples, availabilityGrowth)
    c = createFrequencyMatrix(a, periodLength)
    dd = np.around(c, decimals=1)
    transitionMatrix = sklearn.preprocessing.normalize(dd, axis=1, norm='l1')
    np.savetxt("Data/transitionMatrix.csv", transitionMatrix, fmt="%1.2f", delimiter=",")

#print(a)

#        if item == 0: ++n[0]


# print(n)
