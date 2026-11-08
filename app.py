
from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "ɹɐʇsᴉɐꓤ AI SERVER ONLINE"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(silent=True) or {}
        message = data.get("message", "").strip()

        if not message:
            return jsonify({"reply": "Apna message likho."}), 400

        api_key = os.environ.get("OPENAI_API_KEY")

        if not api_key:
            return jsonify({
                "reply": "API setup pending hai."
            }), 503

        client = OpenAI(api_key=api_key)

        response = client.responses.create(
            model=os.environ.get("OPENAI_MODEL", "gpt-5.5"),
            instructions=(
                "You are ɹɐʇsᴉɐꓤ AI. "
                "Reply in Hindi or Hinglish when appropriate. "
                "Help with general knowledge, anime, gaming "
                "and technology. Be accurate and admit uncertainty."
            ),
            input=message
        )

        return jsonify({"reply": response.output_text})

    except Exception:
        app.logger.exception("Chat error")
        return jsonify({
            "reply": "Server error. Please try again."
        }), 500

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
          )
      
