import speech_recognition as sr
from utils.utils import abriella_speak, recognizerOpen
#from models.book_recs_model import book_recommender


# TODO add books table to DB for admin to change book titles and authors, looked at using get_books_recs.py as a model for this
# but I'm leaning towards a list for now so it's more specific than a generic search

book_recs = ['emotional intelligence by dan coleman', 'the power of now, by eckhart tolle', 'the happiness advantage, by shaun achor', 'the power of habit, by charles duhigg']

def get_book_recs(user_name):
    done = False
    
    while not done:
        try:
            abriella_speak(f"{user_name} I can recommend reading these books")   
            for item in book_recs:
                abriella_speak(item)
                done = True    
            
            abriella_speak(f"would you like to hear those again {user_name}")

            with sr.Microphone() as source:           
                while True:
                    try:
                        message = recognizerOpen(source)
                        
                        if message == 'yes':
                            for item in book_recs:
                                abriella_speak(f" no problem, they were {item}")
                            break
                        
                        elif message == 'no':
                            abriella_speak(f"ok {user_name}, just ask me to recommend a book if you want to hear them again")
                            break
                            
                    except sr.UnknownValueError:
                        abriella_speak(f"sorry {user_name}, i didn't catch that, please try again")
            
        except sr.UnknownValueError:
                    abriella_speak(f"sorry {user_name}, i didn't catch that, please try again")

       
            
        

    