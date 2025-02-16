from collections import namedtuple

EllipticCurve = namedtuple("EllipticCurve", ["a", "b"])


def is_smooth(curve):
    """Memeriksa apakah kurva smooth."""
    discriminant = -16 * (4 * curve.a**3 + 27 * curve.b**2)
    return discriminant != 0


def test_point(curve, x, y):
    """Memeriksa apakah titik (x, y) berada pada kurva."""
    return y**2 == x**3 + curve.a * x + curve.b


def create_curve(a, b):
    """Membuat kurva eliptik dan memvalidasi ke-smooth-an."""
    curve = EllipticCurve(a, b)
    if not is_smooth(curve):
        raise ValueError(f"Kurva {curve} tidak smooth!")
    return curve


def curve_to_string(curve):
    """Representasi string dari kurva."""
    return f"y^2 = x^3 + {curve.a}x + {curve.b}"
