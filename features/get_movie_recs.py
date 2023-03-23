import speech_recognition as sr
from utils.utils import abriella_speak, recognizerOpen
from models import tfidf_movies_model as tfidf

# TODO # need to finish speech function to get reccommendations for movies once we have user input
# or we change to reccommendations from a list of movies from the practitioner could be you tube or other source(s)

def reccommend_movies(user_name):
    abriella_speak(f"Hello {user_name}, what movie would you like to get reccommendations for?")
    
    done = False
    
    while not done:
        try:
            movie = recognizerOpen()
            get_reccommendations = tfidf.reccommend(movie) 
            get_reccommendations = get_reccommendations.to_string(index=False)
            abriella_speak(f"Here are some reccommendations for {movie}: {get_reccommendations}")           
        
        except:
            abriella_speak("Sorry, I didn't catch that. Please try again.")
            continue

 
       
            
        

    