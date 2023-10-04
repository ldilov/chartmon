# ChartMon

## Description

ChartMon is a Python application designed to visualize telemetry data from PresentMon in a user-friendly manner. It uses Plotly for plotting and supports various types of plots including FPS, Frametime, and CPU vs GPU active time.

## Features

- Load CSV files containing PresentMon data
- Generate interactive plots
- Command-line and GUI support for file selection

### Types of Charts

1. **FPS (Frames Per Second)**: This chart shows the number of frames rendered per second. A consistent and high FPS is desired for smooth gameplay. Low or fluctuating FPS can indicate a bottleneck in the system.

2. **Frametime**: This chart shows the time taken to render each frame in milliseconds. Lower frametime is better, and spikes in frametime can indicate stuttering or other performance issues.

3. **CPU vs GPU Active Time**: This chart shows the percentage of time the CPU and GPU are active. It can help identify which component is the bottleneck. For example, if the CPU is active 90% of the time and the GPU is active only 10%, it's likely that the CPU is the bottleneck.

4. **Performance per Watt **: Analyzing performance per watt for both cpu and gpu if available

## Why These Charts are Useful

These charts are particularly useful for identifying bottlenecks in a system's performance. By analyzing these charts, you can determine whether your CPU, GPU, or some other component is the limiting factor in your setup. This can guide you on what to upgrade in your system for better performance.


## Prerequisites

- Python 3.x
- Pip (Python package installer)

## Installation

1. Clone the repository
    ```bash
    git clone https://github.com/yourusername/ChartMon.git
    ```

2. Navigate to the project directory
    ```bash
    cd ChartMon
    ```

3. Install required packages
    ```bash
    pip install -r requirements.txt
    ```

## Build Executable

To build an executable version of the application, follow these steps:

1. Make sure you are in the project directory.

2. Run the setup script to build the executable.
    ```bash
    python setup.py build
    ```

3. After the build is complete, you will find the executable in the `build` directory.

## Usage

You can run the application in two ways:

1. **Command Line:**
    ```bash
    python main.py -f /path/to/csv/file
    ```

2. **GUI:**
    Simply run the application and a file dialog will appear for you to select the CSV file.

 ![Sample](https://raw.githubusercontent.com/ldilov/chartmon/main/sample.png)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
