#5. Izveidot Python programmu, kas ļauj lietotājam ievadīt savu vārdu terminālī. Ievadīto vārdu pēc tam ierakstīt teksta failā (piemēram, "lietotajs.txt"). Programmai jābūt spējīgai apstrādāt kļūdas, piemēram, faila nepieejamību vai rakstīšanas problēmas. Pēc ierakstīšanas izvadīt paziņojumu par veiksmīgu darbību vai kļūdu gadījumā attiecīgu kļūdas ziņojumu. json formātā (8 punkti)
import json

def ierakstit_faila(nosaukums, saturs):
    try:
        with open(nosaukums, 'w') as fails:
            fails.write(saturs)
            return {"statuss": "Veiksmīgi ierakstīts teksta failā."}
    except FileNotFoundError:
        return {"kļūda": f"Faila '{nosaukums}' nav iespējams atrast."}
    except Exception as e:
        return {"kļūda": str(e)}

def main():
    vards = input("Lūdzu, ievadiet savu vārdu: ")
    rezultats = ierakstit_faila("lietotajs.txt", vards)
    print(json.dumps(rezultats))

if __name__ == "__main__":
    main()