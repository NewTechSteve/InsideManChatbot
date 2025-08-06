 # ⚙ InsideMan Setup Guide (Local Dev)

## 🔧 Prerequisites

- Python 3.9+
- pip
- Virtualenv
- Git (optional)

## 📦 Step-by-Step

### 1. Clone or Navigate to Your Folder
```bash
cd D:\Productions\InsideMan\InsideManChatbot
```
---
# ⚙️ InsideMan Chatbot – Setup Guide

Welcome to the InsideMan chatbot backend setup guide. This guide walks you through installing dependencies, configuring your environment, and running the chatbot locally or in production.

---

## 📁 Project Structure (Backend)
```
InsideManChatbot/
└── backend/
├── app/ # Flask app logic
├── models/ # NLP logic
├── training/ # Training scripts (future)
├── data/ # Sample inputs
├── tests/ # Unit tests
├── docs/ # Documentation
├── run.py # Entry point
├── requirements.txt # Python dependencies
└── .env # Environment variables
```

---

## 🧰 Prerequisites

- ✅ Python 3.10+ (Install from [python.org](https://www.python.org/downloads/))
- ✅ pip (usually included with Python)
- ✅ Git (optional, for version control)

> 💡 You can verify installation with:
```bash
python --version
pip --version
```
## 🔧 Step 1 – Set Up Virtual Environment (Recommended)
Use a virtual environment to avoid dependency issues.


### Navigate to backend folder
```
cd InsideManChatbot/backend
```

### Create virtual environment
```
python -m venv venv
```

### Activate it (Windows)
```
venv\Scripts\activate
```

### (macOS/Linux)
```
source venv/bin/activate
```

## 📦 Step 2 – Install Dependencies
```
pip install -r requirements.txt
```
If requirements.txt is not yet filled, start with:


*Flask*
You can later add:


*spacy*
scikit-learn
transformers

## 🗝️ Step 3 – Environment Variables
Create a .env file in backend/:
```
FLASK_ENV=development
SECRET_KEY=supersecretkey123
DEBUG=True
```
You can add more keys later (like API keys, DB settings).

## 🚀 Step 4 – Run the App (Development Mode)
Make sure you're in the backend/ directory and your virtual environment is activated.
```
python run.py
```
You should see something like:

```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
## 🧪 Step 5 – Test the Chat Endpoint
Use Postman, cURL, or a simple Python script to test:

Example Request
```c
curl -X POST http://127.0.0.1:5000/chat \
     -H "Content-Type: application/json" \
     -d "{\"message\": \"I feel so alone\"}"
```
You should get a response like:

```json

{
  "response": "I'm really sorry you're feeling this way. You're not alone.",
  "intent": "emotional_support",
  "risk": "medium"
}
```
## 🧪 Step 6 – Run Tests
If tests are defined (in tests/test_chatbot.py):

```python
python -m unittest discover tests
```

## 📤 Deployment (Optional Later Step)
Deployment on HostAfrica (via cPanel or VPS) may use:
```python
flask run (for dev/testing)
```
- Gunicorn + WSGI (wsgi.py or passenger_wsgi.py)

- Docker (if supported)

- Setup your production .env separately

- SSL and security headers recommended.

## 🧹 Maintenance Tips
Keep requirements.txt updated:

```
pip freeze > requirements.txt
```
Use Git to version control:

```
git init
git add .
git commit -m "Initial commit"
```
- Back up .env securely (never push to GitHub)

## 🙋 Need Help?
Reach out to the Realtec dev team, or contact the project maintainer at:

📧 [your_email@realtecsysolution.co.ke]
🌐 https://realtecsysolution.co.ke/

## ✅ Summary
Task	Command
Create venv	python -m venv venv
Activate venv (Windows)	venv\Scripts\activate
Install dependencies	pip install -r requirements.txt
Run the app	python run.py
Test chatbot endpoint	Use Postman or cURL
Run tests	python -m unittest discover tests

## 🚀 You're ready to build!
This guide will evolve as the chatbot evolves (especially as training and database come in). Keep it updated as needed.


---
