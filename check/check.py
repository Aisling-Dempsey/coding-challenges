"""Given a chessboard with one K and one Q, see if the K can attack the Q.

This function is given coordinates for the king and queen on a chessboard.
These coordinates are given as a letter A-H for the columns and 1-8 for the
row (see below for example):

Queens can move in any direction: horizontally, vertically, or diagonally,
as far as possible.

This function returns True if the king is in the line of attack of the queen.

For example, these boards show the king under attack:

8    . . . . . . . .      . . . . . . . .      . . . . . . . .    8
7    . . . . . . . .      . . . . . . . .      . K . . . . . .    7
6    . . . K . . . Q      . . . . K . . .      . . . . . . . .    6
5    . . . . . . . .      . . . . . . . .      . . . Q . . . .    5
4    . . . . . . . .      . . . . Q . . .      . . . . . . . .    4
3    . . . . . . . .      . . . . . . . .      . . . . . . . .    3
2    . . . . . . . .      . . . . . . . .      . . . . . . . .    2
1    . . . . . . . .      . . . . . . . .      . . . . . . . .    1
     A B C D E F G H      A B C D E F G H      A B C D E F G H

     K=D6, Q=H6           K=E6, Q=E4           K=B7, Q=D5

>>> check("D6", "H6")
True

>>> check("E6", "E4")
True

>>> check("B7", "D5")
True

>>> check("A1", "H8")
True

>>> check("A8", "H1")
True

>>> check("D6", "H7")
False

>>> check("E6", "F4")
False
"""


def check(king, queen):
    """Given a chessboard with one K and one Q, see if the K can attack the Q.

    This function is given coordinates for the king and queen on a chessboard.
    These coordinates are given as a letter A-H for the columns and 1-8 for the
    row, likr "D6" and "B7":
    """

    # checks if in-line horizontally or vertically
    if king[0] == queen[0] or king[1] == queen[1]:
        return True

    king = (ord(king[0]) - ord("A") + 1, int(king[1]))
    queen = (ord(queen[0]) - ord("A") + 1, int(queen[1]))

    # if difference in x is equal to difference in y it is able to reach diagonally.
    return abs(king[0] - queen[0]) == abs(king[1] - queen[1])



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. EXCELLENT GAME!\n"
