import random
import json


def random_point():
    random.seed('hello world')
    r_x = random.randint(-10000, 10000)
    r_y = random.randint(-10000, 10000)
    r_z = random.randint(-10000, 10000)
    return Point(r_x, r_y, r_z)


class Point:
    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        self.x = x
        self.y = y
        self.z = z


class Game:
    def __init__(self):
        self.players = []
        self.planets = []
        self.orders = []
        self.current_cycle = 0
        self.is_game_running = False
        self.building_list = None

    def load_building_list(self):
        with open('buildings.json', 'r') as data:
            self.building_list = json.load(data)

    def create_universe(self):
        planet_count = 1000
        for i in range(0, planet_count):
            self.planets.append(Planet(location=random_point()))

    def start_game(self):
        player_name = input("Define player name: ")
        self.players.append(Player(name=player_name, game=self))
        self.create_universe()
        self.load_building_list()
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
    def __init__(self, name: str, game: Game = None):
        self.name = name
        self.game = game
        self.credits = 0
        print(f"New player created: {self.name}")
        pass

    def update(self):
        print('---------------')
        print('Updating player')
        self.menu()

    def menu(self):
        menu = "[1] Build\n"
        menu += "[2] List current orders\n"
        menu += "[0] Other Actions…"
        print(menu)
        choice = input("Enter choice: ")

        choice = int(choice)

        if choice == 1:
            self.build()
        elif choice == 2:
            [print(order.name) for order in self.game.orders if order.player == self]

    def build(self):
        choices = list(self.game.building_list.keys())
        print('Which building do you want to build?')
        for i, c in enumerate(choices):
            print(f"{i} - {self.game.building_list[c]['name']}")

        choice = int(input("Enter choice: "))

        c_name = self.game.building_list[choices[choice]]['name']
        c_cycles = self.game.building_list[choices[choice]]['prod_time']

        self.game.orders.append(Order(player=self,
                                      order_type='building',
                                      name=c_name,
                                      cycles_left=c_cycles))
        return 0


class Planet:
    def __init__(self, location: Point):
        self.minerals = 0
        self.population = 0
        self.energy_prod = 0
        self.energy_storage = 0
        self.energy_storage_max = 0
        self.buildings = []
        self.location = location
        self.player = None

    def update(self):
        self.energy_storage += self.energy_prod


class Order:
    def __init__(self, name: str = None,
                 order_type: str = None,
                 player: Player = None,
                 cycles_left: int = 0,
                 planet: Planet = None):
        self.name = name
        self.player = player
        self.cycles_left = cycles_left
        self.planet = planet
        self.type = order_type

    def decrement_cycles(self):
        self.cycles_left -= 1


class Building:
    def __init__(self):
        self.name = None
        self.player = None
        self.planet = None
        self.energy_prod = 0
        self.energy_consumption = 0
        self.population_production = 0
        self.population_requirements = 0


if __name__ == "__main__":
    g = Game()
    g.start_game()
