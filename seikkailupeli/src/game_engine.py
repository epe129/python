import json
import os

class Room:
    def __init__(self, name, description, exits, items=None):
        self.name = name
        self.description = description
        self.exits = exits  # esim. {"pohjoinen": "Olohuone"}
        self.items = items or []

    def describe(self):
        return f"{self.description}\nNäet: {', '.join(self.items) if self.items else 'ei mitään erityistä.'}"

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.inventory = []

class Game:
    def __init__(self):
        self.rooms = self.load_world()
        self.player = Player(current_room="Aula")
        # Lataa tallennettu peli jos save.json löytyy
        if os.path.exists("save.json"):
            self.load()

    def load_world(self):
        return {
            "Aula": Room("Aula", "Olet aulassa. Täällä on vanha matto ja ovi pohjoiseen.", {"pohjoinen": "Olohuone"}, items=["avain"]),
            "Olohuone": Room("Olohuone", "Tämä on pimeä olohuone. Seinällä on taulu.", {"etelä": "Aula"})
        }

    def process_command(self, command):
        verb, target = self.simple_parse(command)
        room = self.rooms[self.player.current_room]

        # Komento-ohjeet
        if verb in ("komennot", "apua", "help"):
            return (
                "Käytettävissä olevat komennot:\n"
                "- katso / tutki : kuvaile huonetta\n"
                "- poimi/ota [esine] : poimi esine\n"
                "- kävele [suunta] : siirry toiseen huoneeseen\n"
                "- avaa [kohde] : esim. avaa ovi\n"
                "- tavarat/inventory : näytä tavaraluettelosi\n"
                "- komennot/apua/help : näytä tämä ohje\n"
                "- tallenna : tallenna peli\n"
                "- lopeta/exit/poistu : lopeta peli"
            )

        elif verb in ("katso", "tutki"):
            return room.describe()

        elif verb in ("inventory", "tavarat"):
            return f"Sinulla on: {', '.join(self.player.inventory) if self.player.inventory else 'ei mitään'}"

        elif verb in ("poimi", "ota") and target in room.items:
            self.player.inventory.append(target)
            room.items.remove(target)
            return f"Poimit: {target}"

        elif verb == "kävele" and target in room.exits:
            self.player.current_room = room.exits[target]
            return f"Siirryit huoneeseen: {self.player.current_room}"

        elif verb == "avaa":
            # Esimerkkinä: oven avaaminen
            if target == "ovi" and self.player.current_room == "Aula" and "avain" in self.player.inventory:
                return "Avaat oven ja pääset olohuoneeseen!"
            elif target == "ovi" and self.player.current_room == "Aula":
                return "Ovi on lukossa. Tarvitset avaimen."
            else:
                return "Et voi avata sitä."

        elif verb in ("tallenna",):
            self.save()
            return "Peli tallennettu."

        elif verb in ("lopeta", "exit", "poistu"):
            self.save()
            return "Peli tallennettu ja lopetettu. Hei hei!"

        else:
            return "En ymmärrä mitä tarkoitit... (voit hakea ohjeen kirjoittamalla 'komennot')"

    def simple_parse(self, text):
        words = text.lower().split()
        if len(words) >= 2:
            return words[0], words[-1]
        elif words:
            return words[0], ""
        else:
            return "", ""

    def save(self):
        # Tallenna myös huoneiden esineet
        data = {
            "current_room": self.player.current_room,
            "inventory": self.player.inventory,
            "rooms": {name: room.items for name, room in self.rooms.items()}
        }
        with open("save.json", "w") as f:
            json.dump(data, f)

    def load(self):
        with open("save.json") as f:
            data = json.load(f)
        self.player.current_room = data["current_room"]
        self.player.inventory = data["inventory"]
        # Lataa huoneiden esineet
        for room_name, items in data.get("rooms", {}).items():
            if room_name in self.rooms:
                self.rooms[room_name].items = items