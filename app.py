from flask import Flask, render_template, request, jsonify
import requests
import re
from dotenv import load_dotenv
app = Flask(__name__)
import os
HF_API_URL = "https://api-inference.huggingface.co/models/saniaverma/tinyllama-colorist-v0"
HF_TOKEN = os.getenv("HF_TOKEN") # Replace with your real token

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_color():
    try:
        user_input = request.json.get("prompt", "")
        prompt = f"<|user|>\n{user_input}</s>\n<|assistant|>"
        payload = {"inputs": prompt}

        response = requests.post(HF_API_URL, headers=headers, json=payload)
        result = response.json()
        print("Result from /generate:", result)

        if not result or not isinstance(result, list) or "generated_text" not in result[0]:
            return jsonify({"hex": "#888888"})  # fallback

        match = re.search(r"#(?:[A-Fa-f0-9]{6})", result[0]["generated_text"])
        hex_code = match.group(0) if match else "#888888"

        return jsonify({"hex": hex_code})

    except Exception as e:
        print("Error in /generate:", e)
        return jsonify({"error": str(e)}), 500

@app.route("/palette", methods=["POST"])
def generate_palette():
    user_input = request.json.get("prompt", "")
    colors = []

    for i in range(6):  # Generate 6 different colors
        prompt = f"<|user|>\n{user_input} - Color {i+1}</s>\n<|assistant|>"
        payload = {"inputs": prompt}

        try:
            response = requests.post(HF_API_URL, headers=headers, json=payload)
            result = response.json()

            if not result or not isinstance(result, list) or "generated_text" not in result[0]:
                colors.append("#888888")
                continue

            match = re.search(r"#(?:[A-Fa-f0-9]{6})", result[0]["generated_text"])
            hex_code = match.group(0) if match else "#888888"
            colors.append(hex_code)

        except Exception as e:
            print("Error during palette generation:", e)
            colors.append("#888888")

    return jsonify({"palette": colors})


if __name__ == "__main__":
    app.run(debug=True)
