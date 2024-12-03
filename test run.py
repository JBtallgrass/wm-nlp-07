import spacy
import nltk
from bs4 import BeautifulSoup
from textblob import TextBlob
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Optional
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from wordcloud import WordCloud

class TextAnalyzer:
    """A class for analyzing text documents with NLP techniques."""
    
    def __init__(self, nlp_model: str = 'en_core_web_sm'):
        """Initialize the analyzer with required models and resources."""
        self.nlp = spacy.load(nlp_model)
        self._ensure_nltk_resources()
        
    @staticmethod
    def _ensure_nltk_resources():
        """Ensure required NLTK resources are downloaded."""
        resources = ['punkt', 'stopwords', 'wordnet']
        for resource in resources:
            try:
                nltk.data.find(f'tokenizers/{resource}')
            except LookupError:
                nltk.download(resource)

    def load_text_from_html(self, file_path: str, start_marker: Optional[str] = None) -> str:
        """Load and clean text from HTML file."""
        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file.read(), "html.parser")
            
        # Remove unwanted elements
        for tag in ['script', 'style', 'nav', 'header', 'footer']:
            for element in soup.find_all(tag):
                element.decompose()
                
        text = ' '.join(p.get_text().strip() for p in soup.find_all('p'))
        
        if start_marker:
            start_idx = text.find(start_marker)
            if start_idx != -1:
                text = text[start_idx + len(start_marker):]
                
        return text.strip()

    def analyze_sentiment(self, text: str) -> Dict:
        """Perform sentiment analysis on text."""
        blob = TextBlob(text)
        return {
            'polarity': blob.sentiment.polarity,
            'sentence_count': len(blob.sentences)
        }

    def get_token_frequencies(self, text: str, top_n: int = 5) -> List[Tuple[str, int]]:
        """Get most frequent tokens."""
        doc = self.nlp(text)
        tokens = [token.text.lower() for token in doc 
                 if not token.is_stop and not token.is_punct and not token.is_space]
        return Counter(tokens).most_common(top_n)

    def get_lemma_frequencies(self, text: str, top_n: int = 5) -> List[Tuple[str, int]]:
        """Get most frequent lemmas."""
        doc = self.nlp(text)
        lemmas = [token.lemma_.lower() for token in doc 
                 if not token.is_stop and not token.is_punct and not token.is_space]
        return Counter(lemmas).most_common(top_n)

    def create_chunks(self, text: str, chunk_size: int = 5000) -> List[Tuple[str, str]]:
        """Split text into chunks of specified size."""
        chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
        return [(f"Chunk {i+1}", chunk.strip()) for i, chunk in enumerate(chunks)]

    def generate_sentiment_heatmap(self, chunks: List[Tuple[str, str]], 
                                 output_path: str = "sentiment_heatmap.png"):
        """Generate and save sentiment heatmap for text chunks."""
        # Process chunks and create sentiment matrix
        sentiment_data = []
        for _, content in chunks:
            paragraphs = content.split("\n\n")
            scores = [TextBlob(p.strip()).sentiment.polarity for p in paragraphs if p.strip()]
            sentiment_data.append(scores)

        # Create heatmap matrix
        max_paragraphs = max(len(scores) for scores in sentiment_data)
        heatmap_data = np.full((len(sentiment_data), max_paragraphs), np.nan)
        for i, scores in enumerate(sentiment_data):
            heatmap_data[i, :len(scores)] = scores

        # Create visualization
        plt.figure(figsize=(20, 12))
        sns.heatmap(
            pd.DataFrame(heatmap_data),
            cmap="coolwarm",
            cbar_kws={'label': 'Sentiment Polarity'},
            mask=pd.DataFrame(heatmap_data).isnull(),
            vmin=-1, vmax=1
        )
        plt.title("Sentiment Analysis Heatmap")
        plt.xlabel("Paragraphs")
        plt.ylabel("Chunks")
        plt.tight_layout()
        plt.savefig(output_path, dpi=300)
        plt.close()

    def analyze_themes(self, chunks: List[Tuple[str, str]], n_topics: int = 3) -> Dict:
        """Perform topic modeling on text chunks."""
        texts = [content for _, content in chunks]
        vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
        dtm = vectorizer.fit_transform(texts)
        
        lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
        lda.fit(dtm)
        
        themes = {}
        for idx, topic in enumerate(lda.components_):
            themes[f"Theme {idx + 1}"] = [
                vectorizer.get_feature_names_out()[i] 
                for i in topic.argsort()[-10:]
            ]
        
        return themes