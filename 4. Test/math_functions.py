def add(x, y):
    """Menambahkan dua angka."""
    return x + y


def divide(x, y):
    """Membagi dua angka.
    Menaikkan ZeroDivisionError jika y == 0.
    """
    if y == 0:
        raise ZeroDivisionError("Tidak bisa dibagi dengan nol.")
    return x / y


def multiply(x, y):
    """Mengalikan dua angka."""
    return x * y
