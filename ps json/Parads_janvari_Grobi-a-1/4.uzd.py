#4. Izveidot Python programmu, kur lietotājs ievada gan faila nosaukumu, gan faila formātu (paplašinājumu), un atkarībā no faila paplašinājuma tiek nolasīts faila saturs. Nolasītā informācija ir jāizdrukā terminālī. Ievērot iespejamās kļūdas! json formātā (8 punkti)
import json

def lasit_failu(nosaukums, paplasinajums):
    try:
        with open(f"{nosaukums}.{paplasinajums}", 'r') as fails:
            saturs = fails.read()
            return saturs
    except FileNotFoundError:
        return None

def main():
    nosaukums = input("Ievadiet faila nosaukumu: ")
    paplasinajums = input("Ievadiet faila paplašinājumu (piemēram, txt, csv, utt.): ")
    
    saturs = lasit_failu(nosaukums, paplasinajums)
    if saturs is not None:
        print(json.dumps({"saturu": saturs}))
    else:
        print(f"Faila '{nosaukums}.{paplasinajums}' nav atrasts.")

if __name__ == "__main__":
    main()
