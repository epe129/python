# Tee ratkaisusi tähän:
class Sekuntikello:
    def __init__(self):
        self.sekunnit = 0
        self.minuutit = 0

    def tick(self):
        self.sekunnit += 1

        if self.minuutit == 59 and self.sekunnit == 60:
            self.sekunnit = 0 
            self.minuutit = 0 


        if self.sekunnit == 60:
            self.minuutit += 1
            self.sekunnit = 0


    def __str__(self):
        return f"{str(self.minuutit).zfill(2)}:{str(self.sekunnit).zfill(2)}"
    
if __name__ == "__main__":
    
    kello = Sekuntikello()

    for i in range(60*59+59):
        kello.tick()    
        print(kello)     
    kello.tick()
    print(kello)     