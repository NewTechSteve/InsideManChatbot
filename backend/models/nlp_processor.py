from textblob import TextBlob
import spacy
import re

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Expanded and flexible keyword-based intent detection
INTENT_KEYWORDS = {
    "suicidal_thoughts": [
        "kill myself", "want to die", "end my life", "end it all", "die",
        "not worth living", "give up", "can't go on", "hopeless", "worthless",
        "no point", "can't take it anymore", "end everything", "ending it", "done with life"
    ],
    "emotional_support": [
        "sad", "depressed", "anxious", "lonely", "overwhelmed", "tired", "numb",
        "lost", "broken", "angry", "hurt", "heartbroken"
    ],
    "greeting": ["hello", "hi", "hey", "good morning", "good evening", "what's up"]
}

INTENT_RISK_MAPPING = {
    "suicidal_thoughts": "high",
    "emotional_support": "medium",
    "greeting": "low",
    "general": "low"
}

CATEGORY_MAPPING = {
    "suicidal_thoughts": "emergency",
    "emotional_support": "mental_health",
    "greeting": "general",
    "general": "general"
}

def normalize_text(text):
    """Lowercase and remove punctuation."""
    return re.sub(r'[^a-zA-Z\s]', '', text.lower())

def analyze_sentiment(message):
    """
    Analyze sentiment using TextBlob and keyword boosting.
    Returns polarity and label.
    """
    blob = TextBlob(message)
    polarity = blob.sentiment.polarity

    # Suicide/self-harm related keywords override sentiment
    crisis_keywords = ["die", "kill", "worthless", "end it", "give up", "suicide", "can't go on", "no reason", "hopeless"]
    lowered = message.lower()

    # Boost logic for short but high-risk messages
    if any(kw in lowered for kw in crisis_keywords):
        return {"score": -1.0, "label": "negative"}

    if polarity > 0.3:
        label = "positive"
    elif polarity < -0.3:
        label = "negative"
    else:
        label = "neutral"

    return {"score": polarity, "label": label}

def extract_entities(message):
    """
    Extract named entities using spaCy.
    Returns a list of entity dictionaries.
    """
    doc = nlp(message)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return entities

def detect_intent(message):
    """
    Match keywords to detect intent.
    Allows for multiple overlapping intents (e.g., greeting + distress).
    """
    normalized = normalize_text(message)
    detected_intents = set()

    for intent, keywords in INTENT_KEYWORDS.items():
        for keyword in keywords:
            if keyword in normalized:
                detected_intents.add(intent)

    if not detected_intents:
        return ["general"]

    return list(detected_intents)

def process_message(message: str) -> dict:
    """
    Processes message and returns structured analysis.
    Includes intent(s), risk, category, sentiment, and NER.
    """
    intents = detect_intent(message)
    sentiment = analyze_sentiment(message)
    entities = extract_entities(message)

    # Determine primary intent and escalate based on negative sentiment
    if "suicidal_thoughts" in intents:
        primary_intent = "suicidal_thoughts"
    elif "emotional_support" in intents:
        primary_intent = "emotional_support"
    elif "greeting" in intents and len(intents) > 1:
        # Prioritize non-greeting intent
        non_greeting_intents = [i for i in intents if i != "greeting"]
        primary_intent = non_greeting_intents[0]
    elif "greeting" in intents:
        primary_intent = "greeting"
    else:
        primary_intent = "general"

    # Escalate risk if sentiment is strongly negative
    risk = INTENT_RISK_MAPPING.get(primary_intent, "low")
    if sentiment['label'] == "negative" and sentiment['score'] < -0.5:
        if risk == "low":
            risk = "medium"
        elif risk == "medium":
            risk = "high"

    category = CATEGORY_MAPPING.get(primary_intent, "general")

    return {
        "intent": primary_intent,
        "intents_detected": intents,
        "risk": risk,
        "category": category,
        "sentiment": sentiment,
        "entities": entities
    }
