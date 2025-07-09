import datetime
from datetime import date

def syntyma_päivä():
    nykyaikak = date.today().month
    nykyaikap = date.today().day

    nykypäivä = ()
    y = list(nykypäivä)
    y.append(nykyaikap)
    y.append(nykyaikak)

    nykypäivä = tuple(y)

    
    """
    Kysyy käyttäjältä syntymäpäivän ja palauttaa sen datetime-oliona.
    """
    while True:
        try:
            späivä = ()
            syntymäpäivä_str = input("Anna syntymäpäivä (pp.kk.vvvv): ").strip()
            syntymäpäivä_strk = syntymäpäivä_str[2]
            syntymäpäivä_strp = syntymäpäivä_str[0]

            x = list(späivä)
            x.append(int(syntymäpäivä_strp))
            x.append(int(syntymäpäivä_strk))

            späivä = tuple(x)

            syntymäpäivä = datetime.datetime.strptime(syntymäpäivä_str, "%d.%m.%Y").date()
        except ValueError:
            print("Virheellinen päivämäärä. Yritä uudelleen.")
        
        if nykypäivä == späivä:
            print("Olet syntynyt tänään!")
            break
        else:
            print(f"Syntymäpäiväsi on {syntymäpäivä.strftime('%d.%m')}")
            print(f"Nykyinen päivä on {date.today().strftime('%d.%m')}")
            break

syntyma_päivä()