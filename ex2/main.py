#Carregar les dades des d'unfitxer JSON
import argparse
import pymongo 
from pymongo import MongoClient
import json

# Establim la connexió amb el port determinat
Host = 'dcccluster.uab.cat'
Port = 8209

DSN = "mongodb://{}:{}".format(Host, Port)
conn = MongoClient(DSN)

# Creem la base de dades
db = conn['aplicacio']
productes = db['productes']
clients = db['clients']
tiquets = db['tiquets']
estades = db['estades']

# Carreguem les dades a partir dels json
with open('clients.json', 'r') as file:
    cl = json.load(file)

for cliente in cl:
    try:
        clients.insert_one(cliente)
    except pymongo.errors.DuplicateKeyError:
        # El document ja existeix a la col·lecció
       pass



with open('productes.json', 'r') as file:
    pr = json.load(file)
for producto in pr:
       try:
           productes.insert_one(producto)
       except pymongo.errors.DuplicateKeyError:
           # El document ja existeix a la col·lecció
           pass

with open('tiquets.json', 'r') as file:
    t = json.load(file)
for tiquet in t:
        try:
            tiquets.insert_one(tiquet)
        except pymongo.errors.DuplicateKeyError:
            # El document ja existeix a la col·lecció
            pass

with open('estades.json', 'r') as file:
    e = json.load(file)
for estada in e:
        try:
            estades.insert_one(estada)
        except pymongo.errors.DuplicateKeyError:
            # El document ja existeix a la col·lecció
            pass

conn.close()
