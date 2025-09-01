nimi = input("Anna nimi: ")
ika = input("Anna ikäsi: ")

class AgeAndName:
    def __init__(self, age, name):
        self.name = name
        self.age = age

    def __str__(self):
        return f"hello {self.name}, {self.age}"
        
NimiJaIka = AgeAndName(nimi, ika)

print(NimiJaIka)

