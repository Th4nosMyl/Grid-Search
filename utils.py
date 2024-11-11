import math

class Utils:
    @staticmethod
    def distance(qx, qy, x, y):
        return math.sqrt((qx - x) ** 2 + (qy - y) ** 2)

# Δοκιμή της μεθόδου distance
print(Utils.distance(0.5, 0.5, 0.1, 0.1))
