from models.nlp_processor import process_message

def get_chatbot_response(message):
    analysis = process_message(message)

    response = {
        "response": "I'm here for you. Can you tell me more?",
        "intent": analysis.get("intent"),
        "risk": analysis.get("risk"),
        "category": analysis.get("category")
    }
    return response

