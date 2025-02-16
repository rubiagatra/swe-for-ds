import numpy as np
import logging

# Konfigurasi logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def multiply_matrices(matrix1, matrix2):
    """
    Mengalikan dua matriks NumPy dengan logging.

    Args:
        matrix1: Matriks NumPy pertama.
        matrix2: Matriks NumPy kedua.

    Returns:
        Hasil perkalian matriks, atau None jika terjadi kesalahan.

    Raises:
        TypeError: Jika input bukan matriks NumPy.
        ValueError: Jika dimensi matriks tidak kompatibel untuk perkalian.
    """

    logging.info("Memulai perkalian matriks.")

    if not isinstance(matrix1, np.ndarray) or not isinstance(matrix2, np.ndarray):
        logging.error("Input bukan matriks NumPy.")
        raise TypeError("Input harus berupa matriks NumPy.")

    if matrix1.shape[1] != matrix2.shape[0]:
        logging.error("Dimensi matriks tidak kompatibel untuk perkalian.")
        raise ValueError("Dimensi matriks tidak kompatibel untuk perkalian.")

    try:
        result = np.dot(matrix1, matrix2)
        logging.info("Perkalian matriks berhasil.")
        return result
    except Exception as e:
        logging.exception(
            f"Terjadi kesalahan saat perkalian matriks: {e}"
        )  # Gunakan logging.exception untuk mencatat traceback
        return None
