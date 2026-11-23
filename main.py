import runpy

def main():
    print("Starting Autonomous Robot Path Planning System...")
    runpy.run_module("visualization.simulator", run_name="__main__")


if __name__ == "__main__":
    main()