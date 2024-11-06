import math


class RectangularCoordinates:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_pos(self):
        return (self.x, self.y)

    def vertical_or_horizontal(self):
        if self.x == 0:
            return "It is on x-axis"

        elif self.y == 0:
            return "It is on y-axis"

        else:
            return "It is not"

    def get_quadrant(self) -> 1:
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        else:
            return 0

    def distance_to_origin(self) -> int:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def calculate_distance(self, coor: 'RectangularCoordinates') -> int:
        return math.sqrt((self.x - coor.x) ** 2 + (self.y - coor.y) ** 2)

    def angle_with_x_axis(self) -> int:
        if self.x == 0:
            if self.y > 0:
                return 90
            else:
                return 0
        elif self.y == 0:
            return 0
        else:
            return abs(math.degrees(math.atan(self.y / self.x)))
