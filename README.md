# DataSlush Talent Recommendation System

## Overview

This talent recommendation system for DataSlush matches creators with potential talent based on job requirements. The system uses text embeddings and Gemini AI for basic analysis and provides recommendations for job postings.

## Project Structure

```
Data-Slush-task/
├── main.py                          # Main application
├── requirements.txt                  # Python dependencies
├── README.md                        # This file
├── .gitignore                       # Git ignore file
├── config/
│   └── settings.py                  # Configuration settings
├── utils/
│   └── data_loader.py              # Data loading utilities
├── models/
│   └── embedding_model.py           # TF-IDF embedding model
├── services/
│   └── gemini_service.py           # Gemini API service
├── scoring/
│   └── scoring_engine.py           # Basic scoring algorithm
├── ui/
│   └── console_interface.py        # User interface
└── data/
    ├── embeddings/                  # Embeddings storage
    └── models/                      # Model storage
```

## Features

- **Basic Talent Matching**: Scoring algorithm using skills, location, and budget
- **Gemini AI Integration**: Uses Google's Gemini API for basic personality analysis
- **Top 10 Recommendations**: Provides recommendations for each job posting
- **Interactive Console**: Console-based interface for viewing recommendations

## Installation

1. Clone or download the project files
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure all CSV dataset files are in the project directory

## Usage

Run the main script:
```bash
python main.py
```

The system will:
1. Load talent and creator data
2. Preprocess data and create embeddings
3. Show interactive menu to select job roles
4. Display top 10 candidates for selected position

## Job Postings Covered

1. **Video Editor for Entertainment/Lifestyle Creator**
   - Skills: Adobe Premiere Pro, Splice & Dice, Rough Cut & Sequencing, 2D Animation
   - Location: Asia preferred
   - Budget: $2500/month

2. **Producer/Video Editor for Education/Food Creator**
   - Skills: Storyboarding, Sound Designing, Rough Cut & Sequencing, Filming
   - Location: New York (1st priority) or remote US
   - Budget: $100-150/hour

3. **Chief Operation Officer for Productivity Channel**
   - Skills: Strategy & Consulting, Business operations, Development
   - Location: Remote
   - Budget: No limitation

## Technical Implementation

### Data Processing
- Uses pandas for data loading and manipulation
- Basic text preprocessing with TF-IDF vectorization
- Text representation combining talent attributes

### Scoring Algorithm
The scoring system considers basic factors:
- Skill matching: +15 points per matching skill
- Location matching: +25 points for location match
- Budget compatibility: +20 points if talent rate fits budget
- Content vertical matching: +15 points for content fit
- Software matching: +10 points per matching software
- AI analysis: +2 points per AI score (for high-scoring candidates only)

### AI Integration
- Integrates with Google's Gemini API for basic personality analysis
- Analyzes talent descriptions against job requirements
- Provides additional scoring based on AI insights

## Dependencies

- pandas: Data manipulation
- numpy: Numerical operations
- scikit-learn: Machine learning and embeddings
- requests: API communication with Gemini

## Files Description

- **main.py**: Main application entry point
- **config/settings.py**: Configuration parameters and job requirements
- **utils/data_loader.py**: Data loading and validation utilities
- **models/embedding_model.py**: TF-IDF embedding generation and storage
- **services/gemini_service.py**: Gemini API integration service
- **scoring/scoring_engine.py**: Basic scoring algorithm implementation
- **ui/console_interface.py**: Console user interface 