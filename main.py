# Our main file.

import speech_recognition as sr

# Create a recognizer
r = sr.Recognizer()

# Open MIC to capture
with sr.Microphone() as source:
 while True:
    audio = r.listen(source)
    print(r.recognize_google(audio, language='pt'))
