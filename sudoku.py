__author__ = "luis m."

from square import Square


class Sudoku:

    def __init__(self, initial_solution):
        self._matrix_solution = initial_solution
        self._square_matrix = [3*[1] for i in range(3)]
        self.square_parser()

    def square_parser(self):
        square_column1, square_column2, square_column3 = [], [], []
        for count, row in enumerate(self._matrix_solution):
            square_column1.append(row[0:3])
            square_column2.append(row[3:6])
            square_column3.append(row[6:9])
            square_column1 = self.create_square(square_column1, count, 0)
            square_column2 = self.create_square(square_column2, count, 1)
            square_column3 = self.create_square(square_column3, count, 2)

    def see_solution(self):
        for i in range(3):
            for j in range(3):
                print(self._square_matrix[i][0].current_solution[j][:],
                      self._square_matrix[i][1].current_solution[j][:],
                      self._square_matrix[i][2].current_solution[j][:])

    def create_square(self, square_column, count, column):
        if count in [2, 5, 8]:
            self._square_matrix[count // 3][column] = Square(square_column, (count // 3, column))
            return []
        return square_column

    def get_neighbour_squares_idx(self, pos):
        """ Return the indices of the neighbours square
            The first 2 are the horizontal neighbour and
            The last 2 are the vertical neighbour"""
        if pos:
            possible_values = {0, 1, 2}
            col_variation = zip( [pos[0], pos[0]], possible_values - {pos[1]} )
            row_variation = zip( possible_values - {pos[0]}, [pos[1], pos[1]] )
            return list(col_variation), list(row_variation)

    def position_surroundings(self, neighbour_pos, missed_value):
        """ Get the position of the missed_value in all square neighbors"""
        pos = []
        for x, y in neighbour_pos:
            position = self._square_matrix[x][y].get_pos_from_number(missed_value)
            if position:
                pos.append(position)
        return pos

    def scan(self, position_list, dir):
        cant_go_indices = set()
        for pos in position_list:
            if dir:
                select = zip([pos[0], pos[0], pos[0]], [0, 1, 2])
            else:
                select = zip([0, 1, 2], [pos[1], pos[1], pos[1]])
            cant_go_indices = cant_go_indices | set(select)
        return cant_go_indices


    def solver(self):
        iter_ = 150
        for it in range(iter_):
            for i in range(3):
                for j in range(3):
                    current_square = self._square_matrix[i][j]
                    horizontal_neighbour_pos, vertical_neighbour_pos = self.get_neighbour_squares_idx((i, j))
                    missing_values = current_square.missing_values()
                    for missed_value in missing_values:
                        position_list_horizontal = self.position_surroundings(horizontal_neighbour_pos, missed_value)
                        position_list_vertical = self.position_surroundings(vertical_neighbour_pos, missed_value)
                        cant_go_row = self.scan(position_list_horizontal, dir=True)
                        cant_go_col = self.scan(position_list_vertical, dir=False)
                        total_cant_go_pos = cant_go_row | cant_go_col | current_square.get_taken_positions()
                        missing_val_pos = Square.missing_position(total_cant_go_pos)
                        current_square.update_square(missing_val_pos, missed_value)
        print("----------------------------------------------")
        self.see_solution()






