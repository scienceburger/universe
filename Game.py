import random


class Game:
    def __init__(self):
        self.players = []
        self.planets = []
        self.orders = []
        self.current_cycle = 0
        self.is_game_running = False

    def create_universe(self):
        planet_count = 1000
        for i in range(0, planet_count):
            self.planets.append(Planet(location=random_point()))

    def start_game(self):
        player_name = input("Define player name: ")
        self.players.append(Player(name=player_name))
        self.create_universe()
        self.is_game_running = True
        self.run()

    def stop_game(self):
        self.is_game_running = False

    def update(self):
        self.current_cycle += 1
        print(".", end='')

        if self.current_cycle >= 80:
            self.stop_game()

    def run(self):
        while self.is_game_running:
            self.update()


class Player:
    def __init__(self, name: str):
        self.name = name
        print(f"New player created: {self.name}")
        pass


class Point:
    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        self.x = x
        self.y = y
        self.z = z


def random_point():
    random.seed('hello world')
    r_x = random.randint(-10000, 10000)
    r_y = random.randint(-10000, 10000)
    r_z = random.randint(-10000, 10000)
    return Point(r_x, r_y, r_z)


class Planet:
    def __init__(self, location: Point):
        self.location = location


class Order:
    def __init__(self, name, player, cycles_left, planet):
        self.name = name
        self.player = player
        self.cycles_left = cycles_left
        self.planet = planet


if __name__ == "__main__":
    g = Game()
    g.start_game()


