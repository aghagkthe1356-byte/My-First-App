import os
import speech_recognition as sr
from gtts import gTTS
recognizer = sr.Recognizer()
def listen():
	with sr.Microphone() as source:
		audio = recognizer.listen(source)
		try:
			text = recognizer.recognize_google(audio, language='hi-IN')
		except:
		  return None
		return text
	tts = gTTS(text=text, lang='hi')
	tts.save("response.mp3")
	os.system("mpg321 response.mp3")
	print(listen())