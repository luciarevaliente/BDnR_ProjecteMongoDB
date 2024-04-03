#Carregar les dades des d'unfitxer JSON
from pymongo import MongoClient
import json

# En execució remota
Host = 'localhost'
Port = 27017


def insert_data(json_file):
    DSN = "mongodb://{}:{}".format(Host, Port)
    conn = MongoClient(DSN)
    db = conn['aplicacio']
    productes = db['productes']
    clients = db['clients']
    tiquets = db['tiquets']
    estades = db['estades']

    # llegim JSON
    with open(json_file, 'r') as file:
        data = json.load(file)

    #inserim dades
    for cliente in data['clients']:
        if clients.count_documents({'DNI': cliente['DNI']}) == 0:
         clients.insert_one(cliente)

    for producto in data['productes']:
        if productes.count_documents({'codi': producto['codi']}) == 0:
            productes.insert_one(producto)

    for tiquet in data['tiquets']:
        if tiquets.count_documents({"id_client":tiquets['id_client']})==0:
            tiquets.insert_one(tiquet)

    for estada in data['estades']:
        if estades.count_documents({'matricula_cotxe':estades['matricula_cotxe']})==0:
            estades.insert_one(estada)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Inserim dades a una base de dades MongoDB.')
    parser.add_argument('-f', '--file', type=str, help='Nom arxiu JSON de dades')

    args = parser.parse_args()

    insert_data(args.file)

