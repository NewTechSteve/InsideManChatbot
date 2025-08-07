# app/chatbot.py

from models.nlp_processor import process_message
from app.session_manager import get_session, update_session

RESPONSE_TEMPLATES = {
    "greeting": {
        "low": "Hello! It's good to hear from you. How can I support you today?"
    },
    "emotional_support": {
        "low": "I'm here for you. What's been on your mind lately?",
        "medium": "I'm really sorry you're going through this. Want to share more?",
        "high": "This sounds really serious. Please consider reaching out to a professional. I can help you do that."
    },
    "crisis_support": {
        "low": "I sense some distress. It's okay to feel overwhelmed. Want to talk more?",
        "medium": "That sounds tough. You're not alone — I'm here to listen.",
        "high": "Please speak to a professional immediately. Your life matters, and I can help connect you."
    },
    "general": {
        "low": "I'm here to listen. What's on your mind?",
        "medium": "Let's talk more about what you're feeling. I'm listening.",
        "high": "If you're in distress, I can help you find support. You're not alone."
    }
}

def generate_dynamic_response(intent, risk, session_state):
    if intent == "greeting" and session_state.get("greeted"):
        return "Welcome back. Feel free to talk to me anytime."

    intent_responses = RESPONSE_TEMPLATES.get(intent)
    if intent_responses:
        return intent_responses.get(risk, intent_responses.get("low"))
    return "I'm here for you. Can you tell me more?"


def get_chatbot_response(message: str, session_id: str) -> dict:
    # Get user session (or create one)
    session = get_session(session_id)

    # Analyze message
    analysis = process_message(message)
    intent = analysis.get("intent", "general")
    risk = analysis.get("risk", "low")
    category = analysis.get("category", "general")
    sentiment = analysis.get("sentiment", "neutral")  # <- Add this line

    # Determine if user has been greeted
    if intent == "greeting":
        session["greeted"] = True

    # Generate response
    response_text = generate_dynamic_response(intent, risk, session)

    # Update session history
    update_session(session_id, message, response_text)

    return {
        "response": response_text,
        "intent": intent,
        "risk": risk,
        "category": category,
        "sentiment": sentiment,  # <- Include it in the output
        "thread": session["messages"]
    }
