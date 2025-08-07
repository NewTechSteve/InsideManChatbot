# app/session_manager.py

# Temporary in-memory session store (later replace with Redis, DB, etc.)
SESSIONS = {}

def get_session(session_id):
    if session_id not in SESSIONS:
        SESSIONS[session_id] = {
            "messages": [],
            "greeted": False
        }
    return SESSIONS[session_id]

def update_session(session_id, user_message, bot_response):
    session = get_session(session_id)
    session["messages"].append({
        "user": user_message,
        "bot": bot_response
    })
