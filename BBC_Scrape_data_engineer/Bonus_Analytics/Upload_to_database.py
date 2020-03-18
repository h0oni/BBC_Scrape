# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 22:51:21 2020

@author: Sakib
"""
import csv
import psycopg2
import os

#connecting with the database
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

def create_database(cur,con):

    cur.execute(f"""DROP TABLE IF EXISTS analytics""")
    cur.execute(f"""CREATE TABLE analytics(
    Word text,
    Hit_count text)""")
    con.commit()
    print(f'Table-"analytics" created')
    
    #Run the below code to upload the csv to database
def load_csv(cur,con):
    with open('analytics.csv', 'r') as f:
        reader = csv.reader(f)
        print(reader)
        next(reader) # Skip the header row.
        for row in reader:
            cur.execute(f"INSERT INTO analytics VALUES (%s, %s)",row)
    con.commit()
    
#create_database(cur,con)
load_csv(cur,con)