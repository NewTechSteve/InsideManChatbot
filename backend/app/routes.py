# app/routes.py

from flask import Blueprint, request, jsonify
from app.chatbot import get_chatbot_response
from app.sessions import (
    create_session, add_message_to_session,
    get_session, list_sessions, reset_session, reset_all_sessions
)

main = Blueprint('main', __name__)

@main.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    session_id = data.get("session_id")

    if not session_id:
        session_id = create_session()

    bot_response = get_chatbot_response(message, session_id)

    add_message_to_session(session_id, message, bot_response["response"])

    return jsonify({
        "session_id": session_id,
        "response": bot_response
    })

@main.route("/sessions", methods=["GET"])
def get_sessions():
    return jsonify(list_sessions())

@main.route("/session/<session_id>", methods=["GET"])
def get_session_by_id(session_id):
    session = get_session(session_id)
    if session:
        return jsonify(session)
    return jsonify({"error": "Session not found"}), 404

@main.route("/session/<session_id>/reset", methods=["POST"])
def reset_session_by_id(session_id):
    if reset_session(session_id):
        return jsonify({"message": f"Session {session_id} reset successfully."})
    return jsonify({"error": "Session not found"}), 404

@main.route("/sessions/reset_all", methods=["POST"])
def reset_all():
    reset_all_sessions()
    return jsonify({"message": "All sessions cleared."})
