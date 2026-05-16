import re
import spacy
from spacy.matcher import PhraseMatcher

class SkillExtractor:
    def __init__(self):
        # Initial common skills list (can be expanded)
        self.skills_db = [
            'Python', 'Java', 'C++', 'JavaScript', 'React', 'Angular', 'Vue', 'Node.js',
            'SQL', 'NoSQL', 'MongoDB', 'PostgreSQL', 'AWS', 'Azure', 'GCP', 'Docker',
            'Kubernetes', 'Machine Learning', 'Deep Learning', 'NLP', 'Data Science',
            'Pandas', 'NumPy', 'Scikit-Learn', 'TensorFlow', 'PyTorch', 'Tableau',
            'Power BI', 'Excel', 'Project Management', 'Agile', 'Scrum', 'Git',
            'Linux', 'Cybersecurity', 'Cloud Computing', 'HTML', 'CSS', 'Flask', 'Django'
        ]
        
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except:
            # Fallback if model not downloaded
            self.nlp = None
            print("Warning: spaCy model 'en_core_web_sm' not found. Using regex fallback.")

        self.matcher = None
        if self.nlp:
            self.matcher = PhraseMatcher(self.nlp.vocab)
            patterns = [self.nlp.make_doc(skill) for skill in self.skills_db]
            self.matcher.add("SKILL", patterns)

    def extract_skills(self, text):
        if not text:
            return []
            
        skills_found = set()
        
        if self.nlp and self.matcher:
            doc = self.nlp(text)
            matches = self.matcher(doc)
            for match_id, start, end in matches:
                skills_found.add(doc[start:end].text)
        else:
            # Simple Regex Fallback
            for skill in self.skills_db:
                if re.search(r'\b' + re.escape(skill) + r'\b', text, re.IGNORECASE):
                    skills_found.add(skill)
                    
        return list(skills_found)

    def identify_missing_skills(self, resume_skills, jd_skills):
        resume_skills_lower = [s.lower() for s in resume_skills]
        missing = [skill for skill in jd_skills if skill.lower() not in resume_skills_lower]
        return missing

    def identify_matched_skills(self, resume_skills, jd_skills):
        resume_skills_lower = [s.lower() for s in resume_skills]
        matched = [skill for skill in jd_skills if skill.lower() in resume_skills_lower]
        return matched
