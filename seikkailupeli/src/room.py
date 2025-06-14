class Room:
    def __init__(self, name, description, exits, items=None):
        self.name = name
        self.description = description
        self.exits = exits  # esim. {"pohjoinen": "Olohuone"}
        self.items = items or []

    def describe(self):
        return f"{self.description}\nNäet: {', '.join(self.items) if self.items else 'ei mitään erityistä.'}"