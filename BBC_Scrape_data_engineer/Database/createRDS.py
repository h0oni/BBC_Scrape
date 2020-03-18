

import csv
import psycopg2
import os

#Run the below code to upload the csv to database
def load_csv(file_name,db_name):
    #offline database
    con = psycopg2.connect(  
                host = "localhost",
                database = "sakib",
                user = os.environ.get('user_local'),
                password = os.environ.get('pass_local')
                )   
        
    #heroku database
    #con = psycopg2.connect(
    #            host = os.environ.get('heroku_host'),
    #            database = os.environ.get('heroku_database'),
    #            user = os.environ.get('heroku_user'),
    #            password = os.environ.get('heroku_pass')
    #            ) 
    cur = con.cursor()
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        print(reader)
        next(reader) # Skip the header row.
        for row in reader:
            cur.execute(f"INSERT INTO {db_name} VALUES (%s, %s, %s, %s, %s, %s)",row)
    con.commit()
    

#Run the below code to create the database

def create_database(db_name):
    #offline database
    con = psycopg2.connect(  
                host = "localhost",
                database = "sakib",
                user = os.environ.get('user_local'),
                password = os.environ.get('pass_local')
                )   
        
    #heroku database
    #con = psycopg2.connect(
    #            host = os.environ.get('heroku_host'),
    #            database = os.environ.get('heroku_database'),
    #            user = os.environ.get('heroku_user'),
    #            password = os.environ.get('heroku_pass')
    #            ) 
    cur = con.cursor()
    cur.execute(f"""DROP TABLE IF EXISTS {db_name}""")
    cur.execute(f"""CREATE TABLE {db_name}(
    Date text,
    Headline text,
    Hyperlink text,
    Tag text,
    Text text,
    Type text)""")
    con.commit()
    print(f'Table-"{db_name}" created')
   
    

create_database('data1')
load_csv('item.csv','data1')

        