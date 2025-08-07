# app/chatbot.py

from models.nlp_processor import process_message

# Predefined response templates based on intent and risk
RESPONSE_TEMPLATES = {
    "emotional_support": {
        "low": "I'm here for you. What's been on your mind lately?",
        "medium": "I'm really sorry you're going through this. Would you like to talk more about it?",
        "high": "This sounds serious. Please consider reaching out to a professional, or I can help guide you to one."
    },
    "crisis_support": {
        "low": "I sense some distress. It's okay to feel overwhelmed sometimes. Want to talk more?",
        "medium": "I'm really concerned about what you're going through. You're not alone, and I'm here to listen.",
        "high": "It’s important you speak to a professional immediately. You're not alone, and your life matters. I can help you find support now."
    },
    "general": {
        "low": "Hi there! I'm here to listen. What would you like to talk about?",
        "medium": "Let's talk more about what you're feeling. I'm listening.",
        "high": "If you’re in distress, please don’t hesitate to reach out for help. I can assist you in finding someone."
    },
    "greeting": {
        "low": "Hello there. How are you feeling today?",
        "medium": "Hi again. How can I support you today?",
        "high": "Hey, I'm here for you. How are you really feeling?"
    }
}

def generate_dynamic_response(intent: str, risk: str) -> str:
    """
    Dynamically generates a chatbot response based on intent and risk level.
    Falls back to a general response if no specific mapping found.
    """
    intent_responses = RESPONSE_TEMPLATES.get(intent)

    if intent_responses:
        return intent_responses.get(risk, intent_responses.get("low"))

    # Fallback default
    return "I'm here for you. Can you tell me more?"


def get_chatbot_response(message: str) -> dict:
    """
    Main chatbot function that receives a message,
    analyzes it, and returns a structured response.
    """
    analysis = process_message(message)

    intent = analysis.get("intent", "general")
    risk = analysis.get("risk", "low")
    category = analysis.get("category", "general")

    response_text = generate_dynamic_response(intent, risk)

    return {
        "response": response_text,
        "intent": intent,
        "risk": risk,
        "category": category
    }
