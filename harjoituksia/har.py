# tee ratkaisu tänne
def histogrammi(sana: str):
    kirjaimet = {}
    for kirjain in sana:
        if kirjain not in kirjaimet:
            kirjaimet[kirjain] = 0
        kirjaimet[kirjain] += 1
    
    for avain, arvo in kirjaimet.items():
        print(avain, "*"*arvo)

if __name__=="__main__":
    histogrammi("saippuakauppias")