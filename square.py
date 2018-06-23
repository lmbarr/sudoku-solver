__author__ = "luis m."

from itertools import product


class Square(object):
    """docstring for Square"""

    def __init__(self, initial_solution, pos):
        self._current_solution = initial_solution
        self._position = pos # base zero index position

    def missing_values(self):
        """Get all the empty values inside the square"""
        flattened_list = [y for x in self._current_solution for y in x]
        return list( set(range(1, 10)) - set(flattened_list) )

    def update_square(self, pos, val):
        if len(pos) > 0:
            x, y = pos
            self._current_solution[x][y] = val

    @property
    def current_solution(self):
        """Get current square solution."""
        return self._current_solution

    def get_pos_from_number(self, number):
        for i, row in enumerate(self._current_solution):
            for j, col in enumerate(row):
                if number == col:
                    return (i, j)
        return None

    def get_taken_positions(self):
        d = set()
        for i, row in enumerate(self._current_solution):
            for j, col in enumerate(row):
                if col != -1:
                    d.add((i, j))
        return d

    @staticmethod
    def missing_position(position_set):
        """ Detect one missing position on position_set.
            position_set contains the position for taken values and
            the position of cant_go for current value"""

        if len(position_set) == 8:
            missing_pos = set(product([0, 1, 2], [0, 1 ,2])) - position_set
            return missing_pos.pop()
        else:
            return ()


