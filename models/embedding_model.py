import pickle
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from config.settings import (
    EMBEDDINGS_FILE, VECTORIZER_FILE, TFIDF_MAX_FEATURES, 
    TFIDF_STOP_WORDS
)

class EmbeddingModel:
    """Handles text embedding generation and storage"""
    
    def __init__(self):
        self.vectorizer = None
        self.tfidf_matrix = None
        
    def create_text_representations(self, data):
        """Create comprehensive text representations for talent profiles"""
        print("Creating comprehensive text representations...")
        
        # Combine all text fields
        data['combined_text'] = (
            data['Job Types'].astype(str) + ' ' +
            data['Skills'].astype(str) + ' ' +
            data['Software'].astype(str) + ' ' +
            data['Content Verticals'].astype(str) + ' ' +
            data['Creative Styles'].astype(str) + ' ' +
            data['Profile Description'].astype(str)
        )
        
        return data
    
    def generate_embeddings(self, text_data):
        """Generate TF-IDF embeddings from text data"""
        print("Generating TF-IDF embeddings...")
        
        # Create TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer(
            max_features=TFIDF_MAX_FEATURES,
            stop_words=TFIDF_STOP_WORDS
        )
        
        # Generate embeddings
        self.tfidf_matrix = self.vectorizer.fit_transform(text_data)
        
        print(f"Embeddings created: {self.tfidf_matrix.shape}")
        return self.tfidf_matrix
    
    def save_embeddings(self):
        """Save embeddings and vectorizer to files"""
        # Create directories if they don't exist
        os.makedirs(os.path.dirname(EMBEDDINGS_FILE), exist_ok=True)
        os.makedirs(os.path.dirname(VECTORIZER_FILE), exist_ok=True)
        
        print("Saving embeddings to file...")
        
        # Save embeddings
        with open(EMBEDDINGS_FILE, 'wb') as f:
            pickle.dump(self.tfidf_matrix, f)
        
        # Save vectorizer
        with open(VECTORIZER_FILE, 'wb') as f:
            pickle.dump(self.vectorizer, f)
        
        print(f"Embeddings saved: {self.tfidf_matrix.shape}")
    
    def load_embeddings(self):
        """Load existing embeddings from files"""
        try:
            if os.path.exists(EMBEDDINGS_FILE) and os.path.exists(VECTORIZER_FILE):
                print("Loading existing embeddings...")
                
                # Load embeddings
                with open(EMBEDDINGS_FILE, 'rb') as f:
                    self.tfidf_matrix = pickle.load(f)
                
                # Load vectorizer
                with open(VECTORIZER_FILE, 'rb') as f:
                    self.vectorizer = pickle.load(f)
                
                print("Embeddings loaded successfully")
                return True
            else:
                print("No existing embeddings found")
                return False
                
        except Exception as e:
            print(f"Error loading embeddings: {e}")
            return False
    
    def get_embedding_similarity(self, text1, text2):
        """Calculate similarity between two text inputs"""
        if self.vectorizer is None:
            return 0.0
        
        # Transform texts
        text1_vector = self.vectorizer.transform([text1])
        text2_vector = self.vectorizer.transform([text2])
        
        # Calculate cosine similarity
        similarity = np.dot(text1_vector.toarray(), text2_vector.toarray().T)[0][0]
        
        return similarity
    
    def get_embedding_stats(self):
        """Get statistics about the embeddings"""
        if self.tfidf_matrix is None:
            return None
        
        return {
            'shape': self.tfidf_matrix.shape,
            'sparsity': self.tfidf_matrix.nnz / (self.tfidf_matrix.shape[0] * self.tfidf_matrix.shape[1]),
            'features': self.vectorizer.get_feature_names_out().shape[0] if self.vectorizer else 0
        } 