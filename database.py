from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://miiigueeel24:Mikito.pereda24@clustermiguel.f7ezejm.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb"]
    except ConnectionError:
        print('Error de conexión con la base de datoooos')
    return db