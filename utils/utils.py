import pyttsx3 as tts
import speech_recognition as sr
import openai
openai.api_key = "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"


conversation = ""
user_name = "David"
def abriella_speak(text):
        engine = tts.init()
        voices = engine.getProperty('voices')
        #engine.setProperty('voice', 'english+f3') 
        engine.setProperty('rate', 155)
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
with sr.Microphone() as source:   
    def recognizerOpen(source,callback = None):
            print("please speak")
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            print("listening")
            audio = recognizer.listen(source,timeout=5)
            print("got it")
             
            recognizer_input = recognizer.recognize_google(audio)
            print("You said:", recognizer_input)
            recognizer_input = recognizer_input.lower()

                
            response = openai.Completion.create(engine='text-davinci-003', prompt=recognizer_input, max_tokens=70)
            text = response["choices"][0]["text"].replace("\n", "")
            print(text)
            text = text.split(user_name + ": ", 1)[0].split("Abriella: ", 1)[0]

            return recognizer_input
    

# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source, timeout=5)

# try:
#     text = r.recognize_google(audio)
#     print("You said:", text)
# except sr.WaitTimeoutError:
#     print("Timeout occurred while waiting for speech input.")
# except sr.UnknownValueError:
#     print("Unable to recognize speech input.")