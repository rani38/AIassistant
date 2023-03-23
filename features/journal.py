import speech_recognition as sr
import os
import os.path
from utils.utils import abriella_speak, recognizerOpen


# Create a new note and save the file with the file name the user specifies along with the text they want to save
# TODO Need to create a journal DB for this so users can create a full diary and journal

def create_note(user_name):
    abriella_speak(f"no problem {user_name}, what would you like me to make a note of?")
    done = False
    with sr.Microphone() as source:
        while not done:
            try:
                note = recognizerOpen(source)
                abriella_speak("please choose a filename")
                filename = recognizerOpen(source)
                
                with open(f"{filename}.txt", 'w') as f:
                    f.write(note)   
                    done = True
                    abriella_speak(f"ok great, I've sucessfully created your note {filename}")
                      
            except sr.UnknownValueError:
                abriella_speak(f"sorry {user_name}, i didn't catch that, please try again")

# Opens existing note created by the user and reads the contents (needs looking at as it's not working as expected)

def read_note(user_name):
    abriella_speak("which note would you like me to read?")
    done = False
    
    with sr.Microphone() as source:
        while not done:
            try:
                filename = recognizerOpen(source)
                    
                with open(f"{filename}.txt", 'r') as f:
                    note = f.read()
                    abriella_speak(note)
                    done = True
                    
            except sr.UnknownValueError:
                abriella_speak(f"sorry {user_name}, i didn't understand that, please try again")
            
            except FileNotFoundError:
                abriella_speak(f"sorry {user_name}, that note doesn't exist, if you would like to create one, just say create note")
                recognizerOpen(source)


# Delete the file/note created by user (works as expected)
def delete_note(user_name):
    abriella_speak(f"ok {user_name}, what note would you like me to delete?")
    done = False
    with sr.Microphone() as source:
        while not done:
            try:
                filename = recognizerOpen(source)
                        
                os.remove(f"{filename}.txt")
                abriella_speak(f"ok {user_name}, I have deleted {filename} for you, do you need to create another one?")
                    
            except sr.UnknownValueError:
                abriella_speak(f"sorry {user_name}, i didn't catch that, please try again")
                
            except FileNotFoundError:
                abriella_speak("sorry, that note doesn't exist, please try again")
                # TODO need an exit function but loop back to listening for user input -
                # will try recognizerOpen() because if note doens't exist, it get stuck in the loop
                recognizerOpen(source)
                