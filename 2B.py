def default_rule(current_state, neighborhood):  # rule for Life Automata
    total = sum(neighborhood)
    if current_state == 1 and total < 2:  # underpopulation
        return 0

    if current_state == 1 and 2 <= total <= 3:  # proceeds to next generation
        return 1

    if current_state == 1 and total > 3:  # overpopulation
        return 0

    if current_state == 0 and total == 3:  # reproduction
        return 1
    return current_state


class CellularAutomata:
    def __init__(self, cells, rule=default_rule):
        self.cells = cells  # matrix any size
        self.N = len(cells)  # size of cells matrix
        self.rule = rule  # evolution rule

    def __str__(self):
        s = ''
        for cell_row in self.cells:
            s += str(cell_row) + '\n'
        return s

    def get_neighborhood(self, x, y):
        result = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                result.append(self.get_cell(i, j))
        return result

    def get_cell(self, x, y):
        xmod = x % self.N
        ymod = y % self.N
        return self.cells[xmod][ymod]

    def evolve(self):
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                neighborhood = self.get_neighborhood(i, j)
                self.cells[i][j] = self.rule(self.get_cell(i, j), neighborhood)
