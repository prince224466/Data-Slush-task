import requests
import json
from config.settings import GEMINI_API_KEY, GEMINI_URL, API_TIMEOUT

class GeminiService:
    """Service class for interacting with Google Gemini API"""
    
    def __init__(self):
        self.api_key = GEMINI_API_KEY
        self.base_url = GEMINI_URL
        self.timeout = API_TIMEOUT
    
    def analyze_personality_fit(self, talent_description, job_requirements):
        """Analyze personality fit between talent and job using Gemini AI"""
        try:
            prompt = f"""
            Analyze if this talent profile fits the job requirements.
            
            Talent Description: {talent_description[:300]}...
            Job Requirements: {job_requirements}
            
            Consider:
            1. Skills alignment
            2. Experience relevance
            3. Personality traits
            4. Work style compatibility
            
            Return only a number between 0-10 representing the fit score.
            """
            
            response = self._call_api(prompt)
            if response and response.isdigit():
                return int(response)
            return 0
            
        except Exception as e:
            print(f"Error in personality analysis: {e}")
            return 0
    
    def analyze_skill_compatibility(self, talent_skills, required_skills):
        """Analyze skill compatibility using AI"""
        try:
            prompt = f"""
            Analyze the compatibility between talent skills and required skills.
            
            Talent Skills: {talent_skills}
            Required Skills: {required_skills}
            
            Consider:
            1. Direct skill matches
            2. Related skills
            3. Transferable skills
            4. Skill level assessment
            
            Return only a number between 0-10 representing skill compatibility.
            """
            
            response = self._call_api(prompt)
            if response and response.isdigit():
                return int(response)
            return 0
            
        except Exception as e:
            print(f"Error in skill analysis: {e}")
            return 0
    
    def analyze_cultural_fit(self, talent_profile, company_culture):
        """Analyze cultural fit using AI"""
        try:
            prompt = f"""
            Analyze the cultural fit between talent and company culture.
            
            Talent Profile: {talent_profile[:200]}...
            Company Culture: {company_culture}
            
            Consider:
            1. Work style preferences
            2. Communication style
            3. Values alignment
            4. Team dynamics
            
            Return only a number between 0-10 representing cultural fit.
            """
            
            response = self._call_api(prompt)
            if response and response.isdigit():
                return int(response)
            return 0
            
        except Exception as e:
            print(f"Error in cultural analysis: {e}")
            return 0
    
    def _call_api(self, prompt):
        """Make API call to Gemini"""
        try:
            headers = {
                'Content-Type': 'application/json',
            }
            
            data = {
                "contents": [{
                    "parts": [{
                        "text": prompt
                    }]
                }]
            }
            
            response = requests.post(
                f"{self.base_url}?key={self.api_key}",
                headers=headers,
                json=data,
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                result = response.json()
                if 'candidates' in result and len(result['candidates']) > 0:
                    return result['candidates'][0]['content']['parts'][0]['text'].strip()
            
            return ""
            
        except requests.exceptions.Timeout:
            print("API call timed out")
            return ""
        except Exception as e:
            print(f"API call error: {e}")
            return ""
    
    def test_connection(self):
        """Test API connection"""
        try:
            test_prompt = "Return the number 5"
            response = self._call_api(test_prompt)
            if response == "5":
                print("✓ Gemini API connection successful")
                return True
            else:
                print("⚠ Gemini API connection failed")
                return False
        except Exception as e:
            print(f"✗ Gemini API connection error: {e}")
            return False 