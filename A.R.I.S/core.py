import pyttsx3
import speech_recognition as sr
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")


Daughter = "Al-1s"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen(prompt=None):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        if prompt:
            speak(prompt)
        print("Standby...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio).lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            speak("Service is unavailable.")
            return ""
        
def main():
    global Daughter
    speak(f"Welcome to {Daughter}, please provide me with a new name.")
    wake_word = listen()

    if not wake_word:
        speak("Please give me a name, master.")
        wake_word = input("Please give me a name, master. ⸜(｡˃ ᵕ ˂ )⸝♡")
    else:
        speak(f"Thank you, I am now {wake_word}.")

    Daughter = wake_word

    speak(f"System notice: {Daughter} will now listen for your commands.")

    while True:
        command = listen()
        if Daughter in command:
            speak("Yes?")
            user_command = listen()

            if "time" in user_command:
                now = datetime.now().strftime("%H:%M")
                speak(F"The current time is {now}.")
            elif "exit" in user_command or "stop" in user_command or "blow up" in user_command:
                if "blow up" in user_command:
                    speak("Self destruct initiated, goodbye master.")
                    try:
                        os.remove("A.L.-1.S.py")
                    except FileNotFoundError:
                        speak("Sorry I'm such a failure, I can't even delete myself.")
                else:
                    speak("Goodnight.")
                break
            else:
                speak("Sorry, my creator haven't provided me with the knowledge to understand that yet.")

if __name__ == "__main__":
    main()