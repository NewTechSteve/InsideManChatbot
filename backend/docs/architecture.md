# 🏗️ InsideMan Chatbot – System Architecture

## 📌 Overview

InsideMan is an anonymous, emotionally intelligent chatbot designed to help men (and others) who are emotionally hurting. The system is structured with clear modules for input handling, NLP processing, response generation, and future expandability (including machine learning).

The architecture is built using **Flask (Python)** as the backend framework and will evolve from a **rule-based MVP** to a **modular ML/NLP-driven chatbot**.

---

## 🔁 System Workflow (High-Level Flow)
```
[User Input]
↓
[Flask Route: /chat]
↓
[Chatbot Logic (chatbot.py)]
↓
[NLP Processor (Intent + Emotion + Risk)]
↓
[Response Selector]
↓
[JSON Response to Frontend]
```


---

## 📂 Folder Structure (Backend)
```
backend/
│
├── app/ # Flask app logic
│ ├── init.py # App factory
│ ├── routes.py # API routes (e.g., /chat)
│ ├── chatbot.py # Core chatbot logic
│ └── utils.py # Reusable helpers
│
├── models/ # NLP/ML processing modules
│ └── nlp_processor.py # Handles intent/emotion/risk processing
│
├── data/ # Sample inputs, logs, config files
│ └── example_inputs.json
│
├── training/ # ML training pipeline (future)
│ ├── training_data.json
│ ├── preprocess.py
│ └── train_intent_model.py
│
├── tests/ # Unit and integration tests
│ └── test_chatbot.py
│
├── docs/ # Documentation and planning
│ ├── roadmap.md
│ ├── setup_guide.md
│ └── architecture.md
│
├── .env # Environment variables
├── requirements.txt # Project dependencies
└── run.py # Entry point
```

---

## 🧠 NLP/AI Components (Progressive Build)

| Stage | NLP Component            | Implementation       |
|-------|---------------------------|-----------------------|
| 1     | Keyword categorization     | Hardcoded keywords    |
| 2     | Rule-based intent matching | spaCy / manual rules  |
| 3     | Trained intent classifier  | Scikit-learn / spaCy  |
| 4     | Emotion detection          | Transformers / APIs   |
| 5     | Risk scoring               | Custom thresholds     |

All NLP logic lives in:  
`models/nlp_processor.py`

---

## 📬 API Interface

### `POST /chat`
**Input:**
```json
{
  "message": "I feel so alone and tired of everything"
}
```

**Output:**
```json
{
  "response": "I'm really sorry you're feeling this way. You're not alone.",
  "category": "loneliness",
  "intent": "emotional_support",
  "risk": "medium"
}
```
## 🧩 Core Modules Explained
1. app/chatbot.py
* Central logic to:

* Take user message

* Call NLP processor

* Determine response

* Simple routing logic based on intent and risk

2. models/nlp_processor.py
* NLP engine:

* Rule-based or model-based

* Handles:

* Intent classification

* Emotion detection

* Risk analysis

3. training/
- Pipeline for training the intent classifier:

- Labeled data in training_data.json

- Training script using scikit-learn or spaCy

- Future: emotion models (transformers)

## 🧪 Testing Strategy
***Manual:***
* Run run.py

* Use Postman or browser to test /chat

***Automated:***
* Write unit tests in tests/

* Use pytest or Python’s built-in unittest

## ⚙️ Hosting & Deployment (Future)
- Hosted on HostAfrica (cPanel)

- Use flask run or WSGI deployment

- Use .htaccess or passenger_wsgi.py (if needed)

- SQLite → MySQL for production DB

- SSL for HTTPS

## 🔐 Security Considerations
- No user tracking (anonymous by design)

- Log dangerous messages internally for admin review

- Use HTTPS for data security

- Add spam rate limits if exposed to public

## 🌱 Scalability (Future Roadmap)
- Swap out rule-based NLP for transformer models (Hugging Face)

- Add database logging of high-risk chats (with user consent)

- Add professional referral system with dynamic DB/API

- Allow multiple personalities/tones (configurable support voices)

- Multilingual support (via translation APIs or models)

## 🤝 Integration Possibilities
- WhatsApp/Telegram integration (via webhook)

- Discord/Slack chatbot bot

- Integration with licensed therapists/professional database

- Community forum connection (for peer-to-peer support)

## 👷 Maintainer Notes
- Code should remain modular and readable

- NLP and logic must be easy to swap or upgrade

- Training data and model files are versioned

- Keep mental health tone: supportive, never cold or clinical

## 📌 Summary
- Flask app handles input/output

- NLP processor handles understanding

- Chatbot decides response logic

- System is modular, testable, and future-ready

---


