# 🧠 Resume Parser & Classifier

A bilingual resume parser and job-fit classifier built with **Python**, **NLP**, and **Machine Learning**. Designed to extract key skills and predict job roles from resumes written in **English** or **Mandarin**.

---

## 🚀 Features

- 📄 Parses resumes to extract skills and languages  
- 🧠 Classifies resumes into job categories (e.g., Developer, Analyst, Tester)  
- 🗃️ Trained on labeled dataset using TF-IDF + Logistic Regression  
- 🌍 Supports multilingual input (English + Mandarin)  
- 🧩 Modular OOAD design for easy extension

---

## 🛠️ Tech Stack

| Component     | Technology Used         |
|---------------|--------------------------|
| NLP           | Python, scikit-learn     |
| ML Model      | Logistic Regression      |
| Data Handling | pandas, TfidfVectorizer  |
| Language      | English + Mandarin       |

---

## 📦 Folder Structure

resume-parser-classifier/ ├── parser/ # Parsing and classification logic ├── data/ # Sample resumes and training data ├── model/ # Saved ML model └── README.md # Project overview

---

## 🧪 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/resume-parser-classifier.git
   cd resume-parser-classifier
2. **Install dependencies**
   pip install pandas scikit-learn
3. **Train the model**
   python parser/classify.py
4. **Run prediction**
   from parser.classify import predict_resume
text = open('data/sample_resumes/resume1.txt').read()
print(predict_resume(text))
Future Enhancements
🧾 Add PDF/DOCX parsing support

🧪 Integrate spaCy for advanced entity extraction

🌐 Build a web interface with Flask or Streamlit

📊 Add confidence scores and explainable predictions
Author
Samyuktha
License
This project is licensed under the MIT License. Feel free to fork, modify, and share!

---

Let me know if you’d like a sample resume dataset, Streamlit UI, or Dockerfile to containerize it. Want me to zip all 4 projects into a GitHub-ready bundle next?
