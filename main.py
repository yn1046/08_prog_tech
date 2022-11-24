from typing import *

Vector = List[float]
Matrix = List[Vector]


def print_matrix(matrix: Matrix):
    for line in matrix:
        for n in line:
            print(n, end=' ')
        print()


def solve_gauss(given_matrix: Matrix) -> Vector:
    # Copy to avoid changing the original matrix
    matrix = [line[:] for line in given_matrix]

    # Forward elimination
    for i in range(len(matrix) - 1):
        for k in range(i + 1, len(matrix)):
            coeff = matrix[k][i] / matrix[i][i]
            for j in range(len(matrix[0])):
                matrix[k][j] -= coeff * matrix[i][j]

    # Back substitution
    result = [.0 for line in matrix]
    for i in range(len(matrix) - 1, -1, -1):
        substituted = 0
        for j in range(i + 1, len(matrix[0]) - 1):
            substituted += matrix[i][j] * result[j]

        result[i] = (matrix[i][-1] - substituted) / matrix[i][i]

    return result


def solve_cramer(given_matrix: Matrix) -> Vector:
    def det(matrix: Matrix) -> float:
        if len(matrix) == 1:
            return matrix[0][0]
        elif len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            answer = 0
            for j in range(len(matrix[0])):
                minor_here = minor(matrix, 0, j)
                answer += (-1) ** j * matrix[0][j] * det(minor_here)

            return answer

    # ix — excluded i
    # jx — excluded j
    def minor(matrix: Matrix, ix: int, jx: int) -> Matrix:
        return [
            [
                matrix[i][j] for j in range(len(matrix[i])) if j != jx
            ] for i in range(len(matrix)) if i != ix
        ]

    def substitute(matrix: Matrix, column: Vector, index: int) -> Matrix:
        return [
            [
                matrix[i][j] if j != index else column[i]
                for j in range(len(matrix[i]))
            ] for i in range(len(matrix))
        ]

    result = [.0 for line in given_matrix]
    main_matrix: Matrix = [line[:-1] for line in given_matrix]
    free_members: Vector = [line[-1] for line in given_matrix]
    for i in range(len(given_matrix)):
        substituted = substitute(main_matrix, free_members, i)
        result[i] = det(substituted) / det(main_matrix)

    return result


with open('matrix.tsv', 'r') as f:
    matrix_inp: Matrix = [[float(n) for n in line.split('\t')] for line in f]

    print_matrix(matrix_inp)

    gauss_result = solve_gauss(matrix_inp)
    print('\n\n[GAUSSIAN ELIMINATION:]')
    for x in gauss_result:
        print(x, end=' ')

    cramer_result = solve_cramer(matrix_inp)
    print('\n\n[CRAMER\'S RULE:]')
    for x in cramer_result:
        print(x, end=' ')
