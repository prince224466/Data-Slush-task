import os
from config.settings import JOB_REQUIREMENTS

class ConsoleInterface:
    """Basic console interface for the recommendation system"""
    
    @staticmethod
    def show_welcome():
        """Display welcome message"""
        print("\n" + "="*60)
        print("           DATASLUSH TALENT RECOMMENDATION SYSTEM")
        print("="*60)
    
    @staticmethod
    def show_menu():
        """Display main menu"""
        print("\nAvailable Job Roles:")
        print("1. Video Editor for Entertainment/Lifestyle Creator")
        print("2. Producer/Video Editor for Education/Food Creator") 
        print("3. Chief Operation Officer for Productivity Channel")
        print("4. Exit")
        print("\nEnter your choice (1-4): ", end="")
    
    @staticmethod
    def show_job_details(job_id):
        """Show job information"""
        if job_id not in JOB_REQUIREMENTS:
            return None
        
        job_info = JOB_REQUIREMENTS[job_id]
        print(f"\nJob Details: {job_info['title']}")
        print("-" * 40)
        
        requirements = job_info['requirements']
        print(f"Location: {requirements['location']}")
        print(f"Budget: ${requirements['budget']}")
        print(f"Skills: {requirements['skills']}")
        print(f"Software: {requirements['software']}")
        print(f"Content Type: {requirements['content_type']}")
        
        return job_info
    
    @staticmethod
    def show_progress(current, total, message=""):
        """Show progress indicator"""
        percentage = (current / total) * 100
        print(f"\r{message} {percentage:.1f}% ({current}/{total})", end="", flush=True)
    
    @staticmethod
    def show_recommendations(recommendations, job_title):
        """Display recommendations"""
        print(f"\nTop Recommendations for: {job_title}")
        print("=" * 60)
        
        for i, rec in enumerate(recommendations, 1):
            print(f"\n{i}. {rec['name']} ({rec['location']})")
            print(f"   Job Types: {rec['job_types']}")
            print(f"   Skills: {rec['skills'][:80]}...")
            print(f"   Software: {rec['software'][:60]}...")
            print(f"   Content: {rec['content_verticals']}")
            print(f"   Monthly Rate: ${rec['monthly_rate']}")
            print(f"   Match Score: {rec['score']}")
            print("-" * 40)
    
    @staticmethod
    def get_user_choice():
        """Get user input"""
        try:
            choice = int(input())
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Invalid choice. Please enter 1-4.")
                return None
        except ValueError:
            print("Invalid input. Please enter a number (1-4).")
            return None
    
    @staticmethod
    def ask_continue():
        """Ask if user wants to continue"""
        print("\nPress Enter to continue or 'q' to quit: ", end="")
        choice = input().strip().lower()
        return choice != 'q'
    
    @staticmethod
    def show_farewell():
        """Show farewell message"""
        print("\nThank you for using DataSlush Talent Recommendation System!") 