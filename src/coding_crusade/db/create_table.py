import argparse

# from db.sql import users

# Ajouter un arguement obligatoire pour le script qui sera le nom de la table à créer
parser = argparse.ArgumentParser()
parser.add_argument("table_name", help="The name of the sql table you want to create")
args = parser.parse_args()
sql_file = args.table_name + ".sql"
print(sql_file)
# Lire le fichier pour exécuter la requête avec la connection psycopg
with open(sql_file) as f:
    print(f)
# try/except à chaque erreur posible
# Retour de message de succès ou d'erreur
