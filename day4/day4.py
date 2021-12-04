class Cell:
    def __init__(self, value):
        self.value = value
        self.selected = False

    def __str__(self):
        return f'[{str(self.value)}] ' if self.selected else f'{str(self.value)} '


class Board:
    width = 5

    def __init__(self, values):
        self.cells = [Cell(value) for value in values]
        self.score = 0
        self.winning_number = -1

    def __str__(self):
        result = ""
        for cell in self.cells:
            result += cell.__str__()
        return result

    def mark_number(self, num):
        for cell in self.cells:
            if num == cell.value:
                cell.selected = True
                if self.is_winner():
                    self.score = self.calc_score(num)
                    self.winning_number = num

    def is_winner(self):
        pos = 0
        while pos < Board.width:
            if self.cells[pos * Board.width].selected \
                    and self.cells[pos * Board.width + 1].selected \
                    and self.cells[pos * Board.width + 2].selected \
                    and self.cells[pos * Board.width + 3].selected \
                    and self.cells[pos * Board.width + 4].selected:
                return True
            if self.cells[pos].selected \
                    and self.cells[pos + Board.width * 1].selected \
                    and self.cells[pos + Board.width * 2].selected \
                    and self.cells[pos + Board.width * 3].selected \
                    and self.cells[pos + Board.width * 4].selected:
                return True
            pos += 1

    def calc_score(self, last_number):
        sum_of_unselected_cells = 0
        for cell in self.cells:
            sum_of_unselected_cells += 0 if cell.selected else cell.value
        return sum_of_unselected_cells * last_number


def read_selections(input_file):
    return [int(num) for num in input_file.readline().strip().split(",")]


def read_boards(input_file):
    boards = []
    line = input_file.readline()
    while line == '\n':
        values = [int(num) for num in input_file.readline().split()]
        values += [int(num) for num in input_file.readline().split()]
        values += [int(num) for num in input_file.readline().split()]
        values += [int(num) for num in input_file.readline().split()]
        values += [int(num) for num in input_file.readline().split()]
        boards.append(Board(values))
        line = input_file.readline()
    return boards


def read_input():
    with open("input.txt", "r") as input_file:
        selections = read_selections(input_file)
        boards = read_boards(input_file)
    return selections, boards


def play_round(selection, boards):
    for board in boards:
        board.mark_number(selection)
    winners = list(filter(lambda b: b.score > 0, boards))
    remaining = list(filter(lambda b: b.score == 0, boards))
    return winners, remaining


def play_game(selections, boards):
    winners = []
    remaining = boards
    for selection in selections:
        w, r = play_round(selection, remaining)
        winners += w
        remaining = r
    return winners


def main():
    selections, boards = read_input()
    winners = play_game(selections, boards)
    print(f'first winning board score: {winners[0].score}')
    print(f'last winning board score: {winners[len(winners) - 1].score}')


main()
