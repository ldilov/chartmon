import pandas as pd


class DataLoader:
    @staticmethod
    def load_data(file_path, columns):
        try:
            df = pd.read_csv(file_path)
            return df[columns].to_numpy()
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            exit(1)
