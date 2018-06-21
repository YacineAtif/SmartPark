# %matplotlib inline
import csv

import numpy as np
import pandas as pd
from Draw import drawMarkovChain


def availability_forecast(periodLength, futureMinutes, states, currentState):
    # Possible sequences of events



    arrivalPeriod = futureMinutes // periodLength
    arrivalPeriodTime = futureMinutes % periodLength

    # if futureMinutes < periodLength:
    #   print("Availability probality is " + str(max(q_df.loc[states[arrivalPeriodState]] )))
    # else:
    # print("Multiperdiod")
    with open('Data/transitionMatrix.csv', 'r') as f:
        with open('Data/transitionMatrix.csv', newline='') as file:
            reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
            n = []
            for row in reader:
                n.append(row)
    # new_transition_matrix = np.matmul(n, n)
    new_transition_matrix = np.linalg.matrix_power(n, arrivalPeriod + 1)
    # print(new_transition_matrix)

    x = new_transition_matrix[states.index(currentState)].max()
    y = new_transition_matrix[states.index(currentState)].argmax()
    print("Current State is " + currentState)
    print("Expected arrival period is " + str(arrivalPeriod))
    print("Expected arrival time relative to period is " + str(arrivalPeriodTime))
    # print("Highest availability probality is " + str(x))
    print("Expected state on arrival is " + states[y])
    # print(new_transition_matrix[arrivalPeriodState].index(x))
    # print (indices)

