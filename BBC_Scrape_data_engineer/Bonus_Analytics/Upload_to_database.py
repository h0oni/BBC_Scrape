# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 22:51:21 2020

@author: Sakib
"""
import csv
import psycopg2

#connecting with the database
#offline database
#con = psycopg2.connect(  
#            host = "localhost",
#            database = "sakib",
#            user = "postgres",
#            password = "Rainbow6^"
#            )   
    
#heroku database
con = psycopg2.connect(
            host = "ec2-52-86-33-50.compute-1.amazonaws.com",
            database = "dd0t9b5dh1nqt2",
            user = "yoalzlolfjzwwt",
            password = "9cbaa0065c8c927cb30b3c939c01710fe8a07d432b17e65e342b9f35b8976ec2"
            )   
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
    
create_database(cur,con)
load_csv(cur,con)