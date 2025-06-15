class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.inventory = []
        self.score = 0  # Pelaajan pisteet

    def add_score(self, points):
        self.score += points