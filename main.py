import math
import random
from classes.city import City
from classes.ant import Ant


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
        city.pheromone = [1 / (len(cities) * len(cities)) for i in range(len(cities))]
    aco(100, 100, cities, 0.9, 1.0, 2, 1.0)


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


def aco(iterations, ant_count, cities, pheromone_intensity, alpha, beta, rho):
    best_cost = 0
    best_path = []

    for i in range(iterations):
        ants = [Ant(cities[random.randint(0, len(cities) - 1)].id,
                    [i + 1 for i in range(len(cities))], alpha, beta) for i in range(ant_count)]
        for index, ant in enumerate(ants):
            cost = 0
            for moving_count in range(len(ant.allowed) + 1):
                ant.move(cities)
            if index == 0:
                best_cost = ant.cost
                best_path = ant.path
            else:
                if ant.cost < best_cost:
                    best_cost = ant.cost
                    best_path = ant.path
        # Aqui entra o algoritmo para atualizar os feromônios
    print('cost: ', best_cost)
    print('path: ', best_path)


if __name__ == '__main__':
    main()
