from player import Player

class Game:

    def __init__(self):
        self.players = []
        self.planets = []

    def update(self):

        for p in self.players:
            p.update()

        for p in self.planets:
            p.update()

    def add_player(self, player: Player):
        self.players.append(player)