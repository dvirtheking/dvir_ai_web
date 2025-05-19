from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # כדי לאפשר בקשות מהדפדפן (מקורות שונים)

# חשוב מאוד: הכנס את מפתח ה-API שלך כאן!
API_KEY = "AIzaSyB0du0mrmXlXYFokJ5xTdB7mbWslo4ASyY"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route('/ask_ai', methods=['POST'])
def ask_ai():
    data = request.get_json()
    if 'question' not in data:
        return jsonify({'error': 'חסרה שאלה'}), 400

    question = data['question']
    try:
        response = model.generate_content(question)
        if hasattr(response, "text") and response.text:
            return jsonify({'answer': response.text})
        else:
            return jsonify({'answer': 'לא קיבלתי תשובה ברורה מה-AI.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)