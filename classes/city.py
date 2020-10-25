class City:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.distance = []
        # self.pheromone = [[1/(rank * rank) for i in range(rank)] for j in range(rank)]