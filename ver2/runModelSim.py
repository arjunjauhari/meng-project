import simulation
import numpy as np
import visualize
import countCumVotes as ccv

voteHist0 = [[0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [4, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]]]
#visualize.visualizeScat(voteHist0)
#visualize.barPlot(simulation.runModel(voteHist0,6))
voteHist1 = [[0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [4, [0, 1, 2, 3, 4]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]]]
#visualize.visualizeScat(voteHist1)
#visualize.barPlot(simulation.runModel(voteHist1,6))
voteHist2 = [[0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [4, [0, 1, 2, 3, 4]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]]]
voteHist3 = [[0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [4, [0, 1, 2, 3, 4]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]]]

#voteHist4 = [[0, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [8, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [8, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [9, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [12, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], [12, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [12, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [13, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]]
#visualize.visualizeScat(voteHist4)
#visualize.barPlot(simulation.runModel(voteHist4,len(voteHist4[-1][-1])))
#voteHist5 = [[0, [0]], [0, [0]], [0, [0]], [0, [0]], [0, [0]], [0, [0]], [0, [0]], [0, [0]], [0, [0]], [0, [0]], [0, [0]], [0, [0]], [0, [0]], [0, [0]], [0, [0]], [0, [0, 1]], [0, [0, 1]], [0, [0, 1]], [0, [0, 1]], [0, [0, 1]], [0, [0, 1]], [0, [0, 1]], [0, [0, 1, 2]], [0, [0, 1, 2]], [0, [0, 1, 2]], [0, [0, 1, 2]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [1, [0, 1]], [1, [0, 1]], [1, [0, 1, 2]], [1, [0, 1, 2, 3]], [2, [0, 1, 2]], [2, [0, 1, 2]], [2, [0, 1, 2]], [2, [0, 1, 2]], [2, [0, 1, 2]], [2, [0, 1, 2]], [2, [0, 1, 2]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [3, [0, 1, 2, 3]]] # [[0, [0, 1, 2]], [0, [0, 1, 2]], [0, [0, 1, 2]], [0, [0, 1, 2]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [1, [0, 1, 2]], [1, [0, 1, 2]], [1, [0, 1, 2]], [1, [0, 1, 2]], [1, [0, 1, 2]], [1, [0, 1, 2]], [1, [0, 1, 2]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [2, [0, 1, 2]], [2, [0, 1, 2]], [2, [0, 1, 2]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]]]
#visualize.visualizeScat(voteHist5)
#visualize.barPlot(simulation.runModel(voteHist5,len(voteHist5[-1][-1])))

print "6"
voteHist6 = [[0, [0, 1, 2]], [0, [0, 1, 2]], [0, [0, 1, 2]], [0, [0, 1, 2]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [1, [0, 1, 2]], [1, [0, 1, 2]], [1, [0, 1, 2]], [1, [0, 1, 2]], [1, [0, 1, 2]], [1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [2, [0, 1, 2]], [2, [0, 1, 2]], [2, [0, 1, 2]], [2, [0, 1, 2]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [4, [0, 1, 2, 3, 4]], [4, [0, 1, 2, 3, 4]], [4, [0, 1, 2, 3, 4]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [6, [0, 1, 2, 3, 4, 5, 6]], [6, [0, 1, 2, 3, 4, 5, 6]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [8, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [8, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [8, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [8, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [8, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [8, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [8, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]], [8, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [8, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [8, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [8, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [9, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [9, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [9, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [9, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [9, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [9, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [11, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [11, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], [11, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [11, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [11, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [11, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [12, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], [12, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], [12, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [12, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [12, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [12, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [13, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [13, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], [13, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]], [13, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]], [13, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [13, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [13, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [13, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [14, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]], [14, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [14, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [14, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [14, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [15, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]], [15, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [15, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [15, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [15, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [16, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]], [16, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]], [16, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]], [16, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [16, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [16, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [16, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [17, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [18, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [18, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [18, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [19, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]], [19, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]], [19, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [19, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [19, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [19, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [19, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [20, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [20, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [20, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [20, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [20, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [21, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [21, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]], [21, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]]]
visualize.visualizeScat(voteHist6)
visualize.barPlot(simulation.runModel(voteHist6,len(voteHist6[-1][-1])))

print "7"
voteHist7 = [[0, [0, 1, 2]], [0, [0, 1, 2]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [1, [0, 1, 2]], [1, [0, 1, 2]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [4, [0, 1, 2, 3, 4]], [4, [0, 1, 2, 3, 4]], [4, [0, 1, 2, 3, 4]], [4, [0, 1, 2, 3, 4]], [4, [0, 1, 2, 3, 4]], [4, [0, 1, 2, 3, 4]], [4, [0, 1, 2, 3, 4]]]
visualize.visualizeScat(voteHist7)
visualize.barPlot(simulation.runModel(voteHist7,len(voteHist7[-1][-1])))

# with Fake answer implementation
print "8"
#voteHist8 = [[1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4, 5]], [1, [0, 1, 2, 3, 4, 5]], [1, [0, 1, 2, 3, 4, 5]], [1, [0, 1, 2, 3, 4, 5]], [1, [0, 1, 2, 3, 4, 5]], [1, [0, 1, 2, 3, 4, 5]], [1, [0, 1, 2, 3, 4, 5]], [0, [0, 1]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [0, [0, 2]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [4, [0, 1, 2, 3, 4]], [4, [0, 1, 2, 3, 4, 5]], [4, [0, 1, 2, 3, 4, 5]], [4, [0, 1, 2, 3, 4, 5]], [4, [0, 1, 2, 3, 4, 5]], [4, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]]]#[[1, [0, 1, 2]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2]], [2, [0, 1, 2]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4, 5]], [0, [0, 3]], [0, [0, 3]], [4, [0, 1, 2, 3, 4]], [4, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]]]#[[1, [0, 1, 2]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [2, [0, 1, 2]], [2, [0, 1, 2]], [2, [0, 1, 2]], [2, [0, 1, 2]], [2, [0, 1, 2]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5, 6]], [2, [0, 1, 2, 3, 4, 5, 6, 7]], [2, [0, 1, 2, 3, 4, 5, 6, 7]], [2, [0, 1, 2, 3, 4, 5, 6, 7]], [2, [0, 1, 2, 3, 4, 5, 6, 7]], [2, [0, 1, 2, 3, 4, 5, 6, 7]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [0, [0, 3]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [8, [0, 1, 2, 3, 4, 5, 6, 7, 8]]]
#voteHist8 = [[1, [0, 1, 2]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2]], [2, [0, 1, 2]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4, 5]], [0, [0, 3]], [0, [0, 3]], [4, [0, 1, 2, 3, 4]], [4, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]]]
#voteHist8 = [[1, [0, 1, 2]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [1, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [2, [0, 1, 2]], [2, [0, 1, 2]], [2, [0, 1, 2]], [2, [0, 1, 2]], [2, [0, 1, 2]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5, 6]], [2, [0, 1, 2, 3, 4, 5, 6, 7]], [2, [0, 1, 2, 3, 4, 5, 6, 7]], [2, [0, 1, 2, 3, 4, 5, 6, 7]], [2, [0, 1, 2, 3, 4, 5, 6, 7]], [2, [0, 1, 2, 3, 4, 5, 6, 7]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [2, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [0, [0, 3]], [4, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [5, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [6, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [7, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [8, [0, 1, 2, 3, 4, 5, 6, 7, 8]]]

# time matters example
# cumsum -> [ 4  6  3 44 16  3 11]
voteHist8 = [[1, [0, 1, 2, 3, 4, 5]], [1, [0, 1, 2, 3, 4, 5]], [1, [0, 1, 2, 3, 4, 5]], [1, [0, 1, 2, 3, 4, 5, 6]], [1, [0, 1, 2, 3, 4, 5, 6]], [1, [0, 1, 2, 3, 4, 5, 6]], [0, [0, 1]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5, 6]], [0, [0, 2]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [3, [0, 1, 2, 3, 4, 5, 6]], [0, [0, 3]], [4, [0, 1, 2, 3, 4, 5]], [4, [0, 1, 2, 3, 4, 5]], [4, [0, 1, 2, 3, 4, 5]], [4, [0, 1, 2, 3, 4, 5]], [4, [0, 1, 2, 3, 4, 5]], [4, [0, 1, 2, 3, 4, 5, 6]], [4, [0, 1, 2, 3, 4, 5, 6]], [4, [0, 1, 2, 3, 4, 5, 6]], [4, [0, 1, 2, 3, 4, 5, 6]], [4, [0, 1, 2, 3, 4, 5, 6]], [4, [0, 1, 2, 3, 4, 5, 6]], [4, [0, 1, 2, 3, 4, 5, 6]], [4, [0, 1, 2, 3, 4, 5, 6]], [4, [0, 1, 2, 3, 4, 5, 6]], [4, [0, 1, 2, 3, 4, 5, 6]], [4, [0, 1, 2, 3, 4, 5, 6]], [0, [0, 4]], [5, [0, 1, 2, 3, 4, 5, 6]], [5, [0, 1, 2, 3, 4, 5, 6]], [5, [0, 1, 2, 3, 4, 5, 6]], [6, [0, 1, 2, 3, 4, 5, 6]], [6, [0, 1, 2, 3, 4, 5, 6]], [6, [0, 1, 2, 3, 4, 5, 6]], [6, [0, 1, 2, 3, 4, 5, 6]], [6, [0, 1, 2, 3, 4, 5, 6]], [6, [0, 1, 2, 3, 4, 5, 6]], [6, [0, 1, 2, 3, 4, 5, 6]], [6, [0, 1, 2, 3, 4, 5, 6]], [6, [0, 1, 2, 3, 4, 5, 6]], [6, [0, 1, 2, 3, 4, 5, 6]], [6, [0, 1, 2, 3, 4, 5, 6]]]
print ccv.countCumVotes(voteHist8)
visualize.visualizeScat(voteHist8)
visualize.barPlot(simulation.runModel(voteHist8,voteHist8[-1][-1][-1]+1))

#print simulation.runModel(voteHist0,6)
#print simulation.runModel(voteHist1,6)
#print simulation.runModel(voteHist2,6)
#print simulation.runModel(voteHist3,6)