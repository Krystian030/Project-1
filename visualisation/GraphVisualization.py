import networkx as nx
import random
import time
import tkinter as Tk
import copy
from matplotlib import pyplot as plt, animation
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from algorithms.Bfs import Bfs
from algorithms.Dfs import Dfs
from algorithms.dijkstra import Dijkstra
from algorithms.RandomAlgorithm import RandomAlgorithm
from algorithms.RandomAlgorithmWithRepeats import RandomAlgorithmWithRepeats
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class GraphVisualization:
	def __init__(self):
		pass
	@staticmethod
	def visualizationGraph(g,algNumber):
		if algNumber == 1:
			alg = Bfs(g)  # Wybór algorytmu z którego będziemy korzystać
		elif algNumber == 2:
			alg = Dfs(g)
		else:
			alg = Dijkstra(g)
		g.data_init()
		fig = plt.figure()
		stateList = []  # Mapa stanów kolorowań naszego grafu
		# aktualny stan używany do zapisu
		stateNumber = 0
		root = Tk.Tk()
		root.wm_title("Graph n: " + str(g.n))

		# Quit when the window is done
		root.wm_protocol('WM_DELETE_WINDOW', root.quit)
		canvas = FigureCanvasTkAgg(fig, master=root)

		def drawCanvas():
			plt.clf()
			g.set_color()
			fig.clear()
			legend_elements = [Line2D([0], [0], marker='o', color='w', label='Actual node',markerfacecolor='r', markersize=10),
							   Line2D([0], [0], marker='o', color='w', label='Every neighbour checked',markerfacecolor='b', markersize=10),
							   Line2D([0], [0], marker='o', color='w', label='Has neighbours to check',markerfacecolor='yellow', markersize=10),
							   Line2D([0], [0], linewidth=0.1, color='black', label = 'Possible route'),
							   Line2D([0], [0], linewidth=1, color='black', label = 'Chosen route')]
			if isinstance(alg, Dijkstra):
				legend_elements.insert(3,Line2D([0], [0], marker='o', color='w', label='Checking cost to this node',markerfacecolor='orange',
											  markersize=10))
			plt.legend(handles= legend_elements, loc= 0)
			nx.draw(g.graph, g.position, node_size=g.size_map, node_color=g.color_map,
					font_size=7, with_labels=True, labels=g.labels, width=list(g.width.values()))
			nx.draw_networkx_edge_labels(g.graph, g.position, edge_labels=g.edgeLabels)
			plt.axis('off')


			canvas.draw()


		drawCanvas()
		canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
		stateList.append(copy.deepcopy(g))

		def nextGraph():
			nonlocal stateNumber,g
			if stateNumber == len(stateList) - 1:
				if g.actual_node < g.n and g.actual_node != -1:
					tmp = copy.deepcopy(g)  # tworzenie kopii stanu, żeby nie edytować dwóch elementów na raz
					if not g.actual_node == -1:
						alg.func(tmp)
					stateList.append(copy.deepcopy(tmp))  # dopisywanie kopii do tabeli stanów i przypisywanie spowrotem
					g = tmp
					stateNumber += 1
			else:
				stateNumber += 1
				g =stateList[stateNumber]
			drawCanvas()

		def prevGraph():
			nonlocal stateNumber,g
			if stateNumber > 0:
				stateNumber -= 1
				g = stateList[stateNumber]
			drawCanvas()

		button_next = Tk.Button(root, text="next", command=nextGraph)
		button_next.pack()
		button_prev = Tk.Button(root, text="prev", command=prevGraph)
		button_prev.pack()
		Tk.mainloop()