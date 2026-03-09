function addMessage(text, sender) {
  const chatBox = document.getElementById("chatBox");
  const msg = document.createElement("div");
  msg.className = "message " + sender;
  msg.innerText = text;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function addThinking() {
  const chatBox = document.getElementById("chatBox");
  const think = document.createElement("div");
  think.className = "message bot";
  think.id = "thinkingMsg";
  think.innerHTML = `
    <div class="thinking">
      <img src="${logoPath}" class="spin-logo">
      Thinking...
    </div>
  `;
  chatBox.appendChild(think);
}

function removeThinking() {
  const think = document.getElementById("thinkingMsg");
  if (think) think.remove();
}

async function sendMessage() {
  const input = document.getElementById("userInput");
  const text = input.value.trim();
  if (!text) return;

  addMessage(text, "user");
  input.value = "";
  addThinking();

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text })
    });

    const data = await response.json();
    removeThinking();
    addMessage(data.answer, "bot");

  } catch (error) {
    removeThinking();
    addMessage("Error connecting to server", "bot");
  }
}

document.getElementById("userInput")
  .addEventListener("keypress", function(e) {
    if (e.key === "Enter") sendMessage();
  });