import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import os
from musiclibrary import music  # correctly importing music dictionary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    command = c.lower().strip()
    print(f"Processed Command: {command}")

    if "open" in command and "google" in command:
        speak("Opening Google.")
        wb.open("https://www.google.com")

    elif "open" in command and "youtube" in command:
        speak("Opening YouTube.")
        wb.open("https://www.youtube.com")

    elif "open" in command and "github" in command:
        speak("Opening GitHub.")
        wb.open("https://www.github.com")

    elif "open" in command and "stackoverflow" in command:
        speak("Opening Stack Overflow.")
        wb.open("https://www.stackoverflow.com")

    elif "open" in command and "notepad" in command:
        speak("Opening Notepad.")
        os.system("notepad.exe")

    elif "open" in command and "calculator" in command:
        speak("Opening Calculator.")
        os.system("calc.exe")

    elif "open" in command and "command prompt" in command:
        speak("Opening Command Prompt.")
        os.system("start cmd")

    elif "open" in command and "settings" in command:
        speak("Opening Settings.")
        os.system("start ms-settings:")

    elif command.startswith("play"):
        parts = command.split(" ", 1)
        if len(parts) > 1:
            raw_song = parts[1].strip()
            song_key = raw_song.lower().replace(" ", "")  # Normalize key
            print(f"Song to play: {song_key}")

            if song_key in music:
                speak(f"Playing {raw_song}")
                wb.open(music[song_key])
            else:
                speak(f"Sorry, I don't have {raw_song}.")
        else:
            speak("Please say the name of the song after 'play'.")
    else:
        speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Initializing Friday")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word 'Friday'...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                word = recognizer.recognize_google(audio)
                print("Heard:", word)

                if word.lower() == "friday":
                    speak("Yes, what's up?")

                    with sr.Microphone() as source:
                        print("Listening for command...")
                        recognizer.adjust_for_ambient_noise(source, duration=0.5)
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        print("Command:", command)

                    processCommand(command)

        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
        except sr.UnknownValueError:
            print("Could not understand. Waiting again...")
        except sr.RequestError as e:
            print(f"Request failed: {e}")
