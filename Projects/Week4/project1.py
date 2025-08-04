#  Project 1: Resume Ranker (File I/O + String Matching)

#  Concepts Covered:
# File reading (.txt files as resumes)
# String matching with keywords
# Ranking logic
# os module (optional) to loop through multiple files

# Resume Ranker

import os

# Define job-specific keywords
keywords = ['python', 'ml', 'sql', 'pandas', 'tensorflow']

def score_resume(text):
    text = text.lower()
    return sum(1 for kw in keywords if kw in text)

# Assume resumes are in './resumes/' folder as .txt files
folder = "./resumes"
resume_scores = {}

for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        with open(os.path.join(folder, filename), 'r') as f:
            content = f.read()
            score = score_resume(content)
            resume_scores[filename] = score

# Sort by score
sorted_resumes = sorted(resume_scores.items(), key=lambda x: x[1], reverse=True)

print("\nResume Rankings:")
for name, score in sorted_resumes:
    print(f"{name}: {score}/5")
