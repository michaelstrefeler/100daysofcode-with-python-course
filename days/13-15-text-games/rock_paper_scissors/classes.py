# classes.py
# classes for rock paper scissors


class Roll:
    def __init__(self, name, wins, loses):
        self.name = name
        self.wins = wins
        self.loses = loses

    def can_defeat(self, roll):
        return True if roll.name in self.wins else False


class Player:
    def __init__(self, name, points=0):
        self.name = name
        self.points = points

    def get_points(self):
        return self.points

    def add_point(self):
        self.points += 1
