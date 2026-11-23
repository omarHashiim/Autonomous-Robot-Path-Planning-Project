import time
from statistics import mean

from algorithms.algorithm_manager import AlgorithmManager


class PerformanceComparison:

    def __init__(self, repetitions=10):
        self.manager = AlgorithmManager()
        self.repetitions = repetitions

    def compare(self, grid):

        results = {}

        algorithms = self.manager.get_algorithm_names()

        for algorithm_name in algorithms:

            execution_times = []
            path_lengths = []
            explored_nodes = []
            successful_runs = 0

            for _ in range(self.repetitions):

                start_time = time.perf_counter()

                result = self.manager.run_algorithm(
                    algorithm_name,
                    grid
                )

                end_time = time.perf_counter()

                execution_times.append(
                    end_time - start_time
                )

                path_lengths.append(result["path_length"])

                explored_nodes.append(
                    result["explored_nodes"]
                )

                if result["path"]:
                    successful_runs += 1

            results[algorithm_name] = {
                "avg_execution_time": mean(execution_times),
                "avg_path_length": mean(path_lengths),
                "avg_explored_nodes": mean(explored_nodes),
                "success_rate": (
                    successful_runs / self.repetitions
                ) * 100
            }

        return results

    def display_results(self, results):

        print("\n========== ALGORITHM PERFORMANCE COMPARISON ==========\n")

        print(
            f"{'Algorithm':<12}"
            f"{'Time (s)':<18}"
            f"{'Path Length':<16}"
            f"{'Explored':<14}"
            f"{'Success %':<12}"
        )

        print("-" * 72)

        for name, data in results.items():

            print(
                f"{name:<12}"
                f"{data['avg_execution_time']:<18.8f}"
                f"{data['avg_path_length']:<16.2f}"
                f"{data['avg_explored_nodes']:<14.2f}"
                f"{data['success_rate']:<12.1f}"
            )