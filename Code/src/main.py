import sys
import os

# Add the project root to the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data.preprocess import Preprocessor
from src.data.model_saver import ModelSaver
from src.models.spacy_model import SpacyModel
from src.models.nltk_model import NLTKModel
from src.models.pytorch_model import SimpleNN

def main():
    # Ensure directories exist
    from src.utils.config import Config
    Config.ensure_directories()

    # Preprocess Data
    Preprocessor.preprocess_data('sample_data.json', 'processed_data.json')

    # Initialize Models
    spacy_model = SpacyModel()
    nltk_model = NLTKModel()
    pytorch_model = SimpleNN(input_size=10, hidden_size=5, output_size=1)

    # Example Data
    example_text = "What is the capital of France?"

    # Process Text using Models
    print("spaCy Model:", spacy_model.process_text(example_text))
    print("NLTK Model:", nltk_model.process_text(example_text))

    # Save Models
    ModelSaver.save_pytorch_model(pytorch_model, 'pytorch_model.pth')

if __name__ == "__main__":
    main()
