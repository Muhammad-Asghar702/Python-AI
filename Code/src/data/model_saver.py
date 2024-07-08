import os
import torch
from ..utils.config import Config

class ModelSaver:
    @staticmethod
    def save_pytorch_model(model, file_name):
        file_path = os.path.join(Config.MODEL_DIR, file_name)
        torch.save(model.state_dict(), file_path)
        print(f"Model saved to {file_path}")

    @staticmethod
    def load_pytorch_model(model, file_name):
        file_path = os.path.join(Config.MODEL_DIR, file_name)
        model.load_state_dict(torch.load(file_path))
        model.eval()
        print(f"Model loaded from {file_path}")
        return model

if __name__ == "__main__":
    # Example usage (assuming `model` is a PyTorch model instance)
    pass
