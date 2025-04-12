import argparse
import os
from coding_crusade.db.connection import get_connection

sql_files_directory = os.path.dirname(os.path.realpath(__file__)) + "/sql/"
# Ajouter un arguement obligatoire pour le script qui sera le nom de la table à créer
parser = argparse.ArgumentParser()
parser.add_argument("table_name", help="The name of the sql table you want to create")
args = parser.parse_args()

sql_file = sql_files_directory + args.table_name + ".sql"
# Lire le fichier pour exécuter la requête avec la connection psycopg
with open(sql_file) as f:
    print(f)

# with get_connection() as conn:
#     with conn.cursor() as cur:
# cur.execute("SELECT 1")
# print(cur.fetchone())
# try/except à chaque erreur posible
# Retour de message de succès ou d'erre
