from scipy import optimize
import simulation
import numpy as np

np.random.seed(1)
voteHist = [[0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [4, [0, 1, 2, 3, 4]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]]]
voteHist2 = [[2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [9, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [9, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [9, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [9, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [9, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [9, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [9, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [9, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [9, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]]


print "Error:"
print "In1: ",optimize.check_grad(simulation.objFunc2,simulation.objFunc2Grad,np.random.randn(6),voteHist)
print "In2: ",optimize.check_grad(simulation.objFunc2,simulation.objFunc2Grad,np.random.randn(10),voteHist2)
