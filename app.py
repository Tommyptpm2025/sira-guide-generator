from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace this with your Sira LLM URL (e.g., from ngrok or Render)
SIRA_LLM_URL = "https://sira-llm.onrender.com"

@app.route("/generate", methods=["POST"])
def generate_guide():
    data = request.get_json()
    prompt = data.get("prompt", "")
    sira_response = requests.post(SIRA_LLM_URL, json={"prompt": prompt})
    
    if sira_response.status_code == 200:
        return jsonify({"guide": sira_response.json().get("response")})
    else:
        return jsonify({"error": "Failed to generate guide"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
