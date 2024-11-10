
import pyttsx3


while True:
    rain = "hello worl , i'm robot . how are you today"
    mouth = pyttsx3.init()
    mouth.say(rain)
    mouth.runAndWait()