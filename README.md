### Programming Technology lab №8
This program can solve systems of linear equations via 2 methods.

The first one is Gaussian elimination:
```python
def solve_gauss(given_matrix: Matrix) -> Vector:
```

The second one is Cramer's rule:
```python
def solve_cramer(given_matrix: Matrix) -> Vector:
```

It expects an augmented matrix in the tab-separated format: `matrix.tsv`