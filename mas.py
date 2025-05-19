import google.generativeai as genai

# חשוב מאוד: הכנס את מפתח ה-API שלך כאן!
# אל תשתף את המפתח הזה עם אף אחד.
API_KEY = "AIzaSyD8D7ieONZK37KT3Y5EfvxEgUl2JZV3IuU"

# הגדרת מודל ה-Gemini שאנחנו רוצים להשתמש בו
model_name = "gemini-2.0-flash"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(model_name)

def לשאול_את_ה_ai(שאלה):
  """
  הפונקציה הזו מקבלת שאלה כקלט ושולחת אותה למודל Gemini כדי לקבל תשובה.
  היא מחזירה את התשובה הטקסטואלית של ה-AI.
  """
  try:
    response = model.generate_content(שאלה)
    # אם התשובה מכילה טקסט, נחזיר אותו
    if hasattr(response, "text") and response.text:
      return response.text
    else:
      return "אני מצטער, לא הצלחתי לקבל תשובה ברורה."
  except Exception as e:
    return f"קרתה שגיאה: {e}"

def תוכנית_אינטראקטיבית():
  """
  זוהי התוכנית הראשית שמאפשרת לך לשאול שאלות את ה-AI באופן אינטראקטיבי.
  היא ממשיכה לשאול אותך שאלות עד שתגיד 'ביי'.
  """
  print("שלום! אני AI קטן שיכול לענות על שאלות (בעזרת Gemini).")
  while True:
    שאלה_משתמש = input("מה תרצה לשאול? (או הקלד 'ביי' כדי לסיים): ")
    if שאלה_משתמש.lower() == "ביי":
      print("להתראות!")
      break
    if שאלה_משתמש:
      תשובת_ai = לשאול_את_ה_ai(שאלה_משתמש)
      print("התשובה שלי:")
      print(תשובת_ai)
      print("-" * 20) # קו הפרדה יפה בין תשובות
    else:
      print("בבקשה הקלד שאלה.")

if __name__ == "__main__":
  תוכנית_אינטראקטיבית()