import openai
import speech_recognition as sr
import pyttsx3
import requests
import tkinter as tk
from textblob import TextBlob

# הגדרת מפתח API (החלף ב-API אמיתי)
openai.api_key = "YOUR_API_KEY"

# פונקציה לשליחת שאלה ל-GPT
def ask_ai(question):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}]
    )
    return response["choices"][0]["message"]["content"]

# פונקציה לזיהוי דיבור
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("דבר עכשיו...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="he-IL")
        return text
    except sr.UnknownValueError:
        return "לא הצלחתי להבין, נסה שוב!"
    except sr.RequestError:
        return "בעיה בחיבור לאינטרנט."

# פונקציה לחיפוש בגוגל
def google_search(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key=YOUR_GOOGLE_API_KEY&cx=YOUR_SEARCH_ENGINE_ID"
    response = requests.get(url)
    data = response.json()
    results = [item["title"] + ": " + item["link"] for item in data.get("items", [])]
    return "\n".join(results)

# פונקציה לניתוח רגשות
def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "טקסט חיובי 😊"
    elif analysis.sentiment.polarity < 0:
        return "טקסט שלילי 😢"
    else:
        return "טקסט נייטרלי 😐"

# יצירת ממשק גרפי
def send_question():
    question = entry.get()
    response = ask_ai(question)
    result_label.config(text=response)

# הגדרת ממשק GUI
root = tk.Tk()
root.title("צ'אט AI חכם")
root.geometry("500x400")

entry = tk.Entry(root, width=50)
entry.pack()

send_button = tk.Button(root, text="שאל את AI", command=send_question)
send_button.pack()

result_label = tk.Label(root, text="", wraplength=400)
result_label.pack()

root.mainloop()
