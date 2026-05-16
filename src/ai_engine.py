import random

class AIEngine:
    def __init__(self):
        self.strengths_templates = [
            "The candidate demonstrates a solid foundation in {skills}.",
            "Notable expertise in {skills} aligns well with the core requirements.",
            "Strong technical alignment detected with proficiency in {skills}.",
            "The resume highlights advanced knowledge of {skills}, which is a key asset for this role."
        ]
        
        self.gaps_templates = [
            "However, there is a lack of explicit mention of {missing_skills}.",
            "To better align with the role, the candidate could strengthen their profile in {missing_skills}.",
            "Missing keywords such as {missing_skills} were noted in the analysis.",
            "Development in {missing_skills} would significantly improve the candidate's fit."
        ]
        
        self.overall_templates = [
            "Based on the semantic analysis, this candidate is a {match_type} match.",
            "AI assessment suggests a {match_type} potential for this position.",
            "Overall, the candidate's profile is {match_type} for the specified job description."
        ]

    def generate_insight(self, matched_skills, missing_skills, score):
        # Determine match type
        if score > 0.8:
            match_type = "High-Quality"
        elif score > 0.5:
            match_type = "Strong"
        elif score > 0.3:
            match_type = "Potential"
        else:
            match_type = "Low"

        # Generate strengths
        if matched_skills:
            skills_str = ", ".join(matched_skills[:3])
            strength = random.choice(self.strengths_templates).format(skills=skills_str)
        else:
            strength = "No direct skill matches were identified in the primary analysis."

        # Generate gaps
        if missing_skills:
            missing_str = ", ".join(missing_skills[:3])
            gap = random.choice(self.gaps_templates).format(missing_skills=missing_str)
        else:
            gap = "No critical skill gaps were identified; the candidate meets the core technical requirements."

        # Generate overall
        overall = random.choice(self.overall_templates).format(match_type=match_type)

        return f"{overall} {strength} {gap}"
