import timeit

from graph.Graph import Graph
from algorithms.Bfs import Bfs
from algorithms.Dfs import Dfs
from algorithms.RandomAlgorithm import RandomAlgorithm
from algorithms.RandomAlgorithmWithRepeats import RandomAlgorithmWithRepeats
class Stats:
	def __init__(self):
		self.valuesToCheck = [10,20,30]
		self.iterationNumber = []
	def createStats(self):
		avg1=[]
		avg2=[]
		for i in range(0,20):
			gr1 = Graph()
			gr1.randomGraph(20,1)
			gr1.data_init()
			iteration = 0
			alg = Bfs(gr1)
			start = timeit.default_timer()
			while gr1.actual_node != -1:
				iteration+=1
				alg.func(gr1)
			stop = timeit.default_timer()
			avg1.append(stop - start)
			gr1.dataReset()
			iteration = 0
			alg = RandomAlgorithmWithRepeats(gr1)
			start = timeit.default_timer()
			while gr1.actual_node != -1:
				iteration+=1
				alg.func(gr1)
			stop = timeit.default_timer()
			avg2.append(stop - start)
		print(avg1)
		print(avg2)
		print(sum(avg1)/len(avg1))
		print(sum(avg2)/len(avg2))