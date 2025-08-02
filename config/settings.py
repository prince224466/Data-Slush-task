# Configuration settings for DataSlush Talent Recommendation System

# API Configuration
GEMINI_API_KEY = "AIzaSyDwQC6K-OvRBabozd4maasKv39wZwXcyVI"
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
API_TIMEOUT = 10

# Data Configuration
TALENT_DATA_FILE = "Talent Profiles - talent_samples.csv"
CREATORS_DATA_FILE = "Talent Profiles - creators_hiring (optional).csv"
EMBEDDINGS_FILE = "data/embeddings/talent_embeddings.pkl"
VECTORIZER_FILE = "data/models/tfidf_vectorizer.pkl"

# Model Configuration
TFIDF_MAX_FEATURES = 200
TFIDF_STOP_WORDS = 'english'
MIN_SCORE_FOR_AI_ANALYSIS = 30

# Scoring Weights
SKILL_MATCH_WEIGHT = 15
LOCATION_MATCH_WEIGHT = 25
BUDGET_MATCH_WEIGHT = 20
CONTENT_MATCH_WEIGHT = 15
SOFTWARE_MATCH_WEIGHT = 10
AI_ANALYSIS_WEIGHT = 2

# Progress Configuration
PROGRESS_UPDATE_INTERVAL = 100

# Job Requirements
JOB_REQUIREMENTS = {
    1: {
        'title': "Video Editor for Entertainment/Lifestyle Creator",
        'requirements': {
            'skills': 'Adobe Premiere Pro, Splice & Dice, Rough Cut & Sequencing, 2D Animation',
            'software': 'Adobe Premiere Pro, Adobe After Effects',
            'location': 'Asia',
            'budget': 2500,
            'content_type': 'Entertainment/Lifestyle & Vlogs'
        }
    },
    2: {
        'title': "Producer/Video Editor for Education/Food Creator",
        'requirements': {
            'skills': 'Storyboarding, Sound Designing, Rough Cut & Sequencing, Filming',
            'software': 'Adobe Premiere Pro, Adobe After Effects, Final Cut Pro',
            'location': 'New York, US',
            'budget': 150,
            'content_type': 'Entertainment/Education/Food & Cooking'
        }
    },
    3: {
        'title': "Chief Operation Officer for Productivity Channel",
        'requirements': {
            'skills': 'Strategy & Consulting, Business operations, Development',
            'software': 'Excel, Notion, Slack',
            'location': 'Remote',
            'budget': 10000,
            'content_type': 'Productivity'
        }
    }
} 