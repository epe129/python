import random
import pyjokes

def read_finnish_jokes_from_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            jokes = file.readlines()
        return [joke.strip() for joke in jokes if joke.strip()]
    except FileNotFoundError:
        print(f"Tiedostoa ei löytynyt: {file_path}")
        return []

def get_random_english_joke():
    return pyjokes.get_joke(language="en")

if __name__ == "__main__":
    file_path = ".venv/main/jokes.txt"  # Adjust the path if needed
    finnish_jokes = read_finnish_jokes_from_file(file_path)
    
    if finnish_jokes:
        print("Tervetuloa vitsigeneraattoriin! / Welcome to the Joke Generator!")
        while True:
            user_input = input("\nPaina Enter saadaksesi vitsin tai kirjoita 'exit' lopettaaksesi: / Press Enter to hear a joke or type 'exit' to quit: ").strip().lower()
            if user_input == 'exit':
                print("Näkemiin! Toivottavasti pidit vitseistä! / Goodbye! Hope you enjoyed the jokes!")
                break
            print("\nVitsi suomeksi: / Joke in Finnish:")
            print(random.choice(finnish_jokes))
            print("\nVitsi englanniksi: / Joke in English:")
            print(get_random_english_joke())
    else:
        print("Ei vitsejä tiedostossa. / No jokes found in the file.")