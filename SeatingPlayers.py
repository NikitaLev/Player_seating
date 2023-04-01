import random
import numpy as np


class SeatingPlayers:
    def __init__(self, list_players, game_count):
        self.list_players = list_players
        self.list_game_seating = {}

        for i in range(0, game_count):
            self.random_seating(list_players)
        print()
        print(self.list_game_seating)
        self.write_game_list_exl_f()

    def random_seating(self, list_players):
        length = len(list_players)

        list_temp = list_players.copy()
        list_res = []
        try_count = 0
        while len(list_temp) > 0:
            rnd = random.randint(0, len(list_temp) - 1)

            temp = list_temp[rnd]
            if self.occurrence_check(temp, len(list_res)):
                try_count += 1
                if try_count > 20:
                    list_temp = list_players.copy()
                    try_count = 0
                    list_res = []
                continue

            list_res.append(temp)
            list_temp.pop(rnd)
        self.list_game_seating[len(self.list_game_seating)] = list_res

    def occurrence_check(self, elem, index):
        for key in self.list_game_seating:
            # print('key=', key, 'index=', index)
            # print('item=', self.list_game_seating.get(key)[index], 'elem=', elem)

            if self.list_game_seating.get(key)[index] == elem:
                return True
            # print('vl=', self.list_game_seating.get(key))
            # print('item=', self.list_game_seating.get(key)[index])
        return False

    def write_game_list(self):
        for key in self.list_game_seating:
            print('key=', key, self.list_game_seating.get(key))

    def write_game_list_exl_f(self):
        mass = np.array(self.list_game_seating.get(0))
        print(type(mass))
        # mass = np.column_stack((mass, mass))
        # print(mass)
        for key in self.list_game_seating:
            if key == 0:
                continue
            mass = np.column_stack((mass, np.array(self.list_game_seating.get(key))))
            print('key=', key, self.list_game_seating.get(key))
        print(mass)
