import os
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
print("Welcome To RoboSpeaker!")
user = input("Enter what you want to speak: ")
# text = "Python text-to-speech test. using win32com.client"
speak.Speak(user)

