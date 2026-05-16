from sentence_transformers import SentenceTransformer
import numpy as np

class Vectorizer:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def get_embeddings(self, texts):
        if isinstance(texts, str):
            texts = [texts]
        return self.model.encode(texts)

    def compute_similarity(self, embedding1, embedding2):
        # Flatten if needed
        if embedding1.ndim == 1:
            embedding1 = embedding1.reshape(1, -1)
        if embedding2.ndim == 1:
            embedding2 = embedding2.reshape(1, -1)
            
        from sklearn.metrics.pairwise import cosine_similarity
        return cosine_similarity(embedding1, embedding2)[0][0]
