import os
import json
from ..utils.config import Config

class DataLoader:
    @staticmethod
    def load_data(file_name):
        file_path = os.path.join(Config.RAW_DATA_DIR, file_name)
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

if __name__ == "__main__":
    data = DataLoader.load_data('sample_data.json')
    print(data)
