import numpy as np
from multiply_matrices import multiply_matrices

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
result = multiply_matrices(matrix_a, matrix_b)
if result is not None:
    print("Hasil perkalian:")
    print(result)

# Input bukan matriks NumPy
try:
    multiply_matrices([1, 2, 3], matrix_b)
except TypeError as e:
    print(f"Error: {e}")

# Dimensi tidak kompatibel
matrix_c = np.array([[1, 2, 3], [4, 5, 6]])
try:
    multiply_matrices(matrix_a, matrix_c)
except ValueError as e:
    print(f"Error: {e}")

# Menangkap exception umum saat perkalian
matrix_d = np.array([[1, 2], [3, 4]])
matrix_e = np.array([5, 6, 7])  # seharusnya matrix 2D
try:
    multiply_matrices(matrix_d, matrix_e)
except ValueError as e:
    print(f"Error: {e}")
