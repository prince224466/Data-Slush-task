import pandas as pd
import os
from config.settings import TALENT_DATA_FILE, CREATORS_DATA_FILE

class DataLoader:
    """Utility class for loading and validating data files"""
    
    @staticmethod
    def load_talent_data():
        """Load talent data from CSV file"""
        try:
            if not os.path.exists(TALENT_DATA_FILE):
                raise FileNotFoundError(f"Talent data file not found: {TALENT_DATA_FILE}")
            
            print("Loading talent data...")
            data = pd.read_csv(TALENT_DATA_FILE)
            print(f"Loaded {len(data)} talent profiles")
            
            # Validation
            required_columns = ['First Name', 'Last Name', 'Skills', 'Job Types', 'Software']
            missing_columns = [col for col in required_columns if col not in data.columns]
            
            if missing_columns:
                raise ValueError(f"Missing required columns: {missing_columns}")
            
            return data
            
        except Exception as e:
            print(f"Error loading talent data: {e}")
            return None
    
    @staticmethod
    def load_creators_data():
        """Load creators hiring data from CSV file"""
        try:
            if not os.path.exists(CREATORS_DATA_FILE):
                print(f"Warning: Creators data file not found: {CREATORS_DATA_FILE}")
                return None
            
            print("Loading creators hiring data...")
            data = pd.read_csv(CREATORS_DATA_FILE)
            print(f"Loaded {len(data)} creator job postings")
            
            return data
            
        except Exception as e:
            print(f"Error loading creators data: {e}")
            return None
    
    @staticmethod
    def validate_data(data):
        """Validate loaded data for required fields"""
        if data is None or data.empty:
            return False
        
        # Check for required columns
        required_columns = ['First Name', 'Last Name', 'Skills', 'Job Types']
        for col in required_columns:
            if col not in data.columns:
                print(f"Missing required column: {col}")
                return False
        
        # Check for non-empty data
        if len(data) == 0:
            print("Data is empty")
            return False
        
        return True
    
    @staticmethod
    def preprocess_data(data):
        """Data preprocessing"""
        if data is None:
            return None
        
        # Fill missing values
        data = data.fillna('')
        
        # Convert to string and clean
        text_columns = ['Job Types', 'Skills', 'Software', 'Content Verticals', 'Creative Styles', 'Profile Description']
        for col in text_columns:
            if col in data.columns:
                data[col] = data[col].astype(str).str.strip()
        
        return data 
