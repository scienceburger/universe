import random


def random_point():
    random.seed("hello here's a seed")
    x = random.randrange(-1000, 1000)
    y = random.randrange(-1000, 1000)
    z = random.randrange(-1000, 1000)
    return Point(x, y, z)


class Game:
    def __init__(self):
        self.players = []
        self.planets = []

    def update(self):
        for p in self.planets:
            p.update()

        for p in self.players:
            p.update()

    def add_player(self, player):
        self.players.append(player)


class Player:
    def __init__(self, username: str):
        self.username = username
        self.display_name = username
        self.planets = []

    def update(self):
        for p in self.planets:
            print(p)

        return 0


class Planet:

    def __init__(self):
        pass


class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
