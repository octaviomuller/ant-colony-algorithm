import random
import numpy


class Ant:
    def __init__(self, start, allowed):
        self.start = start
        self.path = [start]
        self.current = start
        allowed.remove(self.start)
        self.allowed = allowed
        self.cost = 0

    def _select(self, cities, alpha, beta):
        probabilities = []
        for i in self.allowed:
            denominator = 0
            numerator = ((cities[self.current - 1].tau[i - 1] ** alpha)
                         * (cities[self.current - 1].eta[i - 1] ** beta))
            for city in self.allowed:
                denominator += ((cities[self.current - 1].tau[i - 1] ** alpha)
                                * (cities[self.current - 1].eta[i - 1] ** beta))
            probability = numerator/denominator
            probabilities.append(probability)
        move = numpy.random.choice(self.allowed, 1, probabilities)[0]
        return move

    def move(self, cities, alpha, beta):
        if len(self.allowed) > 0:
            move = self._select(cities, alpha, beta)
            self.allowed.remove(move)
            self.cost += cities[self.current - 1].distance[move - 1]
            self.current = move
            self.path.append(move)
        else:
            self.cost += cities[self.current - 1].distance[self.start - 1]
            self.current = self.start
            self.path.append(self.start)

    def reset(self, allowed):
        self.path = [self.start]
        self.current = self.start
        self.allowed = allowed
        self.allowed.remove(self.start)
        self.cost = 0
