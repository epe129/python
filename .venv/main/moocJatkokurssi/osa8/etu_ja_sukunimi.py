# Tee ratkaisusi tähän:
import string

class Henkilo:
    def __init__(self, nimi: str):
        self.nimi = nimi
    
    def anna_etunimi(self):
        split_text = ''.join(char if char not in string.whitespace else ' ' for char in self.nimi).split()
        return split_text[0]

    def anna_sukunimi(self):
        split_text = ''.join(char if char not in string.whitespace else ' ' for char in self.nimi).split()
        return split_text[1]


if __name__ == "__main__":
    pekka = Henkilo("Pekka Python")
    print(pekka.anna_etunimi())
    print(pekka.anna_sukunimi())

    pauli = Henkilo("Pauli Pythonen")
    print(pauli.anna_etunimi())
    print(pauli.anna_sukunimi())