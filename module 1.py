import datetime
import pandas as pd

#naar input vragen en geen input wordt als anoniem weggeschreven
while True:
    naam = input("Wat is uw naam? , (Niet verplicht):")
    if not naam:
        naam = "Anoniem"

    break

# bericht mag niet meer dan 140 tekens zijn en de actuele datum van de input wordt gepakt
while True:
    """"Input met maximaal 140 tekens, die naar berichten.txt schrijft"""
    x = datetime.datetime.now()
    invul = input("Uw bericht: ")
    print(x)
    if len(invul) > 140:
        print("FOUT geef een maximaal bericht van 140 characters")
    else:
        break

openbericht = open('berichten.txt', 'a')

#er wordt een random station gekozen
import random
station = random.choice(open('stations.txt').readlines())

leesbericht = open('berichten.txt', 'r').readlines()
print(len(leesbericht))
if len(leesbericht) < 1:
        openbericht.write("name, text, station, date" + '\n')  # schrijft column namen naar de csv







openbericht = open('berichten.txt', 'a')
#openbericht.write("name, text, station, date" + '\n')  #schrijft column namen naar de csv
openbericht.write( naam + ',')
openbericht.write( invul + ',' + station.rstrip() + ',' + (datetime.datetime.now().ctime()) + '\n')
openbericht.close()

df = pd.read_csv('berichten.txt')




