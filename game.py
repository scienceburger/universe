import random


def random_point():
    random.seed("hello here's a seed")
    x = random.randrange(-1000, 1000)
    y = random.randrange(-1000, 1000)
    z = random.randrange(-1000, 1000)
    return Point(x, y, z)


def generate_random_planet():
    return Planet(random_point())


class Game:
    def __init__(self):
        self.players = []
        self.planets = []
        self.generate_galaxy(10000)

    def generate_galaxy(self, planet_count):
        print('Generating galaxy…')
        for i in range(0, planet_count):
            self.planets.append(generate_random_planet())

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
    def __init__(self, coord):
        self.player = None
        self.coord = coord


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
