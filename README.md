# Autonomous Robot Path Planning System

A Python-based autonomous navigation simulation that enables a robot to find paths in a 2D grid environment while avoiding obstacles using classical pathfinding algorithms.

The project provides an interactive simulation, an animated robot, a Streamlit dashboard, and performance evaluation tools to analyze and compare different algorithms.

## Project Overview

This project simulates an autonomous robot navigating through a grid-based environment from a starting position to a target destination.

The system implements four classical pathfinding algorithms and evaluates their performance under different obstacle densities.

## Algorithms Implemented

- **Breadth-First Search (BFS):** Finds the shortest path in an unweighted grid.
- **Depth-First Search (DFS):** Explores paths deeply before backtracking.
- **Dijkstra's Algorithm:** Finds the shortest path using cumulative path costs.
- **A* Search:** Uses the Manhattan distance heuristic to guide the search efficiently.

## Main Features

- Interactive 2D grid environment.
- Start and goal position management.
- Manual obstacle placement and removal.
- Path visualization.
- Animated robot movement.
- Multiple pathfinding algorithms.
- Algorithm performance comparison.
- Multiple-map testing.
- Different obstacle density scenarios.
- Performance metrics and graphical analysis.
- Interactive Streamlit dashboard.

## Technologies Used

- Python
- Pygame
- Streamlit
- Matplotlib
- Pandas
- NumPy

## Project Structure

```text
Autonomous-Robot-Path-Planning/
│
├── algorithms/
│   ├── bfs.py
│   ├── dfs.py
│   ├── dijkstra.py
│   ├── astar.py
│   └── algorithm_manager.py
│
├── core/
│   ├── grid.py
│   └── robot.py
│
├── visualization/
│   └── simulator.py
│
├── analysis/
│   ├── multiple_maps_test.py
│   ├── obstacle_density_test.py
│   ├── performance_comparison.py
│   ├── check_high_density.py
│   ├── visualize_results.py
│   ├── results.csv
│   └── plots/
│
├── assets/
│
├── dashboard.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd Autonomous-Robot-Path-Planning
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

On Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Project

### 1. Run the Pygame Simulation

```bash
python -m visualization.simulator
```

### 2. Run the Streamlit Dashboard

```bash
python -m streamlit run dashboard.py
```

The dashboard will open in your default web browser.

## Simulation Controls

| Key / Action | Function |
|---|---|
| Left Mouse Click | Add an obstacle |
| Right Mouse Click | Remove an obstacle |
| 1 | Select BFS |
| 2 | Select DFS |
| 3 | Select Dijkstra |
| 4 | Select A* |
| SPACE | Calculate the path |
| ENTER | Start robot movement |
| R | Reset the simulation |

## Performance Evaluation

The algorithms are evaluated across multiple maps with different obstacle densities:

- 10%
- 20%
- 25%
- 30%
- 35%
- 40%

Each density level is tested using 100 maps.

### Evaluation Metrics

- Execution Time
- Average Path Length
- Average Explored Nodes
- Success Rate

## Generate Performance Results

Run the multiple-map experiment:

```bash
python -m analysis.multiple_maps_test
```

Generate performance graphs:

```bash
python -m analysis.visualize_results
```

Generated graphs are saved in:

```text
analysis/plots/
```

## Project Validation

The project includes tests for:

- Grid functionality.
- Individual pathfinding algorithms.
- Algorithm management.
- Robot movement.
- Path validation.
- Complete system integration.

Run the full system test:

```bash
python test_full_system.py
```

## Project Goal

The main goal is to study and compare classical pathfinding algorithms in autonomous navigation scenarios and evaluate their efficiency, path quality, and reliability under different environmental conditions.

## License

This project is developed for educational and academic purposes.