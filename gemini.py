from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# --------------------------
# Load CSV safely (FIXED)
# --------------------------
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(BASE_DIR, 'courses.csv')

    courses_df = pd.read_csv(csv_path)

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(courses_df['Skills'])

    print("✅ courses.csv loaded successfully")
except Exception as e:
    print("❌ Error loading courses:", e)
    courses_df = pd.DataFrame()
    tfidf_matrix = None

# --------------------------
# Courses Recommendation API
# --------------------------
@app.route('/recommend', methods=['GET'])
def recommend_courses():
    if courses_df.empty or tfidf_matrix is None:
        return jsonify({'recommendations': []})

    query = request.args.get('query', '')
    if not query:
        return jsonify({'recommendations': []})

    try:
        query_vec = vectorizer.transform([query])
        similarity = cosine_similarity(query_vec, tfidf_matrix)
        top_idx = similarity[0].argsort()[-5:][::-1]

        recommendations = []
        for idx in top_idx:
            recommendations.append({
                "Title of Course": courses_df.iloc[idx]['Title of Course'],
                "Roles": courses_df.iloc[idx]['Roles'],
                "Skills": courses_df.iloc[idx]['Skills'],
                "Platform": courses_df.iloc[idx]['Platform'],
                "URL": courses_df.iloc[idx]['URL']
            })

        return jsonify({'recommendations': recommendations})

    except Exception as e:
        print("❌ Recommendation error:", e)
        return jsonify({'recommendations': []})

# --------------------------
# Career Prediction API
# --------------------------
@app.route('/career-predict', methods=['POST'])
def career_predict():
    data = request.get_json()
    user_input = data.get('user_input', '').lower()

    if not user_input:
        return jsonify({"prediction": "Please provide skills, interests, or role information."})

    keyword_roles = {
        'python': ["Data Scientist", "Machine Learning Engineer", "Backend Developer", "Python Developer", "AI Developer"],
        'java': ["Java Developer", "Software Engineer", "Android Developer", "Fullstack Java Developer"],
        'javascript': ["Frontend Developer", "Fullstack Developer", "Web Developer", "React Developer", "Node.js Developer"],
        'c++': ["C++ Developer", "Game Developer", "Embedded Systems Engineer"],
        'html': ["Frontend Developer", "Web Designer", "UI Developer"],
        'css': ["Frontend Developer", "UI/UX Designer", "Web Designer"],
        'ml': ["Machine Learning Engineer", "AI Researcher", "Data Scientist", "ML Ops Engineer"],
        'ai': ["AI Engineer", "Deep Learning Specialist", "NLP Engineer", "Computer Vision Engineer"],
        'nlp': ["NLP Engineer", "AI Researcher", "Data Scientist"],
        'data': ["Data Analyst", "Data Scientist", "Business Intelligence Analyst", "Data Engineer"],
        'design': ["UI/UX Designer", "Graphic Designer", "Product Designer", "Visual Designer"],
        'graphic': ["Graphic Designer", "Visual Designer", "Motion Graphics Designer"],
        'ui': ["UI Designer", "Frontend Developer", "UX Designer"],
        'ux': ["UX Designer", "UI Designer", "Product Designer"],
        'marketing': ["Digital Marketer", "Content Strategist", "SEO Specialist", "Brand Manager"],
        'finance': ["Financial Analyst", "Investment Banker", "Accountant", "Financial Consultant"],
        'management': ["Project Manager", "Operations Manager", "Product Manager", "Team Lead"],
        'cloud': ["Cloud Engineer", "DevOps Engineer", "AWS Developer"],
        'devops': ["DevOps Engineer", "Cloud Engineer", "Site Reliability Engineer"],
        'qa': ["QA Engineer", "Test Automation Engineer", "Software Tester"],
        'blockchain': ["Blockchain Developer", "Smart Contract Developer", "Crypto Analyst"],
        'iot': ["IoT Engineer", "Embedded Systems Engineer", "Hardware Developer"]
    }

    predicted_roles = []
    for keyword, roles in keyword_roles.items():
        if keyword in user_input:
            predicted_roles.extend(roles)

    if not predicted_roles:
        predicted_roles = ["Software Developer", "Project Manager", "Consultant", "Entrepreneur"]

    predicted_roles = list(dict.fromkeys(predicted_roles))[:6]

    return jsonify({"prediction": ", ".join(predicted_roles)})

# --------------------------
# Root Route (for testing)
# --------------------------
@app.route('/')
def home():
    return "🚀 Smart Roadmap Backend Running Successfully!"

# --------------------------
# Run Flask App (Render FIX)
# --------------------------
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)