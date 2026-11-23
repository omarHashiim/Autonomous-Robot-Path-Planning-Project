from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.dijkstra import dijkstra
from algorithms.astar import astar


class AlgorithmManager:

    def __init__(self):

        self.algorithms = {
            "BFS": bfs,
            "DFS": dfs,
            "Dijkstra": dijkstra,
            "A*": astar
        }

    def get_algorithm_names(self):

        return list(self.algorithms.keys())

    def run_algorithm(self, algorithm_name, grid):

        if algorithm_name not in self.algorithms:
            raise ValueError("Unknown algorithm: " + algorithm_name)

        algorithm = self.algorithms[algorithm_name]

        return algorithm(grid)