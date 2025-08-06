 # 🛣 InsideMan Chatbot Roadmap

## Summary

## ✅ Stage 1: Foundation (Current)
- [x] Define purpose, features
- [x] Project structure + documentation
- [ ] Basic chatbot input/output loop (Flask)
- [ ] Initial NLP categorization (manual)
- [ ] Local testing

## 🔜 Stage 2: Intent & Categorization
- Define common user intents (e.g. loneliness, stress, heartbreak)
- Create & label training data
- Train small classifier
- Add intent-based routing to responses

## 🔜 Stage 3: Emotion & Risk Detection
- Detect emotional intensity
- Assign risk levels
- Trigger safety messages or professional advice

## 🔜 Stage 4: Real-World Help
- Connect to real professionals (API or database)
- Suggest forums or mental health groups
- Build out frontend for live users

## 🔜 Stage 5: Production
- Prepare for deployment (HostAfrica cPanel)
- Add HTTPS, security, and logs

# Detailed

# 🛣️ InsideMan Chatbot – Full Roadmap (Agile Sprints)

## 📌 Overview

This roadmap outlines the entire development process of the InsideMan chatbot — from MVP (basic rule-based support bot) to a full-scale, AI-enhanced, production-ready emotional support platform.

We follow an **Agile Sprint-based approach**, where each sprint = 2 weeks.

---

## 🏁 Sprint 0 — Project Kickoff & Planning (Week 1)

- ✅ Define chatbot goals, user needs, emotional tone
- ✅ Identify target personas (hurting men, isolated individuals, etc.)
- ✅ Choose tech stack (Python, Flask, spaCy, SQLite)
- ✅ Set up project folder structure
- ✅ Write documentation: `README.md`, `setup_guide.md`, `architecture.md`, `roadmap.md`
- ✅ Set up version control (Git) and repository
- ✅ Draft initial LICENSE (Proprietary to Realtec)

---

## 🚀 Sprint 1 — MVP Chatbot (Basic Flask App) (Weeks 2–3)

### 🔧 Modules:
- Flask setup with `/chat` route
- Basic chatbot logic in `chatbot.py` (manual keyword-based rules)
- Dummy NLP processor (detect simple categories: grief, heartbreak, loneliness)
- Basic risk flagging (hardcoded rules)
- Logging user inputs

### 🧪 Deliverables:
- Working Flask server on localhost
- Accepts user input and returns supportive responses
- Local test script in `tests/test_chatbot.py`

---

## ⚙️ Sprint 2 — NLP Engine v1 + Categorization (Weeks 4–5)

### 🧠 Modules:
- Integrate `spaCy` NLP pipeline
- Add simple intent detection via rules or keyword patterns
- Categorize messages into tags (e.g., “grief”, “breakup”, “stress”)
- Refactor chatbot logic to be modular

### 🧪 Deliverables:
- Categorized user input
- Updated `models/nlp_processor.py`
- More relevant replies based on topic
- Test cases for intents

---

## 🧠 Sprint 3 — Training v1: Basic Intent Classifier (Weeks 6–7)

### 🎯 Goal:
Train a lightweight intent classification model to replace hardcoded rules

### 📦 Tasks:
- Create `training/training_data.json` with labeled inputs
- Build `preprocess.py` to clean and prepare data
- Train classifier using scikit-learn or spaCy text categorizer
- Update chatbot to use prediction results

### 🧪 Deliverables:
- Trained intent model (pickle or `.pt`)
- Live intent predictions
- Tests showing >80% accuracy on sample inputs

---

## 🚨 Sprint 4 — Emotion & Risk Assessment (Weeks 8–9)

### 🧠 Modules:
- Integrate sentiment/emotion detection (via transformers or rule-based)
- Create scoring for emotional intensity and risk (low, medium, high)
- Add high-risk response template (e.g., recommend professional help)
- Refactor chatbot to separate emotion + intent logic

### 🧪 Deliverables:
- NLP module assigns emotion + risk per input
- Real-time risk flagging
- Safe failover for high-risk inputs

---

## 👨‍⚕️ Sprint 5 — Professional Referral System (Weeks 10–11)

### 🧩 Modules:
- Add referrals.json (list of partner professionals)
- Logic to refer based on category/risk
- Optional: auto-email or database log
- Optional: collect anonymized user session data

### 🧪 Deliverables:
- If high-risk → recommend specific help
- Simulate referral via logging or console

---

## 🌐 Sprint 6 — Web Interface + Hosting Prep (Weeks 12–13)

### 🌍 Frontend:
- Basic HTML/JS chat interface
- Integrate with Flask `/chat` API
- Show past messages
- Optional: connect frontend via AJAX/Fetch

### ☁️ Hosting Prep:
- Prepare app for cPanel deployment
- Test with SQLite → MySQL transition
- Add `.htaccess` / WSGI file if needed

### 🧪 Deliverables:
- Working frontend
- Hosted version (test server)
- Readme instructions for deployment

---

## 🧪 Sprint 7 — Testing, Validation & Feedback (Weeks 14–15)

### 🔍 Tasks:
- Write unit & integration tests
- Test NLP models for bias and edge cases
- Get internal team/user feedback
- Improve response tone and empathy

### 🧪 Deliverables:
- >85% unit test coverage
- Reviewed and improved responses
- Final validation by mental health advisors (if available)

---

## 🚀 Sprint 8 — Full Deployment + Polishing (Week 16)

### 🌟 Final Deliverables:
- Fully working chatbot (rule + model based)
- Hosted on HostAfrica via cPanel
- All routes, logs, referrals functional
- All documentation updated
- License clearly stated (Proprietary to Realtec)
- Optional: create landing page

---

## 📅 Timeline Summary

| Sprint | Week | Focus                                |
|--------|------|--------------------------------------|
| 0      | 1    | Planning & Docs                      |
| 1      | 2–3  | Flask MVP + Basic Bot                |
| 2      | 4–5  | NLP v1 + Categorization              |
| 3      | 6–7  | Train Intent Classifier              |
| 4      | 8–9  | Emotion + Risk Scoring               |
| 5      | 10–11| Referrals Module                     |
| 6      | 12–13| Frontend + Hosting Prep              |
| 7      | 14–15| Testing + Feedback                   |
| 8      | 16   | Final Deployment                     |

---

## 🔚 Post-Launch: Future Features (Beyond MVP)

- User login & anonymous accounts
- Session tracking (with consent)
- Voice input/output
- Language support
- Mobile version
- Mental health forum/community integration

---

## 🧾 Notes

- Each sprint includes documentation updates
- Agile stand-ups/reviews are recommended weekly
- All training models stored in `training/` folder
