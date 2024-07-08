import nltk
import spacy
from .data_loader import DataLoader
from ..utils.config import Config
import os
import json

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

class Preprocessor:
    @staticmethod
    def preprocess_text(text):
        # Tokenization using NLTK
        tokens = nltk.word_tokenize(text)
        
        # Remove stop words
        stop_words = set(nltk.corpus.stopwords.words('english'))
        tokens = [token for token in tokens if token.lower() not in stop_words]

        # POS tagging using spaCy
        doc = nlp(' '.join(tokens))
        tokens = [[token.text, token.pos_] for token in doc]  # Convert tuples to lists

        return tokens

    @staticmethod
    def preprocess_data(input_file, output_file):
        data = DataLoader.load_data(input_file)
        processed_data = []

        for item in data:
            question = item.get('question', '')
            answer = item.get('answer', '')
            processed_data.append({
                'question': Preprocessor.preprocess_text(question),
                'answer': Preprocessor.preprocess_text(answer)
            })

        output_path = os.path.join(Config.PROCESSED_DATA_DIR, output_file)
        with open(output_path, 'w') as file:
            # Ensure data is JSON serializable
            json.dump(processed_data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    Preprocessor.preprocess_data('sample_data.json', 'processed_data.json')
