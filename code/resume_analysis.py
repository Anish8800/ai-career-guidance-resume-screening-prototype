"""
AI-Powered Resume Screening & Career Guidance (Prototype)

Author: Anish Wadatkar
Description:
This is an academic prototype that demonstrates how basic
Natural Language Processing (NLP) techniques can be used to
analyze resumes, match skills with job roles, and identify
skill gaps for career guidance.

Note:
This is a rule-based system created for learning purposes
and is not a production-level ATS or AI system.
"""

import re

# -----------------------------
# Job Role Skill Database
# -----------------------------
JOB_ROLES = {
    "Data Analyst": [
        "Python",
        "SQL",
        "Excel",
        "Data Visualization",
        "Statistics",
    ],
    "Software Developer": [
        "Python",
        "Java",
        "Git",
        "Problem Solving",
        "DSA",
    ],
    "AI Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "NLP",
        "Statistics",
    ],
}

# -----------------------------
# Skill Extraction Function
# -----------------------------
def extract_skills(resume_text):
    """
    Extracts known skills from resume text using
    simple keyword matching (regex-based).
    """
    SKILL_SET = [
        "Python",
        "SQL",
        "Excel",
        "Machine Learning",
        "Deep Learning",
        "NLP",
        "Git",
        "Java",
        "Statistics",
        "Data Visualization",
        "DSA",
        "Problem Solving",
    ]

    found_skills = []

    for skill in SKILL_SET:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, resume_text, re.IGNORECASE):
            found_skills.append(skill)

    return list(set(found_skills))


# -----------------------------
# Resume Analysis Function
# -----------------------------
def analyze_resume(resume_text, target_role):
    """
    Compares extracted resume skills with required
    skills for the selected job role.
    """
    extracted_skills = extract_skills(resume_text)
    required_skills = JOB_ROLES.get(target_role, [])

    matched_skills = set(extracted_skills).intersection(required_skills)
    missing_skills = set(required_skills) - set(extracted_skills)

    score = (
        int((len(matched_skills) / len(required_skills)) * 100)
        if required_skills
        else 0
    )

    return {
        "Target Role": target_role,
        "Resume Score": f"{score}%",
        "Matched Skills": sorted(list(matched_skills)),
        "Missing Skills": sorted(list(missing_skills)),
    }


# -----------------------------
# Sample Demo Run
# -----------------------------
if __name__ == "__main__":
    sample_resume_text = """
    I have experience in Python, SQL, and Excel.
    I have worked on data analysis projects involving
    data visualization and basic machine learning.
    """

    target_job_role = "Data Analyst"

    result = analyze_resume(sample_resume_text, target_job_role)

    print("AI Resume Analysis Result")
    print("-" * 30)
    for key, value in result.items():
        print(f"{key}: {value}")
