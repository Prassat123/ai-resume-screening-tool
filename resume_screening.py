from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

resume = open("sample_resume.txt", "r").read().lower()
job_description = open("job_description.txt", "r").read().lower()

#resume = input("Paste resume text: ").lower()
#job_description = input("Paste job description: ").lower()


documents = [resume, job_description]

vectorizer = CountVectorizer()
matrix = vectorizer.fit_transform(documents)

similarity = cosine_similarity(matrix)
match_score = similarity[0][1] * 100

skills = [
    "python",
    "sql",
    "machine learning",
    "pandas",
    "data analysis",
    "github",
    "communication",
    "excel",
    "power bi"
]

matched_skills = []
missing_skills = []

for skill in skills:
    if skill in resume and skill in job_description:
        matched_skills.append(skill.title())
    elif skill not in resume and skill in job_description:
        missing_skills.append(skill.title())

print("AI Resume Screening Tool")
print("-------------------------")
print("Resume Match Score:", round(match_score, 2), "%")

print("\nMatched Skills:")
for skill in matched_skills:
    print("-", skill)

print("\nMissing Skills:")
for skill in missing_skills:
    print("-", skill)

print("\nRecommendation:")
if match_score >= 70:
    print("Strong Match")
elif match_score >= 40:
    print("Average Match")
else:
    print("Weak Match")