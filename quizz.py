#coding: utf-8

import csv
import random
import requests
from bs4 import BeautifulSoup

q = "questions.csv"
r = "reponses.csv"
f1 = open(q)
f2 = open(r)
r1 = csv.reader(f1)
r2 = csv.reader(f2)
questions = []
reponses = []
bonnerep = []
numeroquestion = 1
points = 0

for reponse in r2:
    reponses.append(reponse[0])
    reponses.append(reponse[1])
    reponses.append(reponse[2])
    reponses.append(reponse[3])

for question in r1:
    questions.append(question[0])

print("Bienvenue au quiz!")
print("Pour chaque question, veuillez entrer votre choix de réponse.")
print("Pour arrêter le quiz, tapez 'stop' ou repondez a 20 questions.")

# global numeroquestion
# global points
while numeroquestion < 21:
    hasard = random.randint(1,11)
    print(numeroquestion,":",questions[hasard-1])
    ## questions.remove([hasard-1])
    if hasard == 1:
        print(reponses[0])
        print(reponses[1])
        print(reponses[2])
        print(reponses[3])
        choix = str(input('Choix:'))
        if choix == reponses[0]:
            points=points+1
        if choix == "stop":
            finDuQuiz()
    if hasard == 2:
        print(reponses[4])
        print(reponses[5])
        print(reponses[6])
        print(reponses[7])
        choix = str(input('Choix:'))
        if choix == reponses[4]:
            points=points+1
        if choix == "stop":
            finDuQuiz()
    if hasard == 3:
        print(reponses[8])
        print(reponses[9])
        print(reponses[10])
        print(reponses[11])
        choix = str(input('Choix:'))
        if choix == reponses[8]:
            points=points+1
        if choix == "stop":
            finDuQuiz()
    if hasard == 4:
        print(reponses[12])
        print(reponses[13])
        print(reponses[14])
        print(reponses[15])
        choix = str(input('Choix:'))
        if choix == reponses[12]:
            points=points+1
        if choix == "stop":
            finDuQuiz()
    if hasard == 5:
        print(reponses[16])
        print(reponses[17])
        print(reponses[18])
        print(reponses[19])
        choix = str(input('Choix:'))
        if choix == reponses[16]:
            points=points+1
        if choix == "stop":
            finDuQuiz()
    if hasard == 6:
        print(reponses[20])
        print(reponses[21])
        print(reponses[22])
        print(reponses[23])
        choix = str(input('Choix:'))
        if choix == reponses[0]:
            points=points+1
        if choix == "stop":
            finDuQuiz()
    if hasard == 7:
        print(reponses[24])
        print(reponses[25])
        print(reponses[26])
        print(reponses[27])
        choix = str(input('Choix:'))
        if choix == reponses[24]:
            points=points+1
        if choix == "stop":
            finDuQuiz()
    if hasard == 8:
        print(reponses[28])
        print(reponses[29])
        print(reponses[30])
        print(reponses[31])
        choix = str(input('Choix:'))
        if choix == reponses[28]:
            points=points+1
        if choix == "stop":
            finDuQuiz()
    if hasard == 9:
        print(reponses[32])
        print(reponses[33])
        print(reponses[34])
        print(reponses[35])
        choix = str(input('Choix:'))
        if choix == reponses[0]:
            points=points+1
        if choix == "stop":
            finDuQuiz()
    if hasard == 10:
        print(reponses[36])
        print(reponses[37])
        print(reponses[38])
        print(reponses[39])
        choix = str(input('Choix:'))
        if choix == reponses[0]:
            points=points+1
        if choix == "stop":
            finDuQuiz()
    numeroquestion = numeroquestion+1

print("Vous avez obtenu",points,"points !")