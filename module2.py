# alle modules geimporteerd die nodig gaan zijn in de rest van de opdracht
import datetime
import pandas as pd
import time
import psycopg2
from tkinter import *
# begin met het verbinden van het programma aan de database via de juiste poort
hostname = 'localhost'
database = 'zuil'
username = 'postgres'
pwd = 123456
port_id = 5432

conn = psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    password=pwd,
    port=port_id,)

cur = conn.cursor()
#tabel met columen aanmaken in de database
create_script = '''CREATE TABLE IF NOT EXISTS input (
                        id serial PRIMARY KEY,
                        Naam        varchar(30) NOT NULL,
                        bericht     varchar(30) NOT NULL,
                        station     varchar(30) NOT NULL,
                        datum       varchar(40) NOT NULL,
                        modnaam     varchar(30) NOT NULL,
                        modemail    varchar(40) NOT NULL,
                        AofG        varchar(12) NOT NULL,
                        timestamp   varchar(30) NOT NULL)  '''
cur.execute(create_script)
conn.commit()

df = pd.read_csv('berichten.txt')

row_count = len(df.index)

# while loop voor het tellen van de regels

while row_count > 0:
    row_count = row_count - 1

    # print(df.iloc[0,2])

    # haalt een row en convert to list
    data_list = df.loc[row_count].tolist()

    # printen om te boordelen
    print(df.loc[row_count])
    # vragen naar moderator input
    naam_mod = input("Hallo! Moderator wat is uw naam?")
    email_mod = input("Wat is uw email adress? ")
    goedgekeurd = input("Is het Bericht Goedgekeurd of afgekeurd G/A ? ")

    time_stamp = datetime.datetime.now().ctime()
    print(len(time_stamp))

    # create table if not
    # cur.execute(create_script)
    # de columns in de database invullen

    # insert_script = 'INSERT INTO INPUT (naam , bericht, station, datum, modnaam, modmail, AofG, timeStamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',(data_list[0], data_list[1], data_list[2], data_list[3], naam_mod, email_mod , goedgekeurd, time_stamp)
    cur.execute(
        'INSERT INTO INPUT (naam , bericht, station, datum, modnaam, modemail, AofG, timeStamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
        (data_list[0], data_list[1], data_list[2], data_list[3], naam_mod, email_mod, goedgekeurd, time_stamp))

    # cur.execute(f"INSERT INTO INPUT (naam , bericht, station, datum, MODnaam, MODmail, Goedgekeurd, timeStamp) ",
    #            f"VALUES ({data_list[0]}, {data_list[1]}, {data_list[2]}, {data_list[3]}, {naam_mod}, {email_mod} , {goedgekeurd}, {time_stamp})")

    #
    # insert_value = (data_list[0], data_list[1], data_list[2], data_list[3], naam_mod, email_mod , goedgekeurd, time_stamp)

    conn.commit()

cur.close()
conn.close()

row_count = len(df.index)
max_row = row_count
max_mes = 5

while row_count > max_row - max_mes:
    #    # printen om te boordelen
    row_count = row_count - 1

    # print(df.loc[row_count])
print(df)

open("berichten.txt", "w").close()