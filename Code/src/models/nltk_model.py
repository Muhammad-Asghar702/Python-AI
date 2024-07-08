import nltk

class NLTKModel:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')

    def process_text(self, text):
        tokens = nltk.word_tokenize(text)
        stop_words = set(nltk.corpus.stopwords.words('english'))
        return [token for token in tokens if token.lower() not in stop_words]

if __name__ == "__main__":
    model = NLTKModel()
    result = model.process_text("What is the capital of France?")
    print(result)
