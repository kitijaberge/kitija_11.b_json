#2. Izveidot Python programmu, kas nolasītu un izdrukātu tikai trešās kolonnas datus no CSV faila. (3 punkti)

import csv
import json

def tris(csv_fails):
    try:
        with open(csv_fails, 'r', newline='') as fails:
            lasitajs = csv.reader(fails)
            kolonnas = []
            for rinda in lasitajs:
                if len(rinda) >= 3:  
                    kolonnas.append(rinda[2])
                else:
                    print("Šai rindai nav trešās kolonnas")
            return kolonnas
    except FileNotFoundError:
        print("CSV fails '%s' nav atrasts." % csv_fails)

trisdati = tris('dati.csv')

if trisdati:
    json_dati = json.dumps(trisdati)
    print(json_dati)
