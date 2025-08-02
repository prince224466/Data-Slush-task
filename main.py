import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.data_loader import DataLoader
from models.embedding_model import EmbeddingModel
from scoring.scoring_engine import ScoringEngine
from ui.console_interface import ConsoleInterface
from services.gemini_service import GeminiService
from config.settings import PROGRESS_UPDATE_INTERVAL

class TalentRecommender:
    """Basic recommendation system"""
    
    def __init__(self):
        self.data_loader = DataLoader()
        self.embedding_model = EmbeddingModel()
        self.scoring_engine = ScoringEngine()
        self.gemini_service = GeminiService()
        self.ui = ConsoleInterface()
        
        self.talent_data = None
        self.creators_data = None
        
    def initialize_system(self):
        """Initialize the recommendation system"""
        print("Initializing DataSlush Talent Recommendation System...")
        
        # Load data
        self.talent_data = self.data_loader.load_talent_data()
        if not self.data_loader.validate_data(self.talent_data):
            print("Failed to load or validate talent data")
            return False
        
        self.creators_data = self.data_loader.load_creators_data()
        
        # Preprocess data
        self.talent_data = self.data_loader.preprocess_data(self.talent_data)
        
        # Load or create embeddings
        if not self.embedding_model.load_embeddings():
            print("Creating new embeddings...")
            self.talent_data = self.embedding_model.create_text_representations(self.talent_data)
            self.embedding_model.generate_embeddings(self.talent_data['combined_text'])
            self.embedding_model.save_embeddings()
        
        return True
    
    def recommend_for_job(self, job_title, job_requirements):
        """Generate recommendations for a specific job"""
        print(f"\nGenerating recommendations for: {job_title}")
        
        recommendations = []
        total_talents = len(self.talent_data)
        
        print(f"Analyzing {total_talents} talent profiles...")
        
        for idx, talent in self.talent_data.iterrows():
            if idx % PROGRESS_UPDATE_INTERVAL == 0:
                self.ui.show_progress(idx + 1, total_talents, "Processing talents")
            
            score = self.scoring_engine.calculate_score(talent, job_requirements)
            
            if score > 0:
                recommendations.append({
                    'name': f"{talent['First Name']} {talent['Last Name']}",
                    'location': f"{talent['City']}, {talent['Country']}",
                    'job_types': talent['Job Types'],
                    'skills': talent['Skills'],
                    'monthly_rate': talent['Monthly Rate'],
                    'content_verticals': talent['Content Verticals'],
                    'software': talent['Software'],
                    'score': score
                })
        
        print(f"\nFound {len(recommendations)} matching candidates")
        
        # Sort by score and take top 10
        recommendations.sort(key=lambda x: x['score'], reverse=True)
        top_recommendations = recommendations[:10]
        
        # Display recommendations
        self.ui.show_recommendations(top_recommendations, job_title)
        
        return top_recommendations
    
    def run_interactive_mode(self):
        """Run the system in interactive mode"""
        self.ui.show_welcome()
        
        while True:
            self.ui.show_menu()
            choice = self.ui.get_user_choice()
            
            if choice is None:
                continue
            elif choice == 4:
                self.ui.show_farewell()
                break
            elif choice in [1, 2, 3]:
                # Show job details
                job_info = self.ui.show_job_details(choice)
                if job_info:
                    # Generate recommendations
                    self.recommend_for_job(job_info['title'], job_info['requirements'])
                    
                    # Ask if user wants to continue
                    if not self.ui.ask_continue():
                        self.ui.show_farewell()
                        break
                else:
                    print("Invalid job selection")
            else:
                print("Invalid choice")

def main():
    """Main function"""
    try:
        # Create recommender instance
        recommender = TalentRecommender()
        
        # Initialize system
        if not recommender.initialize_system():
            print("System initialization failed. Exiting.")
            return
        
        # Run interactive mode
        recommender.run_interactive_mode()
        
    except KeyboardInterrupt:
        print("\nGoodbye!")
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main() 