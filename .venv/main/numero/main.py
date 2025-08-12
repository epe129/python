import phonenumbers
from phonenumbers import geocoder, carrier

# Syötä puhelinnumero kansainvälisessä muodossa (esim. +358xxxxxxxxx)
numero = input("Syötä puhelinnumero (esim. +358401234567): ")

try:
    parsed_numero = phonenumbers.parse(numero, None)

    # Tarkistetaan onko numero mahdollinen ja kelvollinen
    if not phonenumbers.is_possible_number(parsed_numero):
        print(f"Numero {numero} ei ole mahdollinen.")
    elif not phonenumbers.is_valid_number(parsed_numero):
        print(f"Numero {numero} ei ole kelvollinen.")
    else:
        # Maan tai alueen nimi ilman kielirajoitetta
        alue = geocoder.description_for_number(parsed_numero, "en")
        if alue:
            print(f"Numero kuuluu alueelle: {alue}")
        else:
            print("Aluetta ei löytynyt tai geokoodaus epäonnistui.")
        
        # Operaattori
        operaattori = carrier.name_for_number(parsed_numero, "en")
        if operaattori:
            print(f"Mahdollinen operaattori: {operaattori}")
        else:
            print("Operaattoria ei löytynyt.")

except Exception as e:
    print("Virhe numeron käsittelyssä:", e)
