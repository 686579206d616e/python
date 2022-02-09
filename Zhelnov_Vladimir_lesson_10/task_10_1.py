from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        if Matrix.valid_matrix(matrix):
            self.matrix = matrix
        else:
            raise ValueError("fail initialization matrix")

    def __str__(self) -> str:
        result = ""
        for row in self.matrix:
            result += format(f"| {' '.join(map(str, row))} |\r\n")
        return result

    def __add__(self, *args, **kwargs):
        add = args[0]
        for index, row in enumerate(self.matrix):
            for key, number in enumerate(row):
                self.matrix[index][key] += add.matrix[index][key]
        return str(self)

    @staticmethod
    def valid_matrix(matrix: List[List[int]]) -> bool:
        standart_len = len(matrix[0])
        for row in matrix:
            if len(row) != standart_len:
                return False
        return True

if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """


"""

| 1 2 |
| 3 4 |
| 5 6 |

| 7 7 |
| 7 7 |
| 7 7 |

Traceback (most recent call last):
ValueError: fail initialization matrix

Process finished with exit code 1

"""