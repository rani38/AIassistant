
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    database="Linux",
    user = "postgres",
    password = "123",
    host = "localhost",
    port = 5432
    )

def add_todo_item(name, date = None):
    cur = conn.cursor()
    
    if(date is not None):
      cur.execute(f"INSERT INTO TODO (ITEM, DATE) \
      VALUES ('{name}', '{date}')")
    else: 
      cur.execute(f"INSERT INTO TODO (ITEM) \
      VALUES ('{name}')")

    conn.commit()
    
def add_notes_item(user_id, name, note, date = None):
    cur = conn.cursor()

    if(date is not None):
      cur.execute(f"INSERT INTO Notes (NAME, ITEM, DATE, user_id) VALUES ('{name}', '{note}', '{date}', '{user_id}')")
    else: 
      
      cur.execute(f"INSERT INTO Notes (NAME, ITEM, user_id) \
      VALUES ('{name}','{note}', '{user_id}')")

    conn.commit()

def get_notes_item(name):
  cur = conn.cursor() 

  cur.execute(f"""SELECT * FROM "notes" WHERE name = '{name}';""")

 
  return cur.fetchone()


def delete_notes_items(name): 
  cur = conn.cursor()

  recordID = get_notes_item(name)[0]

  cur.execute(f"DELETE FROM Notes WHERE id = {recordID};")

  conn.commit()



def add_journal_item(user_id, name, note, date = None):

    cur = conn.cursor()

    if(date is not None):
      cur.execute(f"INSERT INTO Journal (NAME, ITEM, DATE, user_id) VALUES ('{name}', '{note}', '{date}', '{user_id}')")
    else: 
      
      cur.execute(f"INSERT INTO Journal (NAME, ITEM, user_id) VALUES ('{name}','{note}', '{user_id}')")

    conn.commit()

def get_journal_item(name):
  cur = conn.cursor() 

  cur.execute(f"""SELECT * FROM "journal" WHERE name = '{name}';""")


  return cur.fetchone()

def delete_journal_item(name): 
  cur = conn.cursor()

  recordID = get_journal_item(name)[3]

  cur.execute(f"DELETE FROM Journal WHERE id = '{recordID}';")

  conn.commit()
