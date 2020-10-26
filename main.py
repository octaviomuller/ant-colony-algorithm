import math
import random
from classes.city import City
from classes.ant import Ant

ant_count = 10
iterations = 100
alpha = 0.1
beta = 2
initial_pheromone = 0.1
pheromone_constant = 10
pheromone_evaporation = 0.1


def main():
    cities = []
    with open('./tsp/att48.txt', 'r') as f:
        for line in f.readlines():
            city = line.split(' ')
            cities.append(
                City(int(city[0]), int(city[1]), int(city[2])))
    distances = distance_matrix(cities)
    for index, city in enumerate(cities):
        city.distance = distances[index]
        city.tau = [initial_pheromone for i in range(len(cities))]
        for i in city.distance:
            if i != 0:
                city.eta.append(1/i)
            else:
                city.eta.append(0)
    aco(cities)


def distance_matrix(cities):
    matrix = []
    for i in range(len(cities)):
        row = []
        for j in range(len(cities)):
            row.append(distance_between(cities[i], cities[j]))
        matrix.append(row)
    return matrix


def distance_between(city1, city2):
    return math.sqrt((city1.x - city2.x) ** 2 + (city1.y - city2.y) ** 2)


def aco(cities):
    best_cost = 0
    best_path = []
    allowed = [i + 1 for i in range(len(cities))]
    ants = [Ant(cities[random.randint(0, len(cities) - 1)].id, allowed.copy())
            for i in range(ant_count)]

    for i in range(iterations):
        for index, ant in enumerate(ants):
            cost = 0
            for moving_count in range(len(ant.allowed) + 1):
                ant.move(cities, alpha, beta)
            if index == 0:
                best_cost = ant.cost
                best_path = ant.path
            else:
                if ant.cost < best_cost:
                    best_cost = ant.cost
                    best_path = ant.path
            ant.reset(allowed.copy())

        for i in range(len(best_path) - 1):
            cities[i].update_pheromone(i + 1,
                                       pheromone_constant, best_cost, pheromone_evaporation)

    print('cost: ', best_cost)
    print('path: ', best_path)


if __name__ == '__main__':
    main()
