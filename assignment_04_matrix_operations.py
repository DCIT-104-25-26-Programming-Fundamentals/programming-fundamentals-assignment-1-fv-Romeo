# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

print("=" * 42)
print("Welcome to the Matrix Operations Calculator")
print("=" * 42)

def create_matrix(rows, columns):
    matrix = []
    for i in range(rows):
        row_values = input(f"Enter row {i+1}: ").split()
        row = []
        for j in range(columns):
            row.append(int(row_values[j]))
        matrix.append(row)

    return matrix

def display_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]:4}", end=" ")
        print()

def transpose_matrix(matrix):
    transpose = []

    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(columns):
        new_row = []

        for j in range(rows):
            new_row.append(matrix[j][i])

        transpose.append(new_row)

    return transpose

def add_matrices(matrix_a, matrix_b):
    result = []

    for i in range(len(matrix_a)):
        row = []

        for j in range(len(matrix_a[i])):
            row.append(matrix_a[i][j] + matrix_b[i][j])

        result.append(row)

    return result

def multiply_matrices(matrix_a, matrix_b):
    result = []

    rows_a = len(matrix_a)
    columns_a = len(matrix_a[0])
    columns_b = len(matrix_b[0])


    for i in range(rows_a):
        row = []

        for j in range(columns_b):
            total = 0

            for k in range(columns_a):
                total += matrix_a[i][k] * matrix_b[k][j]

            row.append(total)

        result.append(row)

    return result
