class Kello:
    def __init__(self, tunnit=0, minuutit=0, sekunnit=0):
        self.tunnit = tunnit
        self.sekunnit = sekunnit
        self.minuutit = minuutit

    def tick(self):

        self.sekunnit += 1
            
        if self.tunnit == 23 and self.minuutit == 59 and self.sekunnit == 60:
            self.tunnit = 0
            self.sekunnit = 0 
            self.minuutit = 0
            

        if self.minuutit == 59 and self.sekunnit == 60:
            self.sekunnit = 0 
            self.minuutit = 0 

        if self.sekunnit == 60:
            self.minuutit += 1
            self.sekunnit = 0
        
        if self.minuutit == 60:
            self.tunnit += 1


    
    def aseta(self, tunnit, minuutit):
        self.tunnit = tunnit
        self.minuutit = minuutit
        self.sekunnit = 0

    def __str__(self):
        return f"{str(self.tunnit).zfill(2)}:{str(self.minuutit).zfill(2)}:{str(self.sekunnit).zfill(2)}"

if __name__ == "__main__":
    
    kello = Kello(23, 59, 55)
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)

    kello.aseta(12, 5)
    print(kello)