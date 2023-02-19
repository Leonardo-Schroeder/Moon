import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[-2].id)

engine.say("Palmeiras é gigante")
engine.runAndWait()