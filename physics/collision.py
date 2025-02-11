class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def intersects(self, other):
        return not (self.x > other.x + other.width or 
                    self.x + self.width < other.x or 
                    self.y > other.y + other.height or 
                    self.y + self.height < other.y)

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def intersects(self, other):
        if isinstance(other, Rect):
            # Circle-Rectangle collision
            closest_x = max(other.x, min(self.x, other.x + other.width))
            closest_y = max(other.y, min(self.y, other.y + other.height))
            distance_x = self.x - closest_x
            distance_y = self.y - closest_y
            return (distance_x ** 2 + distance_y ** 2) < (self.radius ** 2)

        elif isinstance(other, Circle):
            # Circle-Circle collision
            distance_x = self.x - other.x
            distance_y = self.y - other.y
            distance_squared = distance_x ** 2 + distance_y ** 2
            radius_sum = self.radius + other.radius
            return distance_squared < (radius_sum ** 2)

        return False

# Example usage
rect1 = Rect(0, 0, 10, 10)
rect2 = Rect(5, 5, 10, 10)
circle1 = Circle(10, 10, 5)
circle2 = Circle(12, 12, 3)

print(rect1.intersects(rect2))  # Output: True
print(circle1.intersects(circle2))  # Output: True
print(circle1.intersects(rect1))  # Output: True
