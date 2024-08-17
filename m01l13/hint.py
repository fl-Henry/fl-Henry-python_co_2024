
class Game:
    winner = '-'
    field = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-'],
    ]

    def __init__(self):
        ...

    def display(self):
        # Отобразить поле
        print(f"Игровое поле:"
              f"   1   2   3"
              f"1   {self.field[0][0]} | {self.field[1][0]} | {self.field[2][0]}"
              f"  -------------"
              f"2   - | X | -"
              f"  -------------"
              f"3   O | - | -"
              f"")

    def check(self) -> bool:
        # Проверка на победителя
        ...

    def check_coords(self, x, y):
        # Проверка корректности ввода координат
        ...

    def run(self):
        # Ход игры
        while not self.check():
            input

        print("Ура! Победил {}".format(self.winner))


if __name__ == '__main__':
    game = Game()
    game.run()

