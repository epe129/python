import random

# Lista elämänohjeita – voit lisätä omia!
ohjeet = [
    "Älä koskaan luota kirjastokorttiin ilman nimen tarkistusta.",
    "Jos kuulet ankan nauravan, juokse.",
    "Kengät eivät ole vain jaloille – ne ovat myös kannanotto.",
    "Jos mikroaaltouuni alkaa puhua, älä vastaa.",
    "Syö jäätelöä sateessa – se ei sula niin nopeasti.",
    "Tarkista aina, onko sohva elossa ennen kuin istut.",
    "Vessapaperi on maailman tärkein valuutta hätätilanteessa.",
    "Älä luota siihen, joka käyttää Crocseja häissä – tai ehkä juuri häneen pitäisi.",
    "Jos löydät salaisen oven – avaa se. Tai älä. Se on juuri siinä jutun juoni.",
    "Kahvi ei ratkaise kaikkea. Mutta se voi aloittaa ratkaisun."
]

# Valitaan sattumanvarainen ohje
valittu_ohje = random.choice(ohjeet)

# Tulostetaan se
print("\n🧠 Elämänohjeesi tänään:\n")
print(f"👉 {valittu_ohje}\n")
