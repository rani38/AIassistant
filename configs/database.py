import psycopg2
from psycopg2.errors import DuplicateTable
import os
from dotenv import load_dotenv

load_dotenv()
print(os.environ.get("Linux"))
conn = psycopg2.connect(
    database="Linux",
    user = "postgres",
    password = "123",
    host = "localhost",
    port = 5432
    )


cur = conn.cursor()
print(cur.description)

# cur.execute('CREATE EXTENSION citext;')

# cur.execute('''CREATE TABLE Users
#       (ID SERIAL PRIMARY KEY,
#       NAME TEXT NOT NULL,
#       EMAIL citext NOT NULL UNIQUE,
#       PATIENT_ID INT NOT NULL,
#       DATE DATE NULL)
#       ;''')


# #Journal
cur.execute('''CREATE TABLE Journal
      (
      ITEM TEXT NOT NULL,
      NAME TEXT NOT NULL,
      DATE DATE NULL,
      ID SERIAL PRIMARY KEY
      
      );''')

cur.execute('''CREATE TABLE Notes
      (ID SERIAL UNIQUE NOT NULL,
      NAME TEXT NOT NULL,
      ITEM TEXT NOT NULL,
      DATE DATE NULL)
      )
       ;''')

cur.execute('''CREATE TABLE Thought_record
       (ID SERIAL UNIQUE NOT NULL,
       Automatic_thought TEXT NOT NULL,
       Cognitive_thought TEXT NOT NULL,
       Rational_thought TEXT NOT NULL,
       DATE DATE NULL
       )
      ;''')

cur.execute('''CREATE TABLE TODO
      (ID SERIAL UNIQUE NOT NULL,
      ITEM TEXT NOT NULL,
      DATE DATE NULL
      )
      ;''')
# TABLE MIGRATIONS
# try:
#     #Journal
#     cur.execute('''CREATE TABLE Journal
#       (ID SERIAL UNIQUE NOT NULL,
#       ITEM TEXT NOT NULL,
#       DATE DATE NULL,

#       )
#       ;''')

#     #Notes
#     cur.execute('''CREATE TABLE Notes
#       (ID SERIAL UNIQUE NOT NULL,
#       ITEM TEXT NOT NULL,
#       DATE DATE NULL)
#       ;''')

#     #Thought record
#     cur.execute('''CREATE TABLE Thought_record
#       (ID SERIAL UNIQUE NOT NULL,
#       Automatic_thought TEXT NOT NULL,
#       Cognitive_thought TEXT NOT NULL,
#       Rational_thought TEXT NOT NULL,
#       DATE DATE NULL)
#       ;''')



#     cur.execute('''CREATE TABLE TODO
#       (ID SERIAL UNIQUE NOT NULL,
#       ITEM TEXT NOT NULL,
#       DATE DATE     NULL)
#       ;''')
# except DuplicateTable:
#     print('duplicate')
#     pass

conn.commit()
conn.close()