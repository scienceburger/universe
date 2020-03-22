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

        [player.update() for player in self.players]
        [order.decrement_cycles() for order in self.orders]

        if self.current_cycle >= 5:
            self.stop_game()

    def run(self):
        while self.is_game_running:
            self.update()


class Player:
    def __init__(self, name: str):
        self.name = name
        print(f"New player created: {self.name}")
        pass

    def update(self):
        print('Updating player')
        self.menu()

    def menu(self):
        menu = "[1] Build\n"
        menu += "[0] Other Actions…"
        print(menu)
        choice = input("Enter choice: ")

        if choice == 1:
            self.build()

    def build(self):
        print('building something')
        return 0

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
    def __init__(self, name: str = None, player: Player = None, cycles_left: int = 0, planet: Planet = None):
        self.name = name
        self.player = player
        self.cycles_left = cycles_left
        self.planet = planet

    def decrement_cycles(self):
        self.cycles_left -= 1


if __name__ == "__main__":
    g = Game()
    g.start_game()

