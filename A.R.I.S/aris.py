import pyttsx3
import speech_recognition as sr
from datetime import datetime

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
    speak("Welcome to Aris, please provide me with a new name.")
    wake_word = listen()

    if not wake_word:
        speak("Please give me a name, master.")
        wake_word = input("Please give me a name, master. ⸜(｡˃ ᵕ ˂ )⸝♡")
    else:
        speak(f"Thank you, I am now {wake_word}.")

    speak(f"System notice: {wake_word} will now listen for your commands.")

    while True:
        command = listen()
        if wake_word in command:
            speak("Yes?")
            user_command = listen()

            if "time" in user_command:
                now = datetime.now().strftime("%H:%M")
                speak(F"The current time is {now}.")
            elif "exit" in user_command or "stop" in user_command:
                speak("Goodnight.")
                break
            else:
                speak("Sorry, my creator haven't provided me with the knowledge to understand that yet.")

if __name__ == "__main__":
    main()