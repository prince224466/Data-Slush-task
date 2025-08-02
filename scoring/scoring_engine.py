from config.settings import (
    SKILL_MATCH_WEIGHT, LOCATION_MATCH_WEIGHT, BUDGET_MATCH_WEIGHT,
    CONTENT_MATCH_WEIGHT, SOFTWARE_MATCH_WEIGHT, AI_ANALYSIS_WEIGHT,
    MIN_SCORE_FOR_AI_ANALYSIS
)
from services.gemini_service import GeminiService

class ScoringEngine:
    """Scoring engine for talent evaluation"""
    
    def __init__(self):
        self.gemini_service = GeminiService()
    
    def calculate_score(self, talent_profile, job_requirements):
        """Calculate score for talent-job match"""
        score = 0
        
        # Skill matching
        required_skills = job_requirements.get('skills', '').lower()
        talent_skills = talent_profile.get('Skills', '').lower()
        
        for skill in required_skills.split(','):
            if skill.strip() in talent_skills:
                score += SKILL_MATCH_WEIGHT
        
        # Location matching
        job_location = job_requirements.get('location', '').lower()
        talent_location = talent_profile.get('Country', '').lower()
        
        if job_location in talent_location or talent_location in job_location:
            score += LOCATION_MATCH_WEIGHT
        
        # Budget matching
        try:
            job_budget = float(job_requirements.get('budget', 0))
            talent_rate = float(talent_profile.get('Monthly Rate', 0))
            
            if talent_rate <= job_budget * 1.3:
                score += BUDGET_MATCH_WEIGHT
        except:
            pass
        
        # Content vertical matching
        job_content = job_requirements.get('content_type', '').lower()
        talent_content = talent_profile.get('Content Verticals', '').lower()
        
        if job_content in talent_content:
            score += CONTENT_MATCH_WEIGHT
        
        # Software matching
        required_software = job_requirements.get('software', '').lower()
        talent_software = talent_profile.get('Software', '').lower()
        
        for software in required_software.split(','):
            if software.strip() in talent_software:
                score += SOFTWARE_MATCH_WEIGHT
        
        # AI analysis for high-scoring candidates
        if score > MIN_SCORE_FOR_AI_ANALYSIS:
            try:
                talent_description = talent_profile.get('Profile Description', '')
                job_skills = job_requirements.get('skills', '')
                
                ai_score = self.gemini_service.analyze_personality_fit(
                    talent_description, job_skills
                )
                
                score += ai_score * AI_ANALYSIS_WEIGHT
                
            except Exception as e:
                pass
        
        return score 
