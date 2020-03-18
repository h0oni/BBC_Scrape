

import csv
import psycopg2

#Run the below code to upload the csv to database
def load_csv(file_name,db_name):
#    con = psycopg2.connect(
#            host = "localhost",
#            database = "sakib",
#            user = "postgres",
#            password = "Rainbow6^"
#            )
    con = psycopg2.connect(
            host = "ec2-52-86-33-50.compute-1.amazonaws.com",
            database = "dd0t9b5dh1nqt2",
            user = "yoalzlolfjzwwt",
            password = "9cbaa0065c8c927cb30b3c939c01710fe8a07d432b17e65e342b9f35b8976ec2"
            )
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
#    conn = psycopg2.connect(
#            host = "localhost",
#            database = "sakib",
#            user = "postgres",
#            password = "Rainbow6^"
#            )
    con = psycopg2.connect(
            host = "ec2-52-86-33-50.compute-1.amazonaws.com",
            database = "dd0t9b5dh1nqt2",
            user = "yoalzlolfjzwwt",
            password = "9cbaa0065c8c927cb30b3c939c01710fe8a07d432b17e65e342b9f35b8976ec2"
            )
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

        