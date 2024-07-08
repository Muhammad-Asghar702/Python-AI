import sys
import os


# Add the project root to the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import json
import tkinter as tk
from tkinter import scrolledtext
from tkinter import font as tkfont
from tkinter import ttk
from src.models.spacy_model import SpacyModel
from src.models.nltk_model import NLTKModel
from src.utils.config import Config
import Levenshtein

class RoundedEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        tk.Entry.__init__(self, master, **kwargs)
        self.config(borderwidth=0, highlightthickness=0, relief='flat', font=("Helvetica", 12), bg='#3c3f41', fg='white', insertbackground='white')
        self['justify'] = 'center'
        self.master = master

class RoundedButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        tk.Button.__init__(self, master, **kwargs)
        self.config(borderwidth=0, highlightthickness=0, relief='flat', font=("Helvetica", 12, "bold"), bg='#4caf50', fg='white')
        self['justify'] = 'center'
        self.master = master

class AIChatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Chatbot")
        self.root.configure(bg='#2b2b2b')

        self.spacy_model = SpacyModel()
        self.nltk_model = NLTKModel()

        # Load preprocessed data
        self.preprocessed_data = self.load_preprocessed_data()

        # Create custom fonts
        self.title_font = tkfont.Font(family="Helvetica", size=18, weight="bold")
        self.label_font = tkfont.Font(family="Helvetica", size=12)
        self.entry_font = tkfont.Font(family="Helvetica", size=12)
        self.button_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
        self.response_font = tkfont.Font(family="Helvetica", size=12)

        # Create widgets
        self.create_widgets()

    def load_preprocessed_data(self):
        file_path = os.path.join(Config.PROCESSED_DATA_DIR, 'processed_data.json')
        with open(file_path, 'r') as file:
            return json.load(file)

    def create_widgets(self):
        # Entry for user input
        self.input_label = tk.Label(self.root, text="Enter your question:", bg='#2b2b2b', fg='white', font=self.label_font)
        self.input_label.pack(pady=10)

        self.user_input = RoundedEntry(self.root, width=80)
        self.user_input.pack(pady=5)
        self.user_input.bind("<Return>", self.get_response)

        # Button to get response
        self.ask_button = RoundedButton(self.root,  text="Ask", command=self.get_response)
        self.ask_button.pack(pady=10)

        # Text area to display response
        self.response_label = tk.Label(self.root, text="Response:", bg='#2b2b2b', fg='white', font=self.label_font)
        self.response_label.pack(pady=10)

        self.response_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=80, height=20, font=self.response_font, bg='#3c3f41', fg='white', insertbackground='white')
        self.response_area.pack(pady=10)

    def get_response(self, event=None):
        question = self.user_input.get()

        # Find the best matching question in the preprocessed data
        best_match = None
        best_score = float('inf')
        for item in self.preprocessed_data:
            processed_question = ' '.join([token[0] for token in item['question']])
            score = Levenshtein.distance(processed_question.lower(), question.lower())
            if score < best_score:
                best_score = score
                best_match = item

        if best_match:
            response = best_match['answer']
        else:
            response = "I'm sorry, I don't understand the question."

        # Display response
        self.response_area.delete(1.0, tk.END)
        self.response_area.insert(tk.INSERT, response)
        self.user_input.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AIChatGUI(root)
    root.mainloop()
