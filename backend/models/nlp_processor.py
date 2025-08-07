# nlp_processor.py

def process_message(message):
    message = message.lower()

    if any(word in message for word in ["kill myself", "end it all", "suicide", "worthless"]):
        return {"intent": "suicidal_thoughts", "risk": "high", "category": "emergency"}

    if any(word in message for word in ["sad", "depressed", "anxious", "lonely", "alone"]):
        return {"intent": "emotional_support", "risk": "medium", "category": "mental_health"}

    if any(word in message for word in ["hello", "hi", "hey"]):
        return {"intent": "greeting", "risk": "low", "category": "general"}

    return {"intent": "general", "risk": "low", "category": "general"}

