# starting the file that will allow users to access help and tips for using the app

# currate get_started_intents.json file to conversation about how to use the assistant
import numpy as np 
import pandas as pd 
import os
import warnings
from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial import distance
from utils.utils import abriella_speak, recognizerOpen
import speech_recognition as sr


warnings.filterwarnings('ignore')
import json 

# open the dataset file
f = open(os.path.join(os.path.dirname(__file__), 'get_started_intents.json'), encoding='utf-8')
data = json.load(f)
data = data['intents']

dataset = pd.DataFrame(columns=['intent', 'text', 'responses'])

for i in data:
    intent = i['intent']
    for t, r in zip(i['text'], i['responses']):
        row = {'intent': intent, 'text': t, 'response':r}
        dataset = dataset.append(row, ignore_index=True)

def cosine_distance_countvectorizer_method(s1, s2):
    
    # sentences to list
    allsentences = [s1 , s2]
    
    # text to vector
    vectorizer = CountVectorizer()
    all_sentences_to_vector = vectorizer.fit_transform(allsentences)
    text_to_vector_v1 = all_sentences_to_vector.toarray()[0].tolist()
    text_to_vector_v2 = all_sentences_to_vector.toarray()[1].tolist()
    
    # distance of similarity
    cosine = distance.cosine(text_to_vector_v1, text_to_vector_v2)
    return round((1-cosine),2)

def respond(text):
    maximum = float('-inf')
    response = ""
    closest = ""
    for i in dataset.iterrows():
        sim = cosine_distance_countvectorizer_method(text, i[1]['text'])
        if sim > maximum:
            maximum = sim
            response = i[1]['response']
            closest = i[1]['text']
    return response

# TODO define Q&A in get_started_intents.
with sr.Microphone() as source:
    def get_started(user_name):
        
        abriella_speak(f"ok {user_name}, let's get started")
        
        while True:
            message = recognizerOpen(source)
            question = str(message).lower()
                    
            if question == "exit":
                    abriella_speak(f"""Ok {user_name}, I've exited the getting started section, if you need to continue, just say get started again,
                                            otherwise, I will be here to help you with your other tasks which can be things like, play music whilst I meditate,
                                            or get the weather for me, or tell me what my book recommendations are""")
                    break
            abriella_speak(respond(question)) 
    
