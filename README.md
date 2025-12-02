# Smart-Roadmap-Recommender-System

🚀 CareerPilot – AI-based Personalized Career & Skills Advisor

CareerPilot is an AI-powered career and skills advisor that helps students and professionals discover suitable career paths, get personalized course recommendations, and build a skill-based learning roadmap.

📌 Features

Career Prediction → Suggests possible career roles based on user skills & interests

Course Recommendations → Uses TF-IDF similarity on skills to suggest best-fit courses (Coursera, Udemy, etc.)

Roadmap Generation → Short-term + long-term skill roadmap for chosen roles

Chatbot Assistant → Interactive Q&A for career guidance

Profile-Based Guidance → Recommendations tailored to each user

🏗️ System Architecture

User Input → Flask Backend (APIs) → Course Dataset + ML Model → JSON Response → Frontend (HTML/CSS/JS UI)

Frontend → HTML, CSS, JS

Backend → Flask (Python) + Scikit-learn (TF-IDF, cosine similarity)

Dataset → courses.csv (curated with Coursera/Udemy links)

APIs → /recommend, /career-predict, Gemini API (planned integration)

📊 Dataset

ONET Dataset → Career roles & required skills

Courses Dataset (courses.csv) → Curated courses with tags (skills, platforms, links)

Gemini API → AI insights for skills & roles (future scope)

⚙️ Installation & Usage
1. Clone Repository
git clone https://github.com/your-username/careerpilot.git
cd careerpilot

2. Backend Setup (Flask)
pip install -r requirements.txt
python main.py


Backend runs at → http://127.0.0.1:5000/

3. Frontend Setup

Open home.html in browser

Frontend JS calls backend APIs (/recommend, /career-predict)

🌍 Deployment

Frontend → Host on GitHub Pages / Netlify / Vercel

Backend → Deploy Flask app on Render / Railway / PythonAnywhere

Update frontend JS API calls with deployed backend URL

📌 Future Scope

Integration with LinkedIn / Job portals

AI Resume Analyzer

Mobile App Version

Multilingual Support (Hindi, English, etc.)

👨‍💻 Team Members

Abhishek Saini
Anubhav Gupta
Anugam Kushwaha
Anuj Singh
Anshika Pandey

📜 License

This project is licensed under the MIT License.
