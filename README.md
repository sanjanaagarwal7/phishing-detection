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

1. Clone the repository<br><br>
git clone https://github.com/your-username/phishing-url-detector.git<br>
cd phishing-url-detector<br><br>

2. Train the Model (Python)<br><br>
cd train_model<br>
python main.py<br><r>

3. Start the Backend Server<br><br>
cd ../backend<br>
npm install<br>
node index.js<br><br>

4. Start the Frontend (React)<br><br>
cd ../frontend<br>
npm install<br>
npm start<br><br>

5. The frontend displays:<br><br>

   ✅ Site is Safe (for label 0)<br>

   ⚠️ Phishing Detected (for label 1)<br>

   🛑 Error (if something goes wrong)<br>

![Screenshot 2025-05-16 150825](https://github.com/user-attachments/assets/2c5487b3-8222-452d-9e07-a5ce1f9bcb08)
![Screenshot 2025-05-16 150903](https://github.com/user-attachments/assets/e76352f4-aaec-45c6-bdeb-f36ff7910ca9)
![Screenshot 2025-05-16 150945](https://github.com/user-attachments/assets/7f363596-8092-4dfb-a2ee-6ad47f90edbb)








