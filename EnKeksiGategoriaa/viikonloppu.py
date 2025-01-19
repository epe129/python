# kertoo kumman viikonloppu
import datetime

päivä = datetime.datetime.today()
viikko = päivä.isocalendar()[1]

if viikko % 2 == 0:
    print("Äiti viikonloppu")
else:
    print("Iskä viikonloppu")
