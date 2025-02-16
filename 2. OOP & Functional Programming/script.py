from oop import EllipticCurve

print("OOP")
curve = EllipticCurve(2, 3)
print(curve)
print(curve.is_smooth())
print(curve.test_point(1, 2))

try:
    curve_not_smooth = EllipticCurve(0, 0)
except ValueError as e:
    print(e)

print("OOP")
