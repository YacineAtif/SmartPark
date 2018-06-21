import Data
import Search
import Draw
from Markov import availability_forecast

totalSpots = 100  # no of parking spots
availabilityGrowth = 0.2  # growth ratio of availability per increasing state, simulate departure rate
arrivalRate = 10  # during period
# cars arriving per minute, all ariving cars park within the minute
# We assumeno cars leave during the observed period
# Cars leave if parking full

initalAvailabilityRate = 0.9  # Initial availablity rate, can change for each period.

periodLength = 5

numSamplePerPeriod = 10  # no of samples

entryPoint = '0'
parkingNodes = ['2']

allStates = ['S0', 'S1', 'S2', 'S3', 'S4', 'S5']
currentState = "S1"

Data.createSimilarPeriods(periodLength, numSamplePerPeriod, totalSpots, arrivalRate, initalAvailabilityRate)

Draw.showRoutes()


(path, expectedCongestion) = Search.searchPath(entryPoint, parkingNodes[0])

print("Path to parking " + parkingNodes[0] + ": " + str(path))
print("Expected congestion to parking " + parkingNodes[0] + ": " + str(expectedCongestion))

expectedArrivalTime = int(expectedCongestion)  # obtain discrete minutes


Data.createParkingStatesWithinPeriod(totalSpots, availabilityGrowth, periodLength,
                                 numSamplePerPeriod)

# Draw.drawMarkovChain() # for one period

availability_forecast(periodLength, expectedArrivalTime, allStates, currentState)
