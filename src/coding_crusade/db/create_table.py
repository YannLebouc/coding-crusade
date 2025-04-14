import argparse
import os
from coding_crusade.db.connection import get_connection
from psycopg import DatabaseError

# Le script prend un nom de table à créer en argument
# Son seul but est de récupérer le fichier sql qui porte ce nom et de l'exécuter
parser = argparse.ArgumentParser()
parser.add_argument("table_name", help="The name of the sql table you want to create")
args = parser.parse_args()

sql_files_directory = os.path.dirname(os.path.realpath(__file__)) + "/sql/"
sql_file = sql_files_directory + args.table_name + ".sql"

try:
    with open(sql_file) as f:
        sql_file_content = f.read()
    try:
        with get_connection() as conn:
            cursor = conn.execute(sql_file_content)
            print("Query status message : " + cursor.statusmessage)
    except DatabaseError as e:
        print("An error occured during database operations, message : " + e)
except Exception as e:
    print("Something went wrong while trying to open the file, message : " + e)
