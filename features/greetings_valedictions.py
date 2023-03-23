from utils.utils import abriella_speak
from datetime import datetime
import sys



# Greetings and valediction intents  
def wake(user_name):
    abriella_speak(f"Hello {user_name} I'm listening, how can I help you?")

def welcome_team(user_name):
    abriella_speak(f"{user_name} I'm here to help you with your daily tasks, and to make your life easier, so if you need me just say hey abriella")

def thank_you(user_name):
    abriella_speak(f"you're welcome {user_name}, it's my pleasure, is there anything else")
  
def goodbye(user_name):
    abriella_speak(f"ok, catch you later {user_name}, have a great day, if you need me just say hey abriella")
    print("exited but still listening")
    #sys.exit()    

def what_time_is_it(user_name):
    now = datetime.now().time # time object TODO add good afternoon, good evening if time is after 12pm etc
    abriella_speak(f"{user_name} the time is " + now().strftime("%H:%M"))

def stop(user_name):
    
    abriella_speak(f"{user_name} stop now " )





    

