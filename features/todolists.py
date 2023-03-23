import speech_recognition as sr
from utils.utils import abriella_speak, recognizerOpen
from utils.db_utils import add_todo_item


# todolist item (TODO connected to db database, inputs come from admin)

# iterate through the todo list and speak each item  
todo_list = ["meditate for 10 minutes", "go for a walk", "read your book"]

def get_todoList(todo_list, user_name):
    abriella_speak("you have these items on your task list")   
    for item in todo_list:
        abriella_speak(item)

# def add_todo(user_name):
   
#     abriella_speak(f"ok {user_name}, what would you like to add to your to do list?")
#     done = False
    
#     while not done:
#         try:
#             item = recognizerOpen()
#             # todo_list.append(item)
#             done = True

#             add_todo_item(item)
                
#             abriella_speak(f"ok {user_name}, I successfully added {item} to your to do list")


#         except sr.UnknownValueError:
#             abriella_speak(f"sorry {user_name}, i didn't understand that, please try again")
           

# Remove an item from the todo list
# def delete_todolistitem(todo_list, user_name):

#     abriella_speak("what would you like to delete from your tasks list?")
    
#     done = False
#     while not done:
#         try:
#             item = recognizerOpen()
#             todo_list.remove(item)
#             done = True
                
#             abriella_speak(f"ok {user_name}, I successfully deleted {item} from your tasks list")

#         except sr.UnknownValueError:
#             abriella_speak(f"sorry {user_name}, i didn't understand that, please try again")
            
#         except ValueError:
#             abriella_speak(f"sorry {user_name}, that item is not on your tasks list, please try again, or create a new task")
