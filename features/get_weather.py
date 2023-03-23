import speech_recognition as sr
import pyowm
from utils.utils import abriella_speak, recognizerOpen

# Getting weather report from openweathermap.org API

owm = pyowm.OWM('253c749eac4517ad796d4922ef6684c5')
mgr = owm.weather_manager()
        
def get_weather(user_name):
    abriella_speak(f"no problem {user_name}, what city do you need the weather for?")
    done = False
    with sr.Microphone() as source:
        while not done:
            try:
                city = recognizerOpen(source)
                convert_city_to_string = city.lower() # convert spoken city from user to string for observation
                observation = mgr.weather_at_place(convert_city_to_string) 
                w = observation.weather
                
                weather = w.detailed_status
                temp = w.temperature('celsius')['temp']
                abriella_speak(f"the current weather in {city} is {weather} with a temperature of {temp} degrees celsius")
                done = True
                
            except sr.UnknownValueError:
                abriella_speak(f"sorry {user_name}, i didn't catch that, please try again")
              

      