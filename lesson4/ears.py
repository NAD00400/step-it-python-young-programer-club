import speech_recognition

ears = speech_recognition.Recognizer()
with speech_recognition.Microphone()as mic:
    print("robot : i'm listening ")
    audio =ears.listen(mic) 
you =ears.recognize_google(audio)
print(you)


