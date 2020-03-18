# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:23:51 2020

@author: Sakib
"""
from nltk.probability import FreqDist
import csv
import psycopg2

#connecting with the database
#offline database
con = psycopg2.connect(  
            host = "localhost",
            database = "sakib",
            user = "postgres",
            password = "Rainbow6^"
            )   
    
#heroku database
#con = psycopg2.connect(
#            host = "ec2-52-86-33-50.compute-1.amazonaws.com",
#            database = "dd0t9b5dh1nqt2",
#            user = "yoalzlolfjzwwt",
#            password = "9cbaa0065c8c927cb30b3c939c01710fe8a07d432b17e65e342b9f35b8976ec2"
#            )   
cur = con.cursor()


def create_database():

    cur.execute(f"""DROP TABLE IF EXISTS analytics""")
    cur.execute(f"""CREATE TABLE analytics(
    id int PRIMARY KEY,
    Word text,
    Hit_count text)""")
    con.commit()
    print(f'Table-"analytics" created')

#Reading the text file with data
with open ("data.txt", "r") as myfile:
    data = myfile.readlines()

#removing punctuations
for char in '-.,?!"\n()\ ':
    data = str(data).replace(char, ' ') 

 #make all word lower case
data = data.lower()

#listing all words. (tokenizing)
word_list = data.split() 

#counting the word frequency with help of dictionary
fdist = FreqDist()
for word in word_list:
    fdist[word] += 1 
    
#saving the data
create_database()
with open('analytics.csv', 'w') as f:
    for key in fdist.keys():
        f.write("%s,%s\n"%(key,fdist[key]))
        cur.execute(f"INSERT INTO analytics VALUES (%s, %s)",(str(key),str(fdist[key])))

