import pymongo as pm
import Conta_cliente as cc

cliente = pm.MongoClient("URL...")
try:
    cliente.admin.command('ping')
    print("Sucesso conection")
except Exception as e:
    print("Not conection")
    print(e)
    exit()

db = cliente.Desafio_Dio
table = db.Cliente_Conta

table.create_index("CPF", unique=True)


Cli_1 = cc.Cliente(
    "Lancer", 
    "773399-00", 
    'Rua dos sonhadores')
print(Cli_1)

#table.insert_one(Cli_1.obj_add_bd())

#table.delete_many({})


collection = db.list_collection_names()

for collec in collection:
    print(collec)


table.update_one({"CPF":"773399-00"},{"$set":{"Conta": cc.Conta("Conta Poupança", "5555-77", "77766").obj_add_bd()}})


