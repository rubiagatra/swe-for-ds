import logging
import math

# Konfigurasi logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class EllipticCurve:
    def __init__(self, a, b):
        """Inisialisasi kurva eliptik dalam bentuk Weierstrass."""
        self.a = a
        self.b = b
        self.discriminant = -16 * (4 * a**3 + 27 * b**2)
        if not self.is_smooth():
            raise ValueError(f"Kurva {self} tidak smooth!")
        logging.info(f"Kurva eliptik {self} berhasil diinisialisasi.")

    def is_smooth(self):
        """Memeriksa apakah kurva smooth."""
        return self.discriminant != 0

    def test_point(self, x, y):
        """Memeriksa apakah titik (x, y) berada pada kurva."""
        return y**2 == x**3 + self.a * x + self.b

    def __str__(self):
        """Representasi string dari kurva."""
        return f"y^2 = x^3 + {self.a}x + {self.b}"

    def __eq__(self, other):
        """Memeriksa kesamaan dua kurva."""
        if not isinstance(other, EllipticCurve):
            return False
        return (self.a, self.b) == (other.a, other.b)

    def add_points(self, p1, p2):
        """Menambahkan dua titik pada kurva.
        Menangani kasus titik di tak hingga dan titik ganda.
        """
        if p1 is None:  # Titik di tak hingga
            return p2
        if p2 is None:  # Titik di tak hingga
            return p1

        if p1 == p2:
            return self.double_point(p1)

        x1, y1 = p1
        x2, y2 = p2

        if x1 == x2:
            return None  # Titik di tak hingga (garis vertikal)

        try:
            slope = (y2 - y1) * pow(x2 - x1, -1, self.curve_order)  # Inverse modular
            x3 = (slope**2 - x1 - x2) % self.curve_order
            y3 = (slope * (x1 - x3) - y1) % self.curve_order
            return (x3, y3)
        except ZeroDivisionError as e:
            logging.exception(f"Terjadi kesalahan saat penambahan titik: {e}")
            raise

    def double_point(self, p):
        """Menggandakan sebuah titik pada kurva."""
        if p is None:
            return None  # Titik di tak hingga

        x, y = p

        try:
            slope = (3 * x**2 + self.a) * pow(
                2 * y, -1, self.curve_order
            )  # Inverse modular
            x3 = (slope**2 - 2 * x) % self.curve_order
            y3 = (slope * (x - x3) - y) % self.curve_order
            return (x3, y3)
        except ZeroDivisionError as e:
            logging.exception(f"Terjadi kesalahan saat penggandaan titik: {e}")
            raise

    def set_curve_order(self, n):
        """Untuk set orde kurva, hanya dipanggil sekali saat inisialisasi."""
        self.curve_order = n
