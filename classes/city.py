class City:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.distance = []
        self.tau = []
        self.eta = []

    def update_pheromone(self, j, pheromone_deposit, path, evaporation):
        self.tau[j - 1] += pheromone_deposit/path
        self.tau[j - 1] *= (1-evaporation)
