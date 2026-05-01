# 🚀 Smart Roadmap Recommender System (CareerPilot)

## 🎯 AI-Based Personalized Career & Skills Advisor

**CareerPilot** is an AI-powered platform designed to help students and professionals discover suitable career paths, receive personalized course recommendations, and build structured learning roadmaps based on their skills and interests.

---

## ✨ Features

* 🔮 **Career Prediction**
  Suggests suitable career roles based on user skills and interests.

* 📚 **Course Recommendations**
  Uses **TF-IDF + cosine similarity** to recommend best-fit courses (Coursera, Udemy, etc.).

* 🗺️ **Roadmap Generation**
  Provides structured short-term and long-term learning paths.

* 🤖 **Chatbot Assistant**
  Interactive chatbot for career-related queries and guidance.

* 👤 **Profile-Based Guidance**
  Personalized recommendations tailored to individual users.

---

## 🏗️ System Architecture

```
User Input 
   ↓
Frontend (HTML/CSS/JS)
   ↓
Flask Backend (API)
   ↓
ML Model + Dataset
   ↓
JSON Response
   ↓
Frontend Display
```

---

## 🛠️ Tech Stack

### 💻 Frontend

* HTML
* CSS
* JavaScript

### ⚙️ Backend

* Flask (Python)
* Scikit-learn (TF-IDF, Cosine Similarity)

### 📊 Dataset

* ONET Dataset (Career roles & skills)
* courses.csv (Curated course dataset)

### 🔌 APIs

* `/recommend` → Course suggestions
* `/career-predict` → Career prediction
* Gemini API (Planned)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Abhishek-Saini2211677/Smart-Roadmap-Recommender-System.git
cd Smart-Roadmap-Recommender-System
```


---

### 2️⃣ Backend Setup (Flask)

```bash
pip install -r requirements.txt
python main.py
```

📍 Backend runs at:
http://127.0.0.1:5000/

---

### 3️⃣ Frontend Setup

* Open `home.html` in your browser
* Frontend connects to backend APIs

---

## 🌍 Deployment

### Frontend

* GitHub Pages
* Netlify
* Vercel

### Backend

* Render
* Railway
* PythonAnywhere

⚠️ Update API URLs in frontend after deployment.

---

## 📈 Future Enhancements

* 🔗 LinkedIn / Job Portal Integration
* 📄 AI Resume Analyzer
* 📱 Mobile Application
* 🌐 Multilingual Support (Hindi, English, etc.)

---

## 👨‍💻 Team Members

* Abhishek Saini
* Anubhav Gupta
* Anugam Kushwaha
* Anuj Singh

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Contribution

Feel free to fork this repository, raise issues, and submit pull requests to improve the project!

---
