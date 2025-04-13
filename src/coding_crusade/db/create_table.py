import argparse
import os
from coding_crusade.db.connection import get_connection
from psycopg import DatabaseError

sql_files_directory = os.path.dirname(os.path.realpath(__file__)) + "/sql/"
# Ajouter un arguement obligatoire pour le script qui sera le nom de la table à créer
parser = argparse.ArgumentParser()
parser.add_argument("table_name", help="The name of the sql table you want to create")
args = parser.parse_args()

sql_file = sql_files_directory + args.table_name + ".sql"
# Lire le fichier pour exécuter la requête avec la connection psycopg
try:
    with open(sql_file) as f:
        sql_file_content = f.read()
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql_file_content)
                    print(cur.fetchone())
        except DatabaseError as e:
            print("An error occured during database operations, message : " + e)
except Exception as e:
    print("Something went wrong while trying to open the file, message : " + e)

# try/except à chaque erreur posible
# Retour de message de succès ou d'erreur
