from pico2d import load_image


class Grass:
    def __init__(self):
        self.image1 = load_image('grass.png')
        self.image2 = load_image('grass.png')

    def draw(self):
        self.image1.draw(400, 30)
        self.image2.draw(400, 10)

    def update(self):
        pass
