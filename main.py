# Our main file.
'''
import speech_recognition as sr

# Create a recognizer
r = sr.Recognizer()

# Open MIC to capture
with sr.Microphone() as source:
 while True:
    audio = r.listen(source)

    print(r.recognize_google(audio, language='pt'))
'''

from vosk import Model, KaldiRecognizer
import os
import pyaudio

model = Model("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

    print(rec.FinalResult())