import random

wins = [[[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]]]


class Player:
    name = ""
    base = []

    def __init__(self, pr_name):
        self.name = pr_name
        self.base = []


def func_control(pr_base):

    control = True
    for rate in wins:
        control = True
        for i in range(len(rate)):
            if rate[i] not in pr_base:
                control = False
                break
        if control:
            break
    return control


def create_table():
    re_table = [["___", "___", "___"],
                ["___", "___", "___"],
                ["___", "___", "___"]]
    return re_table


def print_table(pr_table):
    print("   1   2   3")
    count = 1
    for i in pr_table:
        print(count, *i, end="\n\n")
        count += 1


def is_empty(pr_row, pr_col):
    if [pr_row, pr_col] in player1.base or [pr_row, pr_col] in player2.base:
        return True
    else:
        return False


def is_more_than_2(pr_row, pr_col):
    if pr_row > 2 or pr_col > 2:
        return True
    else:
        return False


def is_not_int(pr_row, pr_col):
    try:
        _ = int(pr_row)
        _ = int(pr_col)
    except ValueError:
        return True

    return False
if __name__ == '__main__':
    table = create_table()
    player1 = Player(input("Player 1 name:"))
    player2 = Player(input("Player 2 name:"))
    while player1.name == player2.name:
        print("Names can not be same,write player 2 name again")
        player2.name = input()

    print_table(table)

    counter = random.randrange(0, 2)
    while True:
        if counter % 2 == 0:
            print(player1.name, "turn!")

            temp_row = input("Enter row number: ")
            temp_col = input("Enter column number: ")

            while is_not_int(temp_row, temp_col):
                print("Please integer 1-3")
                temp_row = input("Enter row number again: ")
                temp_col = input("Enter column number again: ")

            row = int(temp_row) - 1
            column = int(temp_col) - 1

            while is_more_than_2(row, column):
                print("Can not be more 2")
                row = int(input("Enter row number again: ")) - 1
                column = int(input("Enter column number again: ")) - 1

            while is_empty(row, column):
                print("Can not be same place!")
                row = int(input("Enter row number again: ")) - 1
                column = int(input("Enter column number again: ")) - 1

            player1.base.append([row, column])
            table[row][column] = " X "
            print_table(table)
            if func_control(player1.base):
                print(player1.name, "won!")
                break
        else:
            print(player2.name, "turn!")

            temp_row = input("Enter row number: ")
            temp_col = input("Enter column number: ")

            while is_not_int(temp_row, temp_col):
                print("Please integer 0-3")
                temp_row = input("Enter row number again: ")
                temp_col = input("Enter column number again: ")

            row = int(temp_row) - 1
            column = int(temp_col) - 1

            while is_more_than_2(row, column):
                print("Can not be more 2")
                row = int(input("Enter row number again: ")) - 1
                column = int(input("Enter column number again: ")) - 1

            while is_empty(row, column):
                print("Can not be same place!")
                row = int(input("Enter row number again: ")) - 1
                column = int(input("Enter column number again: ")) - 1

            player2.base.append([row, column])
            table[row][column] = " O "
            print_table(table)
            if func_control(player2.base):
                print(player2.name, "won!")
                break
        counter += 1





