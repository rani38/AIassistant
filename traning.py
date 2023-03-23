from intents.intents import GenericAssistant
from abc import ABCMeta, abstractmethod
import speech_recognition as sr
from features.journal import create_note, read_note, delete_note
from features.todolists import get_todoList
from features.greetings_valedictions import welcome_team, thank_you, what_time_is_it, goodbye, wake,stop
from features.wiki_search import wiki_search, wiki_direct
from features.play_music import play_music
from features.get_weather import get_weather
from utils.utils import recognizerOpen   
from features.get_book_recs import get_book_recs
from getting_started.get_started import get_started
from features.chatgpt import chatgpt

user_name = "David"

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
    "stop":stop,
    
}

train = GenericAssistant('intents/intents.json', user_name = user_name, intent_methods=mappings)

train.train_model()
train.save_model()