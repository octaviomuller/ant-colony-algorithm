import random


class Ant:
    def __init__(self, start, allowed, alpha, beta):
        self.start = start
        self.path = [start]
        self.current = start
        allowed.remove(self.start)
        self.allowed = allowed
        self.cost = 0
        self.alpha = alpha
        self.beta = beta

    def _select(self):
        return random.randint(0, len(self.allowed) - 1) # Precisa ser trocado para o algoritmo de Probabilidade

    def move(self, cities):
        if len(self.allowed) > 0:
            likely_move = self._select()
            move = self.allowed.pop(likely_move)
            self.cost += cities[self.current - 1].distance[move - 1]
            self.current = move
            self.path.append(move)
        else:
            self.cost += cities[self.current - 1].distance[self.start - 1]
            self.current = self.start
            self.path.append(self.start)
