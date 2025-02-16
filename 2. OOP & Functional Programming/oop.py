class EllipticCurve:
    def __init__(self, a, b):
        """Inisialisasi kurva eliptik dalam bentuk Weierstrass."""
        self.a = a
        self.b = b
        self.discriminant = -16 * (4 * a**3 + 27 * b**2)
        if not self.is_smooth():
            raise ValueError(f"Kurva {self} tidak smooth!")

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
        return (self.a, self.b) == (other.a, other.b)
