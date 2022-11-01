#Modelo: [(nome, desc,periodo,duracao,_id)]

import csv
from os import listxattr

def lerObras():
    file = open("obras.csv", encoding="UTF8")
    file.readline()
    csv_file = csv.reader(file,delimiter=";")

    lista=[]
    for linha in csv_file:
        lista.append(tuple(linha))
    return lista

def numeroObras(obras):
    obras= lerObras()
    print(len(obras))

def imprime(obras):
    for obra in obras:
        nome, desc, anoCriacao, periodo, compositor, duracao, _id=obra

def pp(obras):
    for obra in obras:
        nome, desc, anoCriacao, periodo, compositor, duracao, _id=obra
    print(f"{obra[0][:25]:25} | {obra[4][:30]:30}")
        




        
    return 


