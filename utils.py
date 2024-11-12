import math

class Utils:
    """
    A utility class containing static methods for various calculations.
    """

    """
        Calculate the Euclidean distance between two points (qx, qy) and (x, y).

        Args:
            qx (float): The x-coordinate of the first point.
            qy (float): The y-coordinate of the first point.
            x (float): The x-coordinate of the second point.
            y (float): The y-coordinate of the second point.

        Returns:
            float: The Euclidean distance between the two points.
    """
    @staticmethod
    def distance(qx, qy, x, y):
        return math.sqrt((qx - x) ** 2 + (qy - y) ** 2)

# Δοκιμή της μεθόδου distance
print(Utils.distance(0.5, 0.5, 0.1, 0.1))
