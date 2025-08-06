from flask import Blueprint, request, jsonify
from app.chatbot import get_chatbot_response

main = Blueprint('main', __name__)

@main.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    response = get_chatbot_response(message)
    return jsonify(response)

