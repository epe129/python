def laske_oikein_vastatut_kysymykset(sanat):
    oikein_vastatut = 0
    for kysymys, oikea_vastaus in sanat.items():
        vastaus = input(kysymys)
        if vastaus == oikea_vastaus:
            oikein_vastatut += 1
        else:
            print("Väärä vastaus.")
    return oikein_vastatut



sanat = {
    "Vad vill du göra i framtiden ": "mitä haluat tehdä tulevaisuudessa",
}

oikein_vastatut = laske_oikein_vastatut_kysymykset(sanat)
print("Oikein vastattujen kysymysten määrä:", oikein_vastatut)
print(len(sanat))
