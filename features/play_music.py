import speech_recognition as sr
from playsound import playsound,_playsoundWin
from utils.utils import abriella_speak
import time
import threading
import os 
from utils.utils import recognizerOpen
from playsound import playsound, _playsoundWin as playsound_win
import winsound
# this function works great but we need a stop function to allow pausing and restarting the music or stopping it completely






def stop(user_name):
    abriella_speak(f"{user_name} stop now " )


def play_music(user_name):
    abriella_speak(f"OK {user_name}, here is a nice relaxing album for you. It will help you unwind, and it's especially good for meditating.")
    
    def play_music1():
        playsound("assets/relaxing-music-vol1.mp3")
        
    music_thread = threading.Thread(target=play_music1)
    music_thread.start()

    # listen for a voice command to stop the music
    while True:
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Say 'please stop' to stop the music playback.")
                r.adjust_for_ambient_noise(source, duration=0.2)
                print("listening")
                audio = r.listen(source)
                print("got it")

            text = r.recognize_google(audio)
            print("You said:", text)
            if text == "please stop":
                os.kill(os.getpid(), 9)
                print("Music playback stopped.")
                break
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")