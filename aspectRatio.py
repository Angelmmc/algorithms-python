import math

class AspectRatioConverter:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def convert_to_16_9(self):
        """Convert the resolution to a 16:9 aspect ratio while keeping the height constant."""
        new_width = math.ceil(self.height * 16 / 9)
        return new_width, self.height

# Ejemplo de uso
res = AspectRatioConverter(1440, 1080)
new_resolution = res.convert_to_16_9()
print(f"Nueva resolución con aspecto 16:9: {new_resolution}")
