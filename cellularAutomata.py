# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
E = {
    "dead": 0,
    "alive": 1
}


def is_alive(current_state):
    return current_state == E["alive"]


def is_dead(current_state):
    return current_state == E["dead"]


def life_rule(current_state, neighborhood, verbose=False):
    total = sum(neighborhood)
    if is_alive(current_state) and total < 2:           # underpopulation
        if verbose:
            print("Cell: " + str(current_state))
            print("Neighboors: " + str(neighborhood))
            print("dead due to underpopulation")
        return E["dead"]

    if is_alive(current_state) and 2 <= total <= 3:     # proceeds to next generation
        if verbose:
            print("Cell: " + str(current_state))
            print("Neighboors: " + str(neighborhood))
            print("keeps living")
        return current_state

    if is_alive(current_state) and total > 3:           # overpopulation
        if verbose:
            print("Cell: " + str(current_state))
            print("Neighboors: " + str(neighborhood))
            print("dead due to overpopulation")
        return E["dead"]

    if is_dead(current_state) and total == 3:           # reproduction
        if verbose:
            print("Cell: " + str(current_state))
            print("Neighboors: " + str(neighborhood))
            print("is born")
        return E["alive"]
    if verbose:
        print("Cell: " + str(current_state))
        print("Neighboors: " + str(neighborhood))
        print("nothing happens")
    return current_state


class CellularAutomata:
    def __init__(self, cells):
        self.cells = cells  # matrix(100 x 100)
        self.rule = {}

    def __str__(self):
        s = ''
        for cell_row in self.cells:
            s += str(cell_row) + '\n'
        return s

    def evolve(self, verbose=False):
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                neighborhood = self.get_neighborhood(i, j)
                self.cells[i][j] = life_rule(self.get_cell(i, j), neighborhood, verbose)

    def show_neighborhood(self, x, y):
        result = ''
        print("getting neighborhood for cell: " + str(self.get_cell(x, y)))
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                result += str(self.get_cell(i, j))
            result += '\n'
        return result

    def get_neighborhood(self, x, y):
        result = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                result.append(self.get_cell(i, j))
        return result

    def get_cell(self, x, y):
        xmod = x % len(self.cells)
        ymod = y % len(self.cells)
        return self.cells[xmod][ymod]
