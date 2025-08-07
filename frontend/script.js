const chatbox = document.getElementById('chatbox');
const input = document.getElementById('messageInput');

function appendMessage(content, sender, labels = {}) {
  const msgDiv = document.createElement('div');
  msgDiv.className = `message ${sender}`;
  
  msgDiv.innerHTML = `<strong>${sender === 'user' ? 'You' : 'Bot'}:</strong><br>${content}`;
  
  if (sender === 'bot') {
    msgDiv.innerHTML += `
      <div class="labels">
        <strong>Intent:</strong> ${labels.intent} |
        <strong>Risk:</strong> ${labels.risk} |
        <strong>Category:</strong> ${labels.category}
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

  fetch('http://127.0.0.1:5000/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message })
  })
  .then(res => res.json())
  .then(data => {
    appendMessage(data.response, 'bot', {
      intent: data.intent,
      risk: data.risk,
      category: data.category
    });
  })
  .catch(err => {
    appendMessage("⚠️ Could not reach chatbot. Is the backend running?", 'bot');
    console.error(err);
  });
}
