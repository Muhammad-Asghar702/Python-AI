import spacy

class SpacyModel:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def process_text(self, text):
        doc = self.nlp(text)
        return [(token.text, token.pos_) for token in doc]

if __name__ == "__main__":
    model = SpacyModel()
    result = model.process_text("What is the capital of France?")
    print(result)
