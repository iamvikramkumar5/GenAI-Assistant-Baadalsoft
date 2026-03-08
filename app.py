from flask import Flask, render_template, request, jsonify
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from google import genai
import os

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

# -------- Gemini Client --------
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# -------- Conversation History --------
conversation_history = []

# -------- Load Documents --------
with open("../docs.json") as f:
    documents = json.load(f)

# -------- Chunk Function --------
def chunk_document(text, size=300):
    return [text[i:i+size] for i in range(0, len(text), size)]

# -------- Prepare Chunks --------
chunks_store = []
for doc in documents:
    chunks = chunk_document(doc["content"])
    chunks_store.extend(chunks)

# -------- TF-IDF Vectorizer --------
vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(chunks_store)

# -------- Similarity Search --------
def find_similar_chunks(user_query):
    query_vector = vectorizer.transform([user_query])
    similarities = cosine_similarity(query_vector, doc_vectors)
    top_indices = similarities.argsort()[0][-3:][::-1]
    return [chunks_store[i] for i in top_indices]

# -------- LLM Response --------
def get_llm_response(context, user_message):
    prompt = f"""
You are Baadalsoft AI Assistant.
Answer using ONLY the context below.

Context:
{context}

User Question:
{user_message}
"""
    response = client.models.generate_content(
        model="models/gemini-2.5-flash-lite",
        contents=prompt
    )
    return response.text

# -------- Routes --------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    similar_chunks = find_similar_chunks(user_message)
    context = "\n".join(similar_chunks)

    conversation_history.append({"role": "user", "content": user_message})
    if len(conversation_history) > 10:
        conversation_history.pop(0)

    answer = get_llm_response(context, user_message)
    conversation_history.append({"role": "assistant", "content": answer})

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run()