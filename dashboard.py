import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import random
import os
import time

from core.grid import Grid
from algorithms.algorithm_manager import AlgorithmManager


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Autonomous Navigation Control Center",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>
.stApp {
    background-color: #080D19;
    color: #E5E7EB;
}

[data-testid="stSidebar"] {
    background-color: #0D1526;
    border-right: 1px solid #1E293B;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1500px;
}

h1, h2, h3 {
    color: #F1F5F9 !important;
}

p, label {
    color: #A7B4C8;
}

.metric-card {
    background: linear-gradient(135deg, #111D32, #101827);
    border: 1px solid #243750;
    border-radius: 12px;
    padding: 20px;
    min-height: 125px;
}

.metric-title {
    color: #94A3B8;
    font-size: 13px;
    font-weight: 600;
    text-transform: uppercase;
}

.metric-value {
    color: #38BDF8;
    font-size: 30px;
    font-weight: 700;
    margin-top: 8px;
}

.metric-subtitle {
    color: #64748B;
    font-size: 12px;
}

.section-card {
    background-color: #111827;
    border: 1px solid #243750;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 15px;
}

.status-online {
    color: #22C55E;
    font-weight: bold;
}

.stButton > button {
    background: linear-gradient(90deg, #0284C7, #2563EB);
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    min-height: 42px;
    width: 100%;
}

.stButton > button:hover {
    border: 1px solid #38BDF8;
    color: white;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# SESSION STATE
# ==========================================

if "results" not in st.session_state:
    st.session_state.results = {}

if "comparison_results" not in st.session_state:
    st.session_state.comparison_results = {}

if "grid" not in st.session_state:
    st.session_state.grid = None


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("# 🤖 AUTONOMOUS")
    st.markdown("### NAVIGATION SYSTEM")
    st.markdown("---")

    page = st.radio(
        "NAVIGATION",
        [
            "Overview",
            "Path Planning",
            "Algorithm Comparison",
            "Algorithms",
            "Performance Analytics",
            "System Information"
        ]
    )

    st.markdown("---")
    st.markdown("### SYSTEM STATUS")

    st.markdown(
        '<p class="status-online">● SYSTEM ONLINE</p>',
        unsafe_allow_html=True
    )

    st.caption("Autonomous Robot Path Planning")
    st.caption("Version 2.1.0")


# ==========================================
# HEADER
# ==========================================

st.markdown(
    "<h1>Autonomous Navigation Control Center</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "Intelligent Path Planning | Algorithm Analysis | Robot Simulation"
)

st.markdown("---")


# ==========================================
# HELPER FUNCTIONS
# ==========================================

def create_grid(rows, cols, density, seed):

    grid = Grid(rows, cols)

    rng = random.Random(seed)

    positions = [
        (r, c)
        for r in range(rows)
        for c in range(cols)
        if (r, c) not in (grid.start, grid.goal)
    ]

    obstacle_count = int(len(positions) * density)

    for obstacle in rng.sample(positions, obstacle_count):
        grid.add_obstacle(obstacle)

    return grid


# ==========================================
# GRID VISUALIZATION
# ==========================================

def draw_grid(grid, path=None, robot_position=None):

    fig, ax = plt.subplots(figsize=(12, 6))

    fig.patch.set_facecolor("#111827")
    ax.set_facecolor("#111827")

    path_set = set(path) if path else set()

    for r in range(grid.rows):

        for c in range(grid.cols):

            position = (r, c)

            color = "#1E293B"

            if position in grid.obstacles:
                color = "#020617"

            if position in path_set:
                color = "#0EA5E9"

            if position == grid.start:
                color = "#22C55E"

            if position == grid.goal:
                color = "#EF4444"

            rect = patches.Rectangle(
                (c, grid.rows - 1 - r),
                1,
                1,
                facecolor=color,
                edgecolor="#334155",
                linewidth=0.5
            )

            ax.add_patch(rect)

    # Draw moving robot

    if robot_position is not None:

        robot_row, robot_col = robot_position

        robot = patches.Circle(
            (
                robot_col + 0.5,
                grid.rows - 1 - robot_row + 0.5
            ),
            0.32,
            color="#A855F7",
            edgecolor="white",
            linewidth=1.2,
            zorder=10
        )

        ax.add_patch(robot)

    ax.set_xlim(0, grid.cols)
    ax.set_ylim(0, grid.rows)

    ax.set_xticks([])
    ax.set_yticks([])

    for spine in ax.spines.values():
        spine.set_visible(False)

    plt.tight_layout()

    return fig


# ==========================================
# METRIC CARD
# ==========================================

def metric_card(title, value, subtitle):

    html = f"""
    <div class="metric-card">

        <div class="metric-title">
            {title}
        </div>

        <div class="metric-value">
            {value}
        </div>

        <div class="metric-subtitle">
            {subtitle}
        </div>

    </div>
    """

    st.html(html)


# ==========================================
# ALGORITHM COMPARISON
# ==========================================

def run_comparison(grid):

    manager = AlgorithmManager()

    algorithm_names = [
        "BFS",
        "DFS",
        "Dijkstra",
        "A*"
    ]

    comparison = {}

    for name in algorithm_names:

        result = manager.run_algorithm(name, grid)

        comparison[name] = {

            "Path Length": result["path_length"],

            "Explored Nodes": result["explored_nodes"],

            "Execution Time": result["execution_time"],

            "Success": bool(result["path"])
        }

    return comparison


# ==========================================
# CHART STYLE
# ==========================================

def style_chart(fig, ax):

    fig.patch.set_facecolor("#111827")

    ax.set_facecolor("#111827")

    ax.tick_params(colors="white")

    ax.xaxis.label.set_color("white")
    ax.yaxis.label.set_color("white")

    ax.title.set_color("white")

    ax.grid(alpha=0.2)

    legend = ax.get_legend()

    if legend:

        for item in legend.get_texts():
            item.set_color("white")


# ==========================================
# ROBOT ANIMATION
# ==========================================

def animate_robot(grid, path, speed):

    if not path:

        st.warning(
            "No valid path is available for the robot."
        )

        return

    animation_area = st.empty()

    progress_bar = st.progress(0)

    status_text = st.empty()

    total_steps = len(path)

    for step, position in enumerate(path):

        fig = draw_grid(
            grid,
            path=path[:step + 1],
            robot_position=position
        )

        animation_area.pyplot(fig)

        plt.close(fig)

        progress = int(
            ((step + 1) / total_steps) * 100
        )

        progress_bar.progress(progress)

        status_text.markdown(
            f"**Robot Position:** `{position}`  |  "
            f"**Step:** {step + 1}/{total_steps}  |  "
            f"**Progress:** {progress}%"
        )

        time.sleep(speed)

    status_text.success(
        "MISSION COMPLETED — Robot successfully reached the goal!"
    )


# ==========================================
# OVERVIEW PAGE
# ==========================================

if page == "Overview":

    st.subheader("System Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card(
            "Algorithms",
            "04",
            "Pathfinding algorithms"
        )

    with col2:
        metric_card(
            "Grid Size",
            "20 × 30",
            "Navigation environment"
        )

    with col3:
        metric_card(
            "Test Maps",
            "600",
            "100 maps per density level"
        )

    with col4:
        metric_card(
            "Obstacle Levels",
            "06",
            "10% to 40%"
        )

    st.markdown("### System Architecture")

    c1, c2 = st.columns(2)

    with c1:

        st.markdown("""
        <div class="section-card">

        <h3>Pathfinding Algorithms</h3>

        <p>01 — Breadth-First Search (BFS)</p>

        <p>02 — Depth-First Search (DFS)</p>

        <p>03 — Dijkstra's Algorithm</p>

        <p>04 — A* Search Algorithm</p>

        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown("""
        <div class="section-card">

        <h3>Core Technologies</h3>

        <p>Python — Core Development</p>

        <p>Pygame — Robot Simulation</p>

        <p>Streamlit — Interactive Dashboard</p>

        <p>Matplotlib — Data Visualization</p>

        </div>
        """, unsafe_allow_html=True)

    st.info(
        "Navigate through the sidebar to explore the simulation "
        "and evaluate the pathfinding algorithms."
    )


# ==========================================
# PATH PLANNING PAGE
# ==========================================

elif page == "Path Planning":

    st.subheader("Interactive Path Planning")

    col1, col2, col3 = st.columns(3)

    with col1:

        rows = st.number_input(
            "Grid Rows",
            min_value=5,
            max_value=40,
            value=20
        )

    with col2:

        cols = st.number_input(
            "Grid Columns",
            min_value=5,
            max_value=50,
            value=30
        )

    with col3:

        density = st.slider(
            "Obstacle Density",
            0.0,
            0.40,
            0.20,
            step=0.05
        )

    seed = st.number_input(
        "Map Seed",
        min_value=1,
        value=42
    )

    algorithm_name = st.selectbox(
        "Select Algorithm",
        ["BFS", "DFS", "Dijkstra", "A*"]
    )

    animation_speed = st.slider(
        "Robot Animation Speed (seconds per step)",
        min_value=0.02,
        max_value=0.50,
        value=0.12,
        step=0.02,
        help="Controls the delay between consecutive robot positions."
    )

    # Generate map

    if st.button("GENERATE MAP"):

        grid = create_grid(
            int(rows),
            int(cols),
            density,
            int(seed)
        )

        st.session_state.grid = grid

        st.session_state.results = {}

        st.session_state.comparison_results = {}

        st.success(
            "Navigation map generated successfully!"
        )

    # Display generated map

    if st.session_state.grid is not None:

        grid = st.session_state.grid

        # Run selected algorithm

        if st.button("RUN PATHFINDING"):

            manager = AlgorithmManager()

            with st.spinner(
                "Calculating navigation path..."
            ):

                result = manager.run_algorithm(
                    algorithm_name,
                    grid
                )

            st.session_state.results[algorithm_name] = result

            st.success(
                "Pathfinding completed!"
            )

        result = st.session_state.results.get(
            algorithm_name
        )

        path = result["path"] if result else None

        fig = draw_grid(grid, path)

        st.pyplot(fig)

        plt.close(fig)

        # Display metrics

        if result:

            a, b, c = st.columns(3)

            with a:

                metric_card(
                    "Path Length",
                    result["path_length"],
                    "Number of path steps"
                )

            with b:

                metric_card(
                    "Explored Nodes",
                    result["explored_nodes"],
                    "Nodes explored during search"
                )

            with c:

                metric_card(
                    "Execution Time",
                    f"{result['execution_time']:.6f}",
                    "Seconds"
                )

            # Robot simulation

            st.markdown("---")

            st.markdown(
                "### Autonomous Robot Simulation"
            )

            st.caption(
                "The purple robot moves along the calculated path "
                "from START to GOAL."
            )

            if path:

                if st.button(
                    "START ROBOT ANIMATION",
                    key="start_robot_animation"
                ):

                    animate_robot(
                        grid,
                        path,
                        animation_speed
                    )

            else:

                st.warning(
                    "No valid path found. "
                    "The robot cannot reach the goal."
                )

    else:

        st.info(
            "Generate a map to start path planning."
        )


# ==========================================
# ALGORITHM COMPARISON PAGE
# ==========================================

elif page == "Algorithm Comparison":

    st.subheader(
        "Algorithm Performance Comparison"
    )

    st.markdown(
        "Compare all four pathfinding algorithms using the same "
        "navigation map and obstacle configuration."
    )

    if st.session_state.grid is None:

        st.warning(
            "Please generate a map first from the Path Planning page."
        )

    else:

        grid = st.session_state.grid

        st.markdown(
            "### Current Navigation Environment"
        )

        fig = draw_grid(grid)

        st.pyplot(fig)

        plt.close(fig)

        st.markdown("---")

        if st.button(
            "RUN ALL ALGORITHMS",
            key="run_all_algorithms"
        ):

            with st.spinner(
                "Running all algorithms..."
            ):

                comparison = run_comparison(grid)

            st.session_state.comparison_results = comparison

            st.success(
                "All four algorithms completed."
            )

        comparison = st.session_state.comparison_results

        if comparison:

            st.markdown(
                "### Comparison Results"
            )

            df_comparison = pd.DataFrame.from_dict(
                comparison,
                orient="index"
            )

            df_comparison.index.name = "Algorithm"

            df_display = df_comparison.copy()

            df_display["Execution Time"] = df_display[
                "Execution Time"
            ].map(
                lambda x: f"{x:.8f} s"
            )

            df_display["Success"] = df_display[
                "Success"
            ].map(
                lambda x: "SUCCESS" if x else "NO PATH"
            )

            st.dataframe(
                df_display,
                use_container_width=True
            )

            successful = [
                name
                for name in comparison
                if comparison[name]["Success"]
            ]

            col1, col2, col3 = st.columns(3)

            fastest = min(
                comparison,
                key=lambda name: comparison[name]["Execution Time"]
            )

            least_explored = min(
                comparison,
                key=lambda name: comparison[name]["Explored Nodes"]
            )

            shortest = (
                min(
                    successful,
                    key=lambda name: comparison[name]["Path Length"]
                )
                if successful else None
            )

            with col1:

                metric_card(
                    "Fastest Algorithm",
                    fastest,
                    "Lowest measured execution time"
                )

            with col2:

                metric_card(
                    "Least Explored",
                    least_explored,
                    "Fewest explored nodes"
                )

            with col3:

                metric_card(
                    "Shortest Path",
                    shortest if shortest else "N/A",
                    "Shortest successful path"
                )

            names = list(comparison.keys())

            # Execution time chart

            st.markdown(
                "### Execution Time Comparison"
            )

            fig, ax = plt.subplots(figsize=(11, 4))

            times_ms = [
                comparison[name]["Execution Time"] * 1000
                for name in names
            ]

            ax.bar(names, times_ms)

            ax.set_ylabel("Execution Time (ms)")

            ax.set_title(
                "Execution Time by Algorithm"
            )

            style_chart(fig, ax)

            st.pyplot(fig)

            plt.close(fig)

            # Explored nodes chart

            st.markdown(
                "### Explored Nodes Comparison"
            )

            fig, ax = plt.subplots(figsize=(11, 4))

            explored = [
                comparison[name]["Explored Nodes"]
                for name in names
            ]

            ax.bar(names, explored)

            ax.set_ylabel("Number of Nodes")

            ax.set_title(
                "Explored Nodes by Algorithm"
            )

            style_chart(fig, ax)

            st.pyplot(fig)

            plt.close(fig)

            # Path length chart

            st.markdown(
                "### Path Length Comparison"
            )

            fig, ax = plt.subplots(figsize=(11, 4))

            path_lengths = [
                comparison[name]["Path Length"]
                if comparison[name]["Success"] else 0
                for name in names
            ]

            ax.bar(names, path_lengths)

            ax.set_ylabel("Path Length")

            ax.set_title(
                "Path Length by Algorithm"
            )

            style_chart(fig, ax)

            st.pyplot(fig)

            plt.close(fig)

            st.markdown("---")

            st.markdown(
                "### Algorithm Insights"
            )

            st.info(
                "BFS and Dijkstra guarantee shortest paths on this "
                "unweighted grid. A* uses a heuristic to guide its "
                "search. DFS does not guarantee the shortest path. "
                "Execution-time differences on a single map can be "
                "affected by measurement noise."
            )

            if shortest:

                st.success(
                    f"Shortest successful path found by: {shortest}"
                )

            else:

                st.warning(
                    "No algorithm found a path on this map."
                )

        else:

            st.info(
                "Click RUN ALL ALGORITHMS to start the comparison."
            )


# ==========================================
# ALGORITHMS PAGE
# ==========================================

elif page == "Algorithms":

    st.subheader(
        "Pathfinding Algorithms"
    )

    manager = AlgorithmManager()

    descriptions = {

        "BFS": (
            "Explores the grid level by level and guarantees a shortest "
            "path on an unweighted grid."
        ),

        "DFS": (
            "Explores one direction deeply before backtracking. "
            "It does not guarantee the shortest path."
        ),

        "Dijkstra": (
            "Finds shortest paths using cumulative movement costs."
        ),

        "A*": (
            "Combines path cost and Manhattan heuristic to guide "
            "the search toward the goal."
        )
    }

    for name in manager.get_algorithm_names():

        with st.expander(name):

            st.write(
                descriptions[name]
            )


# ==========================================
# PERFORMANCE ANALYTICS
# ==========================================

elif page == "Performance Analytics":

    st.subheader(
        "Performance Analytics"
    )

    csv_path = os.path.join(
        "analysis",
        "results.csv"
    )

    if os.path.exists(csv_path):

        df = pd.read_csv(csv_path)

        st.markdown(
            "### Experimental Results"
        )

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        metric = st.selectbox(
            "Select Performance Metric",
            [
                "Average Time",
                "Average Path Length",
                "Average Explored Nodes",
                "Success Rate"
            ]
        )

        fig, ax = plt.subplots(
            figsize=(12, 5)
        )

        for algorithm in df["Algorithm"].unique():

            subset = df[
                df["Algorithm"] == algorithm
            ]

            ax.plot(
                subset["Density"],
                subset[metric],
                marker="o",
                linewidth=2,
                label=algorithm
            )

        ax.set_title(metric)

        ax.set_xlabel(
            "Obstacle Density"
        )

        ax.set_ylabel(metric)

        ax.legend()

        style_chart(fig, ax)

        st.pyplot(fig)

        plt.close(fig)

    else:

        st.warning(
            "Performance results were not found. "
            "Run the multiple maps experiment first."
        )


# ==========================================
# SYSTEM INFORMATION
# ==========================================

elif page == "System Information":

    st.subheader(
        "System Information"
    )

    st.markdown("""
    ### Autonomous Robot Path Planning System

    **Project Type:** Algorithm Design & Autonomous Navigation

    **Programming Language:** Python

    **Algorithms:**
    - BFS
    - DFS
    - Dijkstra
    - A*

    **Visualization:**
    - Streamlit Dashboard
    - Pygame Simulation
    - Matplotlib Analytics

    **Environment:**

    A two-dimensional grid containing a starting point,
    destination point, and obstacles.

    **Objective:**

    Evaluate and compare classical pathfinding algorithms
    under different environmental conditions.
    """)

    st.success(
        "All project modules are integrated with the dashboard."
    )