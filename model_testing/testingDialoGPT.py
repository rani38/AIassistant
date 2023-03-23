from transformers import AutoModelForCausalLM, AutoTokenizer
from utils.utils import abriella_speak, recognizerOpen
import torch
import speech_recognition as sr

recognizer = sr.Recognizer()

# Implemented DialoGPT from https://huggingface.co/microsoft/DialoGPT-large?text=Hi. testing DialoGPT for conversation.
# DialoGPT is a large-scale pre-trained conversational language model based on the GPT-2 architecture.

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")

def abriella_chat():
    
    # Let's chat for 5 lines
    for step in range(5):
        # encode the new user input, add the eos_token and return a tensor in Pytorch
        new_user_input_ids = tokenizer.encode(input(recognizerOpen) + tokenizer.eos_token, return_tensors='pt')
        
        # append the new user input tokens to the chat history
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

        # generated a response while limiting the total chat history to 1000 tokens, 
        chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

        # pretty print last ouput tokens from bot
        print("DialoGPT: {}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))
        abriella_speak("DialoGPT: {}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))
    


