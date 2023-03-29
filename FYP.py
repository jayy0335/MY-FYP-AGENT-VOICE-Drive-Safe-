import speech_recognition as sr
import webbrowser
import os
import pyautogui
import tkinter as tk
import pyttsx3

# Create a recognizer object
r = sr.Recognizer()

current_directory = os.getcwd()
# Initialize the speech recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to take user command and perform tasks
def perform_task(command):
    if "shutdown" in command:
        # Stop listening and close the window
        window.destroy()
    elif "calculator" in command:
        os.system('start calc.exe') 
        speak ("opening Calculator")
    elif "map" in command:
        webbrowser.open('https://www.google.com/maps')
        speak ("opening Google Map")
    elif "chrome" in command:
        os.system('start chrome.exe')
        speak ("opening Google chrome")
    elif "email" in command:
        webbrowser.open('https://mail.google.com')
        speak ("opening Gmail")
    elif "youtube" in command:
        webbrowser.open('https://youtube.com')
        speak ("opening Youtube")
    elif "play music" in command:
        os.system('start vlc.exe "E:\songs"')
        speak ("opening VlC Player")
    elif "next song" in command:
        pyautogui.hotkey('n')
    elif "previous song" in command:
        pyautogui.hotkey('p')
    elif "pause" in command:
        pyautogui.hotkey(' ')
    elif "play" in command:
        pyautogui.hotkey(' ')
    elif "close vlc" in command:
        pyautogui.hotkey('ctrl', 'q')
    elif "volume up" in command:
        pyautogui.press('volumeup')
        speak ("Volume increased")
    elif "volume down" in command:
        pyautogui.press('volumedown')
        speak ("Volume decreased")
    elif "mute" in command:
        pyautogui.press('volumemute')
        speak ("volume has been mute")
    elif "open file explorer" in command:
        os.system('explorer')
        speak ("opening file explorer")
    elif "notepad" in command:
        os.system('start notepad.exe')
        speak ("opening notepad")
    elif "open control panel" in command:
        os.system('start control.exe')
        speak ("opening control panel")
    elif "open task manager" in command:
        os.system('taskmgr')
        speak ("opening task manager")
    else:
        print("Sorry, I didn't understand that command.")

# Define a function to start listening for commands
def start_listening():
    # Use speech recognition to get user's command
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        perform_task(command)
    except sr.UnknownValueError:
        print("Sorry, I could not understand your command.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # Call the start_listening function again after 1 second
    window.after(1000, start_listening)
 
# Create a GUI window
window = tk.Tk()
window.title("Voice Assistant")

# Call the start_listening function when the window is opened
window.after(0, start_listening)

# Create a button to play music
music_button = tk.Button(window, text="Play Music", command=lambda: perform_task("play music"))
music_button.pack()

# Create buttons to answer or decline a call
call_button = tk.Button(window, text="Answer", command=lambda: perform_task("answer"))
call_button.pack()

decline_button = tk.Button(window, text="Decline", command=lambda: perform_task("decline"))
decline_button.pack()

shutdown_button = tk.Button(window, text="Shutdown", command=lambda: perform_task("shutdown"))
shutdown_button.pack()

# Start the GUI loop
window.mainloop()
