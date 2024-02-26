#3. Izveidot Python programmu, kas nolasītu un izdrukātu trešās teksta faila rindas saturu json formātā (3 punkti)

def lasit_treso_rindu(nosaukums):
    try:
        with open(nosaukums, 'r') as fails:
            rindas = fails.readlines()
            if len(rindas) >= 3:
                tresa_rinda = rindas[2]
                print(tresa_rinda)
            else:
                print("Failā nav pietiekami daudz rindu.")
    except FileNotFoundError:
        print("Faila '%s' nav atrasts." % nosaukums)

lasit_treso_rindu('piemers.txt')
