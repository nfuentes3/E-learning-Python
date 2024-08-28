import pprint

anna = {
    "id" : {
        "nombre" : "anna",
        "apellido" : "rodriguez"
    },
    "edad" : 50,
    "sueldo" : 30000
}

josefa = {
    "id" : {
        "nombre" : "josefa",
        "apellido" : "rodriguez"
    },
    "edad" : 50,
    "sueldo" : 30000
}

db = {}
db["anna"] = anna
db["joseffa"] = josefa
print(db)
print("---" * 30)

pprint.pprint(db)