"""
skyscrapers.py

This module's purpose is to check if a given combination in scyscrapers game is a winning
combination.

Github repository:
https://github.com/bogdanmagometa/skyscrapers
"""

def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """

    with open(path, 'r') as infile:
        board = list(map(lambda line: line.strip(), infile.readlines()))

    return board


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """

    maximum = 0
    count = 0

    for char in input_line[1:-1]:
        height = int(char)
        if height > maximum:
            maximum = height
            count += 1

    return count == pivot


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*',
    ... '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*',
    ... '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*',
    ... '*2*1***'])
    False
    """

    for line in board[1:-1]:
        if '?' in line[1:-1]:
            return False

    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*',
    ... '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*',
    ... '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*',
    ... '*2*1***'])
    False
    """

    for line in board[1:-1]:
        line = line[1:-1]
        if len(set(line)) != len(line):
            return False

    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*',
    ... '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*',
    ... '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*',
    ... '*41532*', '*2*1***'])
    False
    """

    for line in board[1:-1]:
        left_num = line[0]
        right_num = line[-1]
        if left_num != '*':
            if not left_to_right_check(line, int(left_num)):
                return False
        if right_num != '*':
            if not left_to_right_check(line[::-1], int(right_num)):
                return False

    return True


def get_reversed_board(board: list):
    """
    Transpose a given board, so that the columns become rows and rows become columns.

    >>> get_reversed_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*',
    ... '*2*1***'])
    ['*44****', '*125342', '*23451*', '2413251', '154213*', '*35142*', '***5***']
    >>> get_reversed_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*',
    ... '*2*1***'])
    ['*44****', '*125342', '*23451*', '2413221', '154213*', '*35142*', '***5***']
    >>> get_reversed_board(['112', '235', '323'])
    ['123', '132', '253']
    >>> get_reversed_board(['13', '24'])
    ['12', '34']
    >>> get_reversed_board(['*'])
    ['*']
    """

    reversed_board = []

    for row in range(len(board[0])):
        reversed_board.append("")
        for column in board:
            reversed_board[-1] += column[row]

    return reversed_board


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height) and
    visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """

    reversed_board = get_reversed_board(board)

    return check_uniqueness_in_rows(reversed_board) and check_horizontal_visibility(reversed_board)


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """

    board = read_input(input_path)

    return check_not_finished_board(board) and check_uniqueness_in_rows(board) and \
                        check_horizontal_visibility(board) and check_columns(board)


if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))
