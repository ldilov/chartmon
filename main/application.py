import argparse
import tkinter as tk
from tkinter import filedialog
import plotly.graph_objects as go
import numpy as np

from data.data_loader import DataLoader
from processing.data_processor import DataProcessor
from plotting.plot_builder import PlotBuilder


class Application:
    def __init__(self):
        self.data_loader = DataLoader()
        self.plot_builder = PlotBuilder()

    def run(self):
        parser = argparse.ArgumentParser(description='Display PresentMon Data.')
        parser.add_argument('-f', '--file', help='full path of the csv file containing presentmon data')
        args = parser.parse_args()

        if args.file:
            file_path = args.file
        else:
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename(initialdir='~',
                                                   filetypes=(('Presentmon Files', '*.csv'), ('All Files', '*')))
            root.destroy()

        if not file_path:
            exit(0)

        columns = ['TimeInSeconds', 'msGPUActive', 'CPUUtilization[%]']
        data = self.data_loader.load_data(file_path, columns)
        processor = DataProcessor(data)

        time_in_seconds = data[:, 0]
        gpu_active_time = data[:, 1]
        cpu_utilization = data[:, 2]

        time_intervals = np.diff(time_in_seconds) * 1000
        time_intervals = np.insert(time_intervals, 0, time_intervals[0])
        cpu_active_time = processor.calculate_cpu_active_time(cpu_utilization, time_intervals)

        total_time = cpu_active_time + gpu_active_time
        cpu_percentage = (cpu_active_time / total_time) * 100
        gpu_percentage = (gpu_active_time / total_time) * 100

        # CPU Active Time % Trace
        self.plot_builder.add_trace(x=time_in_seconds, y=cpu_percentage,
                                    labels={
                                        "time_in_seconds": "Seconds",
                                        "cpu_percentage": "CPU Active Time %",
                                    },
                                    fill='tonexty',
                                    fillcolor='rgba(0,100,80,0.5)',
                                    line=dict(color='rgba(0,100,80,1)'),
                                    name='CPU Active Time %', row=3, col=1)

        # GPU Active Time % Trace
        self.plot_builder.add_trace(x=time_in_seconds, y=gpu_percentage,
                                    labels={
                                        "time_in_seconds": "Seconds",
                                        "gpu_percentage": "GPU Active Time %",
                                    },
                                    fill='tonexty',
                                    fillcolor='rgba(0,176,246,0.5)',
                                    line=dict(color='rgba(0,176,246,1)'),
                                    name='GPU Active Time %', row=3, col=1)

        additional_columns = ['msBetweenPresents']
        additional_data = DataProcessor.load_data(file_path, additional_columns)
        ms_between_presents = additional_data[:, 0]
        fps = 1 / (ms_between_presents / 1000)

        # FPS subplot
        self.plot_builder.add_trace(
            x=time_in_seconds,
            y=fps,
            mode='lines',
            name='FPS',
            labels={
                "time_in_seconds": "Seconds",
                "fps": "FPS",
            }, row=1, col=1)

        # Frametime subplot
        self.plot_builder.add_trace(
            x=time_in_seconds,
            y=ms_between_presents,
            mode='lines',
            name='Frametime',
            labels={
                "time_in_seconds": "Seconds",
                "ms_between_presents": "Frametime",
            },
            row=2, col=1)

        # Load additional columns for new metrics
        additional_columns_for_metrics = ['GPUFrequency[MHz]', 'GPUPower[W]', 'GPUTemperature[C]', 'CPUFrequency[MHz]',
                                          'CPUPower[W]', 'CPUTemperature[C]']
        additional_data_for_metrics = self.data_loader.load_data(file_path, additional_columns_for_metrics)

        gpu_frequency = additional_data_for_metrics[:, 0]
        gpu_power = additional_data_for_metrics[:, 1]
        gpu_temperature = additional_data_for_metrics[:, 2]
        cpu_frequency = additional_data_for_metrics[:, 3]
        cpu_power = additional_data_for_metrics[:, 4]
        cpu_temperature = additional_data_for_metrics[:, 5]

        # Calculate new metrics
        gpu_performance_per_watt = DataProcessor.calculate_performance_per_watt(gpu_frequency, gpu_power)
        cpu_performance_per_watt = DataProcessor.calculate_performance_per_watt(cpu_frequency, cpu_power)
        gpu_thermal_headroom = DataProcessor.calculate_thermal_headroom(gpu_temperature)
        cpu_thermal_headroom = DataProcessor.calculate_thermal_headroom(cpu_temperature)

        # Add new traces for the new metrics
        self.plot_builder.add_trace(x=time_in_seconds, y=gpu_performance_per_watt, mode='lines', labels={
            "time_in_seconds": "Seconds",
            "gpu_performance_per_watt": "Performance/Watt",
        },
                                    name='GPU Performance/Watt', row=4, col=1)
        self.plot_builder.add_trace(x=time_in_seconds, y=cpu_performance_per_watt, mode='lines', labels={
            "time_in_seconds": "Seconds",
            "cpu_performance_per_watt": "Performance/Watt",
        },
                                    name='CPU Performance/Watt', row=5, col=1)
        self.plot_builder.add_trace(x=time_in_seconds, y=gpu_thermal_headroom, mode='lines', labels={
            "time_in_seconds": "Seconds",
            "gpu_thermal_headroom": "Thermal Headroom",
        },
                                    name='GPU Thermal Headroom', row=6, col=1)
        self.plot_builder.add_trace(x=time_in_seconds, y=cpu_thermal_headroom, mode='lines', labels={
            "time_in_seconds": "Seconds",
            "cpu_thermal_headroom": "Thermal Headroom",
        },
                                    name='CPU Thermal Headroom', row=7, col=1)

        self.plot_builder.show_plot()
