class Room:
    def __init__(self, name, description, exits, items=None, enemies=None):
        self.name = name
        self.description = description
        self.exits = exits  # esim. {"pohjoinen": "Olohuone"}
        self.items = items or []
        self.enemies = enemies or []  # Lista vihollisista

    def describe(self):
        enemy_text = f"Viholliset: {', '.join(self.enemies)}" if self.enemies else "Ei vihollisia."
        return f"{self.description}\n{enemy_text}\nNäet: {', '.join(self.items) if self.items else 'ei mitään erityistä.'}"