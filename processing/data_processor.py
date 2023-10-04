import numpy as np
import pandas as pd


class DataProcessor:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def load_data(file_path, columns):
        try:
            df = pd.read_csv(file_path)
            return df[columns].to_numpy()
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            exit(1)

    @staticmethod
    def calculate_cpu_active_time(cpu_utilization, time_interval):
        return (cpu_utilization / 100) * time_interval

    @staticmethod
    def calculate_performance_per_watt(frequency, power):
        return frequency / power

    @staticmethod
    def calculate_thermal_headroom(temperature, max_safe_temperature=100):  # Assuming 100C as max safe temperature
        return max_safe_temperature - temperature
