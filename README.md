# 🔐 Phishing URL Detection Web App

A web-based application that detects whether a given URL is **safe** or **phishing** using a trained machine learning model.

---

## 📌 Features

- ✅ Detects phishing and legitimate websites from URLs
- 🧠 Trained with 500k+ real phishing URLs
- ⚙️ Full-stack: React (frontend), Express.js (backend), Python (ML model)
- 💾 Model saved and reused with `pickle`
- 🌐 REST API integration via Axios

---

## 🧠 Tech Stack

| Layer       | Tech Used              |
|-------------|------------------------|
| Frontend    | React.js               |
| Backend     | Node.js + Express.js   |
| ML Model    | Python + scikit-learn  |
| Data        | `phishing_site_urls.csv` |
| Communication | Axios (HTTP)         |

---

## 🚀 Getting Started

Follow these steps to run the project locally:

---

### 1.Clone the repository

```bash
git clone https://github.com/your-username/phishing-url-detector.git
cd phishing-url-detector

### 2.Train the Model (Python)
cd train_model
python main.py

### 3.Start the Backend Server
cd ../backend
npm install
node index.js

### 4.Start the Frontend (React)
cd ../frontend
npm install
npm start

## The frontend displays:

✅ Site is Safe (for label 0)

⚠️ Phishing Detected (for label 1)

🛑 Error (if something goes wrong)








