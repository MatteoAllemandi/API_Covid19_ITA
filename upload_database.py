'''
Matteo Allemandi, Nicolò Guerra
Programma python che ogni giorno si occuperà di mantenere aggiornato lo stato del database
'''

import requests
import sqlite3
from datetime import datetime

def upload_database(jsonData):  
    try:
        sqliteConnection = sqlite3.connect('CurrentSituation.db')
        cursor = sqliteConnection.cursor()
        jsonData[-1]['data'] = datetime.fromisoformat(jsonData[-1]['data'])

        cursor.execute(f"""INSERT INTO Dati
                (data,stato,ricoverati_con_sintomi,terapia_intensiva,totale_ospedalizzati,isolamento_domiciliare,totale_attualmente_positivi,nuovi_attualmente_positivi,dimessi_guariti,deceduti,totale_casi,tamponi)
                VALUES
                ('{jsonData[-1]['data']}','{jsonData[-1]['stato']}','{jsonData[-1]['ricoverati_con_sintomi']}','{jsonData[-1]['terapia_intensiva']}','{jsonData[-1]['totale_ospedalizzati']}','{jsonData[-1]['isolamento_domiciliare']}','{jsonData[-1]['totale_attualmente_positivi']}','{jsonData[-1]['nuovi_attualmente_positivi']}','{jsonData[-1]['dimessi_guariti']}','{jsonData[-1]['deceduti']}','{jsonData[-1]['totale_casi']}','{jsonData[-1]['tamponi']}');""")
        sqliteConnection.commit() 
        print("Query eseguita")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")



def main():
    r = requests.get('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json')
    jsonData = r.json()
    upload_database(jsonData)

if __name__ == "__main__":
    main()
