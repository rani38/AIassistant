import speech_recognition as sr
import wikipedia as wiki
import random

from utils.utils import abriella_speak, recognizerOpen

# TODO fixed disambiguatoin error, need to add help funtion in help and promtpe, but also 
# need to perhaps look at one function here, perhaps with for if statements depending on the intent
# curenntly uses wiki_search when user input is something like "wiki search" or "look up on wikipedia"
# uses wiki_direct when user input is something like "tell me about mecury" or "what is spacetime" or "who is isaac newton, but testing 
# it with "who is doesn't work, but "search wiki" does work, so need to look at this, handles the disambiguation error, well now though

def wiki_direct(user_name):
    done = False
    with sr.Microphone() as source:
        while not done:
            try:
                search = recognizerOpen(source)
                result = wiki.summary(search, sentences=3)
                done = True
                abriella_speak(f"according to wikipedia, {result}")
                
                abriella_speak(f"would you like to know more about this {user_name}")
                            
                while True:
                    try:
                        message = recognizerOpen(source)
                        
                        if message == 'yes':
                            result = wiki.summary(search, sentences=10)
                            abriella_speak(f"according to wikipedia, {result}")
                            break
                        
                        elif message == 'no':
                            abriella_speak(f"ok {user_name}, i'll stop here")
                            break
                    
                    except sr.UnknownValueError:
                        abriella_speak(f"sorry {user_name}, i couldn't find anything related to {search}, please try again")
                        
            except wiki.exceptions.DisambiguationError as e:
                        
                        s = random.choice(e.options)
                        p = wiki.page(s)
                        
                        abriella_speak (f"it looks like there is more than one result for, {search}")
                        abriella_speak (f"i've chosen one at random called, {p.title}")
                        abriella_speak (f"would you like me to continue and talk about, {p.title}")
                        
                        message = recognizerOpen(source)
                        
                        if message == 'yes':
                            result = wiki.summary(p, sentences=3)
                            abriella_speak(f"according to wikipedia, {result}")
                            break
                        if message == 'no':
                            abriella_speak(f"""ok {user_name}, sorry about that, try searching again but this time try to be more specific, 
                                        wikipedia has a vast amount of information for me to search through.""")
                            break
                        done = True
                               

# searches wiki when the question is search for something with no context just a simple "search wiki" question? See intents.json

def wiki_search(user_name):
    abriella_speak(f"ok {user_name}, what subject would you like me to search for?")
    done = False
    with sr.Microphone() as source:
        while not done:
            try:
                search = recognizerOpen(source)
                result = wiki.summary(search, sentences=3)
                done = True
                abriella_speak(f"according to wikipedia {result}")
                abriella_speak(f"would you like to know more about this {user_name}")
                
                while True:
                    try:
                        message = recognizerOpen(source)
                        
                        if message == 'yes':
                            result = wiki.summary(search, sentences=10)
                            abriella_speak(f"according to wikipedia {result}")
                            break
                        
                        elif message == 'no':
                            abriella_speak(f"ok {user_name}, i'll stop here")
                            break                        

                    except sr.UnknownValueError:
                        abriella_speak(f"sorry {user_name}, i couldn't find anything related to {search}, please try searching again")
        
            except wiki.exceptions.DisambiguationError as e:
                        
                        s = random.choice(e.options)
                        p = wiki.page(s)
                        
                        abriella_speak (f"it looks like there is more than one result for {search}")
                        abriella_speak (f"i've chosen one at random called {p.title}")
                        abriella_speak (f"would you like me to continue and talk about {p.title}")
                        
                        message = recognizerOpen()
                        
                        if message == 'yes':
                            result = wiki.summary(p, sentences=3)
                            abriella_speak(f"according to wikipedia {result}")
                            break
                        if message == 'no':
                            abriella_speak(f"""ok {user_name}, I'm sorry about that, try searching again but this time try to be more specific, 
                                        wikipedia has a vast amount of information for me to search through.""")
                            break
                        done = True
 