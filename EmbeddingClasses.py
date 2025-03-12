from sentence_transformers import SentenceTransformer
import numpy as np

# Load the model from the saved directory
model = SentenceTransformer("../models/all-MiniLM-L6-v2")

class Phrase:
    def __init__(self, sentence):
        self.sentence = sentence
        self.embedding = model.encode(sentence)

    def get_embedding(self):
        return self.embedding

    def cosine_similarity(self, other_phrase):
        """Calculate the cosine similarity between this phrase and another"""
        a = self.embedding
        b = other_phrase.get_embedding()

        # Compute the cosine similarity
        similarity = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
        return similarity
