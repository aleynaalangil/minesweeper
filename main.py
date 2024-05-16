import random

max_mines = 5
rows, cols = (4, 5)
mine_field = [[0 for i in range(cols)] for j in range(rows)]
play_field = [["X" for i in range(cols)] for j in range(rows)]


def print_mine_field():
    print("Mine Field")
    print("  ", end="")
    print(" ".join(str(i) for i in range(cols)))
    for i in range(rows):
        print(i, end=" ")
        for j in range(cols):
            print(mine_field[i][j], end=" ")
        print()


def print_play_field():
    print("Play Field")
    print("  ", end="")
    print(" ".join(str(i) for i in range(cols)))
    for i in range(rows):
        print(i, end=" ")
        for j in range(cols):
            print(play_field[i][j], end=" ")
        print()


def insert_mines():
    mines_to_insert = 0
    while mines_to_insert < max_mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        if mine_field[row][col] == 0:
            mine_field[row][col] = 1
            mines_to_insert += 1


def check_neighbor_count(row, col):
    count = 0
    for i in range(max(row - 1, 0), min(row + 2, rows)):
        for j in range(max(col - 1, 0), min(col + 2, cols)):
            if (i, j) != (row, col) and mine_field[i][j] == 1:
                count += 1
    return count


def minesweeper():
    mine_found = False
    cleared = 0
    while cleared < rows * cols - max_mines:
        print_play_field()
        row, col = get_input()

        if row < 0 or row >= rows or col < 0 or col >= cols:
            print("Invalid input, try again.")
            continue

        if mine_field[row][col] == 1:
            play_field[row][col] = "1"
            mine_found = True
            break
        else:
            cleared += 1
            neighbor_count = check_neighbor_count(row, col)
            play_field[row][col] = str(neighbor_count) if neighbor_count > 0 else "0"
            print("Cleared:", cleared)

    print_play_field()

    if mine_found:
        print("YOU LOST")
    else:
        print("YOU WON")

    print_mine_field()


def get_input():
    row_col = input("Enter row and column (e.g., '0 0', to quit the game please type 'Q' or 'q'): ").split()

    if row_col[0].lower() == 'q':
        print("You have quit the game.")
        exit()

    row, col = row_col

    if len(row_col) != 2:
        print("Invalid input! Please enter both row and column indices separated by space.")
        return get_input()

    try:
        row = int(row)
        col = int(col)
    except ValueError:
        print("Invalid input! Please enter valid integers for row and column indices.")
        return get_input()

    if row < 0 or row >= rows or col < 0 or col >= cols:
        print("Invalid input! Please enter a number between 0 and 3 for the row and between 0 and 4 for the columns, "
              "try again.")
        return get_input()
    elif play_field[row][col] != "X":
        print("You have already cleared this cell, try again.")
        return get_input()

    return row, col


insert_mines()
minesweeper()
