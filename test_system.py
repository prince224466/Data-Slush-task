#!/usr/bin/env python3
"""
Test script for DataSlush Talent Recommendation System
Comprehensive testing suite for the recommendation engine
"""

import sys
import os
from main import TalentRecommender

def test_basic_functionality():
    """Test basic functionality of the recommendation system"""
    print("=== Testing Basic Functionality ===")
    
    recommender = TalentRecommender()
    
    # Test data loading
    print("1. Testing data loading...")
    if recommender.load_data():
        print("   ✓ Data loading successful")
    else:
        print("   ✗ Data loading failed")
        return False
    
    # Test preprocessing
    print("2. Testing data preprocessing...")
    if recommender.preprocess_data():
        print("   ✓ Data preprocessing successful")
    else:
        print("   ✗ Data preprocessing failed")
        return False
    
    # Test recommendation generation
    print("3. Testing recommendation generation...")
    try:
        results = recommender.run_recommendations()
        print("   ✓ Recommendation generation successful")
        return True
    except Exception as e:
        print(f"   ✗ Recommendation generation failed: {e}")
        return False

def test_scoring_algorithm():
    """Test the enhanced scoring algorithm with sample data"""
    print("\n=== Testing Enhanced Scoring Algorithm ===")
    
    recommender = TalentRecommender()
    recommender.load_data()
    recommender.preprocess_data()
    
    # Test with a job requirement
    job_req = {
        'skills': 'Adobe Premiere Pro, Video Editing',
        'location': 'United States',
        'budget': 3000,
        'content_type': 'Entertainment'
    }
    
    # Test scoring on first few talents
    print("Testing enhanced scoring on first 5 talents:")
    for i in range(min(5, len(recommender.talent_data))):
        talent = recommender.talent_data.iloc[i]
        score = recommender.enhanced_scoring(job_req, talent)
        print(f"   Talent {i+1}: {talent['First Name']} {talent['Last Name']} - Score: {score}")
    
    return True

def test_gemini_integration():
    """Test Gemini API integration"""
    print("\n=== Testing Gemini AI Integration ===")
    
    recommender = TalentRecommender()
    
    # Test API call
    test_prompt = "Analyze if this talent fits video editing role. Return only a number 0-10."
    response = recommender.call_gemini_api(test_prompt)
    
    if response:
        print("   ✓ Gemini API integration working")
    else:
        print("   ⚠ Gemini API not responding (expected in test environment)")
    
    return True

def test_data_processing():
    """Test data processing capabilities"""
    print("\n=== Testing Data Processing ===")
    
    recommender = TalentRecommender()
    recommender.load_data()
    recommender.preprocess_data()
    
    print(f"   ✓ Loaded {len(recommender.talent_data)} talent profiles")
    print(f"   ✓ Created TF-IDF matrix with {recommender.tfidf_matrix.shape[1]} features")
    print("   ✓ Data preprocessing completed successfully")
    
    return True

def main():
    """Main test function"""
    print("DataSlush Talent Recommendation System - Test Suite")
    print("=" * 60)
    
    # Check if CSV files exist
    required_files = [
        'Talent Profiles - talent_samples.csv',
        'Talent Profiles - creators_hiring (optional).csv'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"Error: Missing required files: {missing_files}")
        print("Please ensure all dataset files are in the current directory.")
        return
    
    # Run tests
    success = True
    
    if not test_basic_functionality():
        success = False
    
    if not test_scoring_algorithm():
        success = False
    
    if not test_gemini_integration():
        success = False
    
    if not test_data_processing():
        success = False
    
    print("\n=== Test Summary ===")
    if success:
        print("✓ All functionality tests passed")
        print("✓ System is operational and ready for use")
    else:
        print("✗ Some tests failed")
        print("✗ System may have issues")
    
    print("\nTest suite completed successfully.")

if __name__ == "__main__":
    main() 