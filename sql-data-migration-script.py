import mysql.connector
from mysql.connector import errorcode
import os


config = {
  'user': 'admin',
  'password': 'password',
  'host': 'gfam.cyxmuqmooa8j.us-east-1.rds.amazonaws.com',
  'database': 'gfam',
  'port': 3306
}

filename = "gfam_metadata.csv"

gfam_metadata_query = ('INSERT INTO gfam_metadata(gfam_id, name, description) VALUES (%s, %s, %s)')


def setup_connection():
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        print("connection established!")
        return cnx

def close_connection(cnx):
    if cnx is not None:
        cnx.close()

def execute(cnx, query, data):
    if cnx is not None:
        print("Conn exits")
        try:
            cursor = cnx.cursor()
            cursor.execute(query, data)
            cnx.commit()
            print("Data inserted!")
        except Exception as err:
            print(err.__str__)
        else:
            cursor.close()
    else:
        print("Connecton lost!. Data not inserted.")

def dump_data_from_file():

    cnx = setup_connection()

    if os.path.exists(filename) and os.path.isfile(filename):
        with open(filename, 'r') as fh:
            lines = fh.readlines()
            fh.close()
    else:
        close_connection(cnx)

    for line in lines:
        # if the file is a .csv, if it is tab separetd replace "," with "\t".
        line = tuple(line.strip().split(','))
        print(gfam_metadata_query, line)

        try:
            execute(cnx, gfam_metadata_query, data=line)
        except Exception as err:
            print(err.__str__)
    
    close_connection(cnx)


if __name__ == "__main__":
    """ Main"""
    dump_data_from_file()





        
