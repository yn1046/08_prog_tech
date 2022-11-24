from typing import *


def print_matrix(matrix: List[List[float]]):
    for line in matrix:
        for n in line:
            print(n, end=' ')
        print()


def solve_gauss(given_matrix: List[List[float]]) -> List[float]:
    # Copy to avoid changing the original matrix
    matrix = [line[:] for line in given_matrix]

    # Forward elimination
    for i in range(len(matrix)-1):
        for k in range(i+1, len(matrix)):
            coeff = matrix[k][i] / matrix[i][i]
            for j in range(len(matrix[0])):
                matrix[k][j] -= coeff * matrix[i][j]

    # Back substitution
    result = [.0 for line in matrix]
    for i in range(len(matrix)-1, -1, -1):
        substituted = 0
        for j in range(i+1, len(matrix[0]) - 1):
            substituted += matrix[i][j] * result[j]

        result[i] = (matrix[i][-1] - substituted) / matrix[i][i]

    return result


with open('matrix.tsv', 'r') as f:
    matrix_inp: List[List[float]] = [[float(n) for n in line.split('\t')] for line in f]

    print_matrix(matrix_inp)

    gauss_result = solve_gauss(matrix_inp)
    print('\n\n[GAUSSIAN ELIMINATION:]')
    for x in gauss_result:
        print(x, end=' ')

