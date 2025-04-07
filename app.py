from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# OpenAI APIキー設定（環境変数でもOK）
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "あなたは親切なAIアシスタントです。"},
                {"role": "user", "content": user_message}
            ]
        )

        bot_reply = response.choices[0].message["content"]
        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"reply": f"エラーが発生しました: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
