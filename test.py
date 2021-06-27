import matplotlib.pyplot as plt
import pandas
import numpy as np

"""
Travling salesman test, using bio inspired algorithm. 

Dataset from: https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html
Best result possible: 699
"""
distances = np.loadtxt("dantzig42_d.txt", dtype = int)

current_state = np.arange(len(distances))

#Function for evaluation the score:
def DistEval(state):
    DistSum = 0
    for i in range(len(state)):
        DistSum += distances[state[-i]][state[i]]
        #print(a)
    return DistSum

#Function for changing state:
def Change(state):
    indexs = np.random.randint(0, len(state), size = 2)
    temp_dex = state[indexs[0]] #To avoid repetition
    state[indexs[0]] = state[indexs[1]]
    state[indexs[1]] = temp_dex
    return state


