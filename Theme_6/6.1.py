class Parallelepiped:
    info = "['__init__', 'base_area_calculation', 'side_area_calculation', 'volume_calculation', ...]"

    def __init__(self, width, length, height):
        self.width = width
        self.base_length = length
        self.height = height

    # Метод подсчета объема
    def volume_calculation(self):
        volume = self.width * self.base_length * self.height

        return f'{self.width} · {self.base_length} · {self.height} = {volume}cm³'

    # Метод подсчета площади основания
    def base_area_calculation(self):
        base_area = self.width * self.base_length

        return f'{self.width} · {self.base_length} = {base_area}cm²'

    # Метод для подсчета площади боковой стороны
    def side_area_calculation(self):
        side_area = 2 * self.height * (self.width + self.base_length)

        return f'2 · {self.height} · ({self.width} + {self.base_length}) = {side_area}cm²'


volume_box = Parallelepiped(width=6, length=8, height=5).volume_calculation()
base_area_box = Parallelepiped(width=6, length=8, height=0).base_area_calculation()
side_area_box = Parallelepiped(width=6, length=8, height=5).side_area_calculation()

print(volume_box)
print(base_area_box)
print(side_area_box)
print(Parallelepiped.info)
