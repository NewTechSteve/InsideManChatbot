# app/sessions.py

import uuid
from datetime import datetime

# In-memory session store
sessions = {}

def create_session():
    session_id = str(uuid.uuid4())
    sessions[session_id] = {
        "messages": [],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    return session_id

def add_message_to_session(session_id, user_message, bot_response):
    if session_id not in sessions:
        sessions[session_id] = {
            "messages": [],
            "created_at": datetime.utcnow()
        }

    sessions[session_id]["messages"].append({
        "timestamp": datetime.utcnow().isoformat(),
        "user": user_message,
        "bot": bot_response
    })
    sessions[session_id]["updated_at"] = datetime.utcnow()

def get_session(session_id):
    return sessions.get(session_id)

def list_sessions():
    return {
        sid: {
            "messages_count": len(data["messages"]),
            "created_at": data["created_at"].isoformat(),
            "updated_at": data["updated_at"].isoformat()
        }
        for sid, data in sessions.items()
    }

def reset_session(session_id):
    if session_id in sessions:
        sessions[session_id]["messages"] = []
        sessions[session_id]["updated_at"] = datetime.utcnow()
        return True
    return False

def reset_all_sessions():
    sessions.clear()
