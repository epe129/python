# Tee ratkaisusi tähän:
class  Lukutilasto:
    def __init__(self):
        self.luvut = []
        self.summ = 0
        self.summ2 = 0
        self.l = 0
        self.parillinen = 0
        self.maara = 0
        
    def lisaa_luku(self, luku:int):
        self.luvut.append(luku)
    
    def lukujen_maara(self):
        
        return len(self.luvut)

       
    def parittomien_maara(self):
        for c in self.luvut:
            if c % 2 != 0:
                self.maara += c

        return self.maara

    def parillisten_maara(self):
        for c in self.luvut:        
            if c % 2 == 0:
                self.parillinen += c

        return self.parillinen        
    
    def summa(self):
        for c in self.luvut:
            self.summ += c

        return self.summ
    
    def keskiarvo(self):
        for i in self.luvut:
            self.summ2 += i
            self.l += 1
        if self.l == 0:
            return 0

        return self.summ2 / self.l

print("Anna lukuja: ") 

tilasto = Lukutilasto()

while True:       
    luku = int(input(""))

    if str(luku) == "-1":    
        break

    tilasto.lisaa_luku(luku)

print("Lukujen määrä:", tilasto.lukujen_maara())
print("Summa:", tilasto.summa())
print("Keskiarvo:", tilasto.keskiarvo())
print("Parillisten summa:", tilasto.parillisten_maara())
print("Parittomien summa:", tilasto.parittomien_maara())

