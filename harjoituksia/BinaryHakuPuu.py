# käytetty nettiä apuna

class Puu:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def BinaryPuu(juuri, key):
    # Pohjatapaukset: juuri on nolla tai avain
    # on läsnä juurrilla
    if juuri is None or juuri.key == key:
        return juuri
    
    if juuri.key < key:
        return BinaryPuu(juuri.right, key)
    
    
    return BinaryPuu(juuri.left, key)
    
juuri = Puu(50)
juuri.left = Puu(30)
juuri.right = Puu(70)

print("found" if BinaryPuu(juuri, 70) else "not found")
