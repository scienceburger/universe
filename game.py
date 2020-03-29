import random
from uuid import uuid4
from datetime import datetime, timedelta


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
        self.queue = Queue()

    def generate_galaxy(self, planet_count):
        print('Generating galaxy…')
        for i in range(0, planet_count):
            self.planets.append(generate_random_planet())

    def get_random_planet(self):
        r = random.randint(0, len(self.planets))
        return self.planets[r]

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
        self.buildings = []

    def add_building(self, building):
        self.buildings.append(building)


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Task:
    def __init__(self, name, player, planet, duration):
        self.name: name
        self.id = uuid4()
        self.player = player
        self.planet = planet
        self.duration = duration
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(duration)

    def is_task_complete(self):
        if self.end_date < datetime.now():
            return True
        else:
            return False

    def time_left(self):
        t_left = self.end_date - datetime.now()
        return t_left.seconds


class Queue:
    # task format: {name: str, id: int, player: Player, planet: Planet, start_date: date, end_date: date}
    def __init__(self):
        self.tasks = []

    def update(self):
        completed = []
        ongoing = []
        for t in self.tasks:
            if t.is_task_complete:
                completed.append(t)
            else:
                ongoing.append(t)

        self.tasks = completed
