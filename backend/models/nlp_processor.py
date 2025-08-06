def process_message(message):
    # Placeholder for now. This will be replaced with actual NLP later.
    if "alone" in message.lower():
        return {
            "intent": "emotional_support",
            "risk": "medium",
            "category": "loneliness"
        }
    return {
        "intent": "general",
        "risk": "low",
        "category": "general"
    }

