import speech_recognition as sr
import pyttsx3

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Robot: I'm listening...")
        audio = recognizer.listen(source, timeout=5)
        try:
            text = recognizer.recognize_google(audio, language='vi-VN')
            print("You:", text)
            return text
        except sr.UnknownValueError:
            print("Robot: I couldn't understand. Please try again.")
        except sr.RequestError as e:
            print(f"Robot: Error: {e}")
    return None
    
def respond(text):
    if "hello" in text.lower():
        return "Hello! How can I help you today?"
    elif "weather" in text.lower():
        return "The weather is great today! It's sunny and warm."
    elif "time" in text.lower():
        return "It's currently 11:37 AM. What time is it where you are?"
    elif "joke" in text.lower():
        return "Why did the chicken cross the road? To get to the other side!"
    elif "goodbye" in text.lower():
        return "Goodbye! Have a nice day."
    else:
        return "I'm not sure I understand. Can you please rephrase your question?"

engine = pyttsx3.init()
while True:
    text = listen()
    if text:
        response = respond(text)
        engine.say(response)
        engine.runAndWait()