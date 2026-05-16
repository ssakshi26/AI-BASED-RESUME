class Matcher:
    def __init__(self, vectorizer, skill_extractor, ai_engine):
        self.vectorizer = vectorizer
        self.skill_extractor = skill_extractor
        self.ai_engine = ai_engine

    def process(self, resume_text, jd_text):
        # 1. Get embeddings
        resume_emb = self.vectorizer.get_embeddings(resume_text)
        jd_emb = self.vectorizer.get_embeddings(jd_text)
        
        # 2. Compute similarity
        base_score = self.vectorizer.compute_similarity(resume_emb, jd_emb)
        
        # 3. Skill Extraction
        resume_skills = self.skill_extractor.extract_skills(resume_text)
        jd_skills = self.skill_extractor.extract_skills(jd_text)
        
        # 4. Refine Score based on skills
        matched_skills = self.skill_extractor.identify_matched_skills(resume_skills, jd_skills)
        missing_skills = self.skill_extractor.identify_missing_skills(resume_skills, jd_skills)
        
        # Skill bonus: boost score based on matched skills ratio
        skill_score = 0
        if jd_skills:
            skill_score = len(matched_skills) / len(jd_skills)
        
        # Combined score (weighted)
        final_score = (base_score * 0.7) + (skill_score * 0.3)
        
        # 5. Generate AI Insight
        insight = self.ai_engine.generate_insight(matched_skills, missing_skills, final_score)
        
        return {
            "score": round(final_score * 100, 2),
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "insight": insight,
            "all_skills": resume_skills
        }
