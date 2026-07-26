# Tee ratkaisusi tähän:
class Sarja:
    def __init__(self, sarja, kaudet, genret):
        self.nimi = sarja
        self.kaudet = kaudet
        self.genret = genret
        self.arvostelut = []

    def arvostele(self, arvosana: int):
        self.arvostelut.append(arvosana)

    def __str__(self):
        merkkijono = ", ".join(self.genret)
        yhteen_arvostelut = 0
        for c in self.arvostelut:
            yhteen_arvostelut += c
        if not self.arvostelut:
            return f"""{self.nimi} ({self.kaudet} esityskautta)
    genret: {merkkijono}
    ei arvosteluja"""
        else: 
            return f"""{self.nimi} ({self.kaudet} esityskautta)
    genret: {merkkijono}
    arvosteluja {len(self.arvostelut)}, keskiarvo {yhteen_arvostelut / len(self.arvostelut):.1f} pistettä"""

def arvosana_vahintaan(arvosana: float, sarjat: list):
    tulos = []

    for sarja in sarjat:
        if not sarja.arvostelut:
            continue

        keskiarvo = sum(sarja.arvostelut) / len(sarja.arvostelut)

        if keskiarvo >= arvosana:
            tulos.append(sarja)    

    return tulos


def sisaltaa_genren(genre: str, sarjat: list):
    tulos = []
    
    for sarja in sarjat:
            if genre in sarja.genret:
                tulos.append(sarja)
            else:
                continue

    return tulos
    
if __name__ == "__main__":

    s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.arvostele(5)

    s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
    s2.arvostele(3)

    s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
    s3.arvostele(2)

    sarjat = [s1, s2, s3]

    print("arvosana vähintään 4.5:")
    for sarja in arvosana_vahintaan(4.5, sarjat):
        print(sarja.nimi)
    print("genre Comedy:")
    for sarja in sisaltaa_genren("Comedy", sarjat):
        print(sarja.nimi)