from flask import Flask, request, jsonify
from flask_cors import CORS
from gensim.models import Word2Vec
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS

model = Word2Vec.load("your_model.model")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "").lower()
    words = message.split()
    
    embeddings = [model.wv[w] for w in words if w in model.wv]
    if not embeddings:
        return jsonify({"reply": "Sorry, I don't understand."})

    mean_vector = np.mean(embeddings, axis=0)
    response_text = f"Received your message! Mean embedding length: {len(mean_vector)}"

    return jsonify({"reply": response_text})

if __name__ == "__main__":
    app.run(debug=True)
