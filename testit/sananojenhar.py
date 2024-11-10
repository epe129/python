def laske_oikein_vastatut_kysymykset(sanat):
    oikein_vastatut = 0
    kayttajan_vastaukset = {}
    for kysymys, oikea_vastaus in sanat.items():
        yritykset = 1
        while yritykset > 0:
            vastaus = input(kysymys + " ")
            kayttajan_vastaukset[kysymys] = vastaus
            if vastaus == oikea_vastaus:
                oikein_vastatut += 1
                break  # Siirry seuraavaan kysymykseen
            else:
                yritykset -= 1
                print("Väärä vastaus. Sinulla on", yritykset, "yritystä jäljellä.")
    return oikein_vastatut



sanat = {
    "Vad vill du göra i framtiden": "mitä haluat tehdä tulevaisuudessa",
    "bo, bor, bodde, bott på landet": "asua maalla",
    "bo i stan": "asua kaupungissa",
    "bo utomlands": "asua ulkomailla",
    "studera,studerar,studerade,studerat utomlands": "opiskella ulkomailla",
    "jobba, jobbar, jobbade, jobbat utomlands": "tehdä töitä ulkomailla",
    "vara, är, var, varit lycklig": "olla onnellinen",
    "ha, har, hade, haft en partner": "olla kuppani",
    "skaffa, skaffar, skaffade, skaffat barn": "hankkia lapsia",
    "ha en familj": "olla perhe",
    "vara rik": "olla rikas",
    "ha en hund": "olla (omistaa) koira",
    "leva, lever, levde, levt hälsosamt": "elää terveellisesti",
    "vara frisk": "olla terve",
    "ha ett bra jobb": "olla (omistaa) hyvä työ",
    "ha många vänner": "olla (omistaa) monta ystävää ",
    "ha ett eget hem": "olla (omistaa) oma koti",
    "resa, reser, reste, rest": "matkustaa",
    "skriva, skriver, skrev, skrivit": "kirjoittaa",
    "ett brev, brevet, brev, breven": "kirje",
    "till sig själv": "itselleen",
    "öppna, öppnar, öppnade, öppnat": "avata",
    "hoppas, hoppas, hoppades, hoppats": "toivoa",
    "träffas, träffas, träffades, träffats": "tavata (toisensa)",
    "en tofubiff, tofubiffen, tofubiffar, tofubiffarna": "tofupihvi",
    "tillsammans": "yhdessä",
    "eller": "tai/vai",
    "nu": "nyt",
    "i framtiden": "tulevaisuudessa",
    "en trädgård, trädgården, trädgårdar, trädgårdarna": "puutarha",
    "rolig, roligt ,roliga": "hauska",
    "en lön, lönen": "palkka",
    "trevlig, trevligt, trevliga": "mukava",
    "en jobbarkompis, jobbarkompisen, jobbarkompisar, jobbakompisarna": "työkaveri",
    "Toppen": "Huippua",
    "på något sätt": "jollain tavalla",
    "utomlands": "ulkomailla, ulkomaille",
    "fira, firar, firade, firat": "viettää",
    "säkert": " varmasti",
    "jul, julen": "joulu",
    "midsommar, midsommaren": "juhannus",
    "ibland": "joskus",
    "känna, känner, kände, känt sig": "tuntea (itsensä joksikin)",
    "lite rädd": "vähän peloissaan ",
    "tänka, tänker, tänkte, tänkt på": "ajatella jotakin",
    "stressa, stressar, stressade, stressat": "stressata",
    "utan": "vaan",
    "stark, starkt, starka": "vahva",
    "glad, glatt, glada": "iloinen",
    "lugn, lugnt, lugna": "rauhallinen",
    "tro, tror, trodde, trott": "uskoa, luulla",
    "nog": "kyllä, -kin",
    "ha det så bra": "pärjäile",
    "hälsningar": "terveisiä",


}

oikein_vastatut = laske_oikein_vastatut_kysymykset(sanat)
print("Oikein vastattujen kysymysten määrä:", oikein_vastatut)
print(len(sanat))
