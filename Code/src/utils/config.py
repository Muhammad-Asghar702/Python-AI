import os

class Config:
    DATA_DIR = os.path.join(os.path.dirname(__file__), '../../data/')
    RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw/')
    PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed/')
    MODEL_DIR = os.path.join(DATA_DIR, 'models/')
    LOG_DIR = os.path.join(os.path.dirname(__file__), '../../logs/')

    @staticmethod
    def ensure_directories():
        dirs = [Config.DATA_DIR, Config.RAW_DATA_DIR, Config.PROCESSED_DATA_DIR, Config.MODEL_DIR, Config.LOG_DIR]
        for d in dirs:
            if not os.path.exists(d):
                os.makedirs(d)

if __name__ == "__main__":
    Config.ensure_directories()
