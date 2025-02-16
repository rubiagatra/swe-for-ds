import numpy as np
import pytest
from multiply_matrices import multiply_matrices  # Import fungsi yang akan diuji


def test_multiply_matrices_valid_input():
    matrix_a = np.array([[1, 2], [3, 4]])
    matrix_b = np.array([[5, 6], [7, 8]])
    expected_result = np.array([[19, 22], [43, 50]])
    actual_result = multiply_matrices(matrix_a, matrix_b)
    np.testing.assert_array_equal(
        actual_result, expected_result
    )  # Gunakan assert dari numpy


def test_multiply_matrices_invalid_input_type():
    with pytest.raises(TypeError) as excinfo:
        multiply_matrices([1, 2, 3], np.array([[5, 6], [7, 8]]))
    assert str(excinfo.value) == "Input harus berupa matriks NumPy."  # cek pesan error


def test_multiply_matrices_zero_matrix():
    matrix_a = np.array([[0, 0], [0, 0]])
    matrix_b = np.array([[0, 0], [0, 0]])
    expected_result = np.array([[0, 0], [0, 0]])
    actual_result = multiply_matrices(matrix_a, matrix_b)
    np.testing.assert_array_equal(
        actual_result, expected_result
    )  # Gunakan assert dari numpy
