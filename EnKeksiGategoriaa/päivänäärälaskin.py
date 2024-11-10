import datetime

annapäivämäärä = input("Anna päivämäärä (dd/mm/yyyy): ")

aika = datetime.datetime.strptime(annapäivämäärä, '%d.%m.%Y')

aikanyt = datetime.datetime.now()

päivää = aika - aikanyt

print(f"Päivien ero: {päivää.days}")

