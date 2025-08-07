const chatbox = document.getElementById('chatbox');
const input = document.getElementById('messageInput');
let sessionId = null;

function appendMessage(content, sender, labels = {}) {
  const msgDiv = document.createElement('div');
  msgDiv.className = `message ${sender}`;
  
  msgDiv.innerHTML = `<strong>${sender === 'user' ? 'You' : 'Bot'}:</strong><br>${content}`;
  
  if (sender === 'bot' && Object.keys(labels).length > 0) {
    msgDiv.innerHTML += `
      <div class="labels">
        <strong>Intent:</strong> ${labels.intent} |
        <strong>Risk:</strong> ${labels.risk} |
        <strong>Category:</strong> ${labels.category} |
        <strong>Sentiment:</strong> ${labels.sentiment?.label || 'unknown'} (${labels.sentiment?.score?.toFixed(2) || ''})
      </div>
    `;
  }

  chatbox.appendChild(msgDiv);
  chatbox.scrollTop = chatbox.scrollHeight;
}

function sendMessage() {
  const message = input.value.trim();
  if (!message) return;

  appendMessage(message, 'user');
  input.value = '';

  const payload = { message };
  if (sessionId) {
    payload.session_id = sessionId;
  }

  fetch('http://127.0.0.1:5000/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  })
  .then(res => res.json())
  .then(data => {
    // Store session ID if this is the first interaction
    if (!sessionId) {
      sessionId = data.session_id;
    }

    const botResponse = data.response;
    appendMessage(botResponse.response, 'bot', {
      intent: botResponse.intent,
      risk: botResponse.risk,
      category: botResponse.category,
      sentiment: botResponse.sentiment
    });
  })
  .catch(err => {
    appendMessage("⚠️ Could not reach chatbot. Is the backend running?", 'bot');
    console.error(err);
  });
}

function resetSession() {
  if (!session_id) return;
  fetch(`http://127.0.0.1:5000/session/${session_id}/reset`, {
    method: 'POST'
  })
  .then(() => {
    chatbox.innerHTML = '';
    appendMessage("Session reset. You may start over.", 'bot');
  });
}

function startNewSession() {
  session_id = null;
  chatbox.innerHTML = '';
  appendMessage("Started a new session. Type to begin.", 'bot');
}
