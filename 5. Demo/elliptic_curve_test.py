import pytest
from elliptic_curve import EllipticCurve


def test_elliptic_curve_valid_input():
    curve = EllipticCurve(2, 3)
    assert str(curve) == "y^2 = x^3 + 2x + 3"
    assert curve.is_smooth()


def test_elliptic_curve_invalid_input():
    with pytest.raises(ValueError):
        EllipticCurve(0, 0)  # Kurva tidak smooth


def test_elliptic_curve_test_point():
    curve = EllipticCurve(2, 3)
    assert curve.test_point(1, 2) == False  # Titik tidak pada kurva


def test_elliptic_curve_equal():
    curve1 = EllipticCurve(2, 3)
    curve2 = EllipticCurve(2, 3)
    assert curve1 == curve2

    curve3 = EllipticCurve(3, 3)
    assert curve1 != curve3


def test_add_points():
    curve = EllipticCurve(2, 3)
    curve.set_curve_order(11)  # Orde kurva untuk contoh

    p1 = (2, 7)
    p2 = (3, 1)
    result = curve.add_points(p1, p2)
    assert result == (9, 2)  # Hasil yang benar

    # ... (Test titik di tak hingga sama seperti sebelumnya)

    # Test x1 == x2 (garis vertikal)
    p3 = (2, 4)
    assert curve.add_points(p1, p3) == None


def test_double_point():
    curve = EllipticCurve(2, 3)
    curve.set_curve_order(11)  # Orde kurva untuk contoh
    p = (2, 7)
    result = curve.double_point(p)
    assert result == (8, 9)  # Hasil yang benar

    assert curve.double_point(None) == None
