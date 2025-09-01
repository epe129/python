# tee ratkaisu tänne
def pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict):
    henkilot = (henkilo1, henkilo2, henkilo3)
    keskiarvot = {}
    nimi = ""
    hen = 0
    pienin = 1000
    for c in henkilot:
        keskiarvot[f"{hen}"] = c["tulos1"] + c["tulos2"] + c["tulos3"]/3
        hen += 1
    for avain,arvo in keskiarvot.items():
        if arvo < pienin:
            pienin = arvo
            nimi = avain
    
    return henkilot[int(nimi)]
    
if __name__ == "__main__":
    henkilo1 = {"nimi": "Reijo", "tulos1": 2, "tulos2": 3, "tulos3": 3}
    henkilo2 = {"nimi": "Reijo", "tulos1": 1, "tulos2": 1, "tulos3": 1}
    henkilo3 = {"nimi": "Veijo", "tulos1": 3, "tulos2": 1, "tulos3": 1}

    print(pienin_keskiarvo(henkilo1, henkilo2, henkilo3))