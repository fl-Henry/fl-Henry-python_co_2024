class TicTacGame:
    def __init__(self):
        # Переменные
        self.board = [['-' for _ in range(3)] for _ in range(3)]  # print - for * in range 3 .. in range (3) = 3 x 3
        # self.board = [
        # ['-', '-', '-'],
        # ['-', '-', '-'],
        # ['-', '-', '-'],
        # ]
        self.current_player = "X"

    def print_board(self):
        # Дизайн и рендер игрового поля
        for row in self.board:
            print(" | ".join(row))
            print("-" * 10)

    def make_move(self, row, col):
        # Логика хода // Ставим марку только в том случае если координата не занята
        if self.board[row][col] == '-':
            self.board[row][col] = self.current_player
            return True
        return False

    def check(self):
        # Проверка на победителя
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '-':  # col
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '-':  # row
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '-':  # diag
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '-':  # diag
            return True
        return False

    def check_coords(self):
        # Проверка на ничью // Если нет пустых ячеек но никто не выиграл = ничья
        for row in self.board:
            if '-' in row:
                return False
        return True

    def switch_player(self):
        # Логика смены хода
        self.current_player = "O" if self.current_player == "X" else "X"

    def run(self):
        
        available = list(range(3))

        
        # Логика игры
        while not self.check():
            self.print_board()
            print(f"Ходит {self.current_player}.")
            try:
                row, col = map(int, input("Введите координаты (номер строки и столбца: 0, 1 или 2) разделенные пробелом: ").split())
            except ValueError:
                print(f'\n Ошибка.\n')
                continue

            if row not in available or col not in available:
                print("Неверные координаты. Введите корректныеы координаты.")
                continue

            if not self.make_move(row, col):
                print("Координата занята. Введите корректныеы координаты.")
                continue

            if self.check_coords():
                self.print_board()
                print("Ничья")
                break

            self.switch_player()

        self.print_board()
        print(f"Игрок {self.current_player} победил")


# Запустить игру
if __name__ == "__main__":
    game = TicTacGame()
    game.run()
    