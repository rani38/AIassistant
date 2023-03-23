from intents.intents import GenericAssistant
from abc import ABCMeta, abstractmethod
import speech_recognition as sr
from features.journal import create_note, read_note, delete_note
from features.todolists import get_todoList
from features.greetings_valedictions import welcome_team, thank_you, what_time_is_it, goodbye, wake
from features.wiki_search import wiki_search, wiki_direct
from features.play_music import play_music,stop
from features.get_weather import get_weather
from utils.utils import recognizerOpen   
from features.get_book_recs import get_book_recs
from getting_started.get_started import get_started
from features.chatgpt import chatgpt

recognizer = sr.Recognizer()

user_name = "David"

# Current to do list items, basic at this stage (TODO expand into database as read only) 

#todo_list = ["meditate for 10 minutes", "go for a walk", "read your book"]
# Map Intents to functions intents.py uses these mappings along with intents.json for the intents

mappings = {
    "wake": wake,
    "welcome": welcome_team, 
    "thank_you": thank_you,
    "create_note": create_note,
    "read_note": read_note,
    "delete_note": delete_note,
    "time": what_time_is_it,
    "wiki_search": wiki_search,
    "wiki_direct": wiki_direct,
    "play_music": play_music,
    "get_books": get_book_recs,
    "get_weather": get_weather,
    "get_todoList": get_todoList,
    "get_started": get_started,
    "quit": goodbye,
    "stop":stop
    
}

# Main class 

class IVoiceAssistant(metaclass=ABCMeta):

    def __init__(self, user_name):
        self.assistant = GenericAssistant('intents/intents.json', user_name = user_name, intent_methods=mappings)
        #self.assistant.train_model()
        #self.assistant.save_model() 
        self.assistant.load_model()

    @abstractmethod
    def journal(self):
        """ Implemented in child class """

    @abstractmethod
    def todolists(self, id):
        """ Implemented in child class """

    @abstractmethod
    def conversation(self, id):
        """ Implemented in child class """
    
    @abstractmethod
    def wiki_search(self, id):
        """ Implemented in child class """
    
    abstractmethod
    def wiki_direct(self, id):
        """ Implemented in child class """
    
    abstractmethod
    def play_music(self, id):
        """ Implemented in child class """
    
    abstractmethod
    def get_weather(self, id):
        """ Implemented in child class """
    
    abstractmethod
    def get_started(self, id):
        """ Implemented in child class """ 
   
    abstractmethod
    def stop(self, id):
        """ Implemented in child class """ 
   
            

# Child class of IVoiceAssistant
# TODO add a wake function to this class so that only on wake word does it start listening and allows access to the different features

class VoiceAssistant(IVoiceAssistant):

    def __init__(self, name, user_name):
        super().__init__(user_name = user_name)
        self.name = name
        

    def journal(self):
        return super().journal()
    

    def todolists(self, id):
        return super().todolists(id)

    def conversation(self, id):
        return super().conversation(id)
    
    def wiki_search(self, id):
        return super().wiki_search(id)
    
    def wiki_direct(self, id):
        return super().wiki_direct(id)
    
    def play_music(self, id):
        return super().play_music(id)
    
    def get_weather(self, id):
        return super().get_weather(id)
    
    def get_started(self, id):
        return super().get_started(id)
   
		
    def stop(self, id):
        return super().get_started(id)
   
		

# Main function to run the assistant 

assistant = VoiceAssistant('Abriella Assistant', user_name)

# for testing purposes to denote model has loaded successfully and system is ready
print('Say something to Abriella')

with sr.Microphone() as source:
    while True:  
        print("aayushi")  
        try:
            
            print("Your turn to speak")
            message = recognizerOpen(source)
            print(message)
            assistant.assistant.request(message)
                
        except sr.UnknownValueError:
            print("Sorry, could not understand what you said.")
            recognizer = sr.Recognizer()