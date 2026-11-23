import csv
import os
import matplotlib.pyplot as plt


# ==============================
# CONFIGURATION
# ==============================

CSV_FILE = "analysis/results.csv"
OUTPUT_DIR = "analysis/plots"

ALGORITHMS = ["BFS", "DFS", "Dijkstra", "A*"]

DENSITIES = [10, 20, 25, 30, 35, 40]

os.makedirs(OUTPUT_DIR, exist_ok=True)


# ==============================
# LOAD CSV DATA
# ==============================

def load_results():

    results = []

    with open(CSV_FILE, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            results.append({
                "density": int(row["Density"].replace("%", "")),
                "algorithm": row["Algorithm"],
                "time": float(row["Average Time"]),
                "path": float(row["Average Path Length"]),
                "explored": float(row["Average Explored Nodes"]),
                "success": float(row["Success Rate"])
            })

    return results


# ==============================
# ORGANIZE DATA
# ==============================

def get_values(results, algorithm, metric):

    filtered = [
        row for row in results
        if row["algorithm"] == algorithm
    ]

    filtered.sort(key=lambda row: row["density"])

    return (
        [row["density"] for row in filtered],
        [row[metric] for row in filtered]
    )


# ==============================
# 1. SUCCESS RATE GRAPH
# ==============================

def plot_success_rate(results):

    plt.figure(figsize=(10, 6))

    for algorithm in ALGORITHMS:

        x, y = get_values(results, algorithm, "success")

        plt.plot(
            x, y,
            marker="o",
            linewidth=2,
            label=algorithm
        )

    plt.title("Success Rate vs Obstacle Density", fontsize=15)
    plt.xlabel("Obstacle Density (%)")
    plt.ylabel("Success Rate (%)")

    plt.xticks(DENSITIES)
    plt.ylim(0, 105)

    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()

    plt.savefig(f"{OUTPUT_DIR}/success_rate.png", dpi=300)
    plt.close()


# ==============================
# 2. EXPLORED NODES GRAPH
# ==============================

def plot_explored_nodes(results):

    plt.figure(figsize=(10, 6))

    for algorithm in ALGORITHMS:

        x, y = get_values(results, algorithm, "explored")

        plt.plot(
            x, y,
            marker="o",
            linewidth=2,
            label=algorithm
        )

    plt.title("Explored Nodes vs Obstacle Density", fontsize=15)
    plt.xlabel("Obstacle Density (%)")
    plt.ylabel("Average Explored Nodes")

    plt.xticks(DENSITIES)

    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()

    plt.savefig(f"{OUTPUT_DIR}/explored_nodes.png", dpi=300)
    plt.close()


# ==============================
# 3. EXECUTION TIME GRAPH
# ==============================

def plot_execution_time(results):

    plt.figure(figsize=(10, 6))

    for algorithm in ALGORITHMS:

        x, y = get_values(results, algorithm, "time")

        # Convert seconds to milliseconds
        y = [value * 1000 for value in y]

        plt.plot(
            x, y,
            marker="o",
            linewidth=2,
            label=algorithm
        )

    plt.title("Execution Time vs Obstacle Density", fontsize=15)
    plt.xlabel("Obstacle Density (%)")
    plt.ylabel("Average Execution Time (ms)")

    plt.xticks(DENSITIES)

    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()

    plt.savefig(f"{OUTPUT_DIR}/execution_time.png", dpi=300)
    plt.close()


# ==============================
# 4. AVERAGE PATH LENGTH GRAPH
# ==============================

def plot_average_path_length(results):

    plt.figure(figsize=(10, 6))

    for algorithm in ALGORITHMS:

        x, y = get_values(results, algorithm, "path")

        plt.plot(
            x, y,
            marker="o",
            linewidth=2,
            label=algorithm
        )

    plt.title("Average Path Length vs Obstacle Density", fontsize=15)
    plt.xlabel("Obstacle Density (%)")
    plt.ylabel("Average Path Length (Steps)")

    plt.xticks(DENSITIES)
    plt.ylim(bottom=0)

    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        f"{OUTPUT_DIR}/average_path_length.png",
        dpi=300
    )

    plt.close()


# ==============================
# MAIN
# ==============================

def main():

    print("Loading experimental results...")

    results = load_results()

    print("Generating graphs...")

    plot_success_rate(results)
    plot_explored_nodes(results)
    plot_execution_time(results)
    plot_average_path_length(results)

    print("\n========== VISUALIZATION COMPLETED ==========")

    print("Generated files:")

    print("1. success_rate.png")
    print("2. explored_nodes.png")
    print("3. execution_time.png")
    print("4. average_path_length.png")

    print("\nSaved inside:", OUTPUT_DIR)


if __name__ == "__main__":

    main()