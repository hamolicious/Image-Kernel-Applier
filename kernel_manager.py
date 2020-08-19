import pygame
from math import sqrt

class Kernel():
    def __init__(self, *args, normalise=False):
        self.structure = args
        self.normalise = normalise

class PresetKernels():
    identity = Kernel(
        0, 0, 0,
        0, 1, 0,
        0, 0, 0
    )

    blur = Kernel(
        0.0625, 0.125, 0.0625,
        0.125 , 0.25 , 0.125,
        0.0625, 0.125, 0.0625
    )

    outline = Kernel(
        -1, -1, -1,
        -1,  8, -1,
        -1, -1, -1,
        normalise=True
    )

    sharpen = Kernel(
         0, -1,  0,
        -1,  5, -1,
         0, -1,  0
    )

    denoise = Kernel(
        1/9, 1/9, 1/9,
        1/9, 1/9, 1/9,
        1/9, 1/9, 1/9
    )

    highpass = Kernel(
         0, -1,  0,
        -1,  4, -1,
         0, -1,  0
    )

    lowpass = Kernel(
        -1/9, -1/9, -1/9,
        -1/9,  8/9, -1/9,
        -1/9, -1/9, -1/9
    )

class Image():
    def __init__(self, path, width=-1, height=-1):
        if type(path) is str:
            self.image = pygame.image.load(path)
        else:
            self.image = path

        if width > 0 and height > 0:
            self.image = pygame.transform.scale(self.image, (int(width), int(height)))

        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def to_bw(self):
        for y in range(1, self.height-1):
            for x in range(1, self.width-1):
                self.image.set_at((x, y), [sum(self.image.get_at((x, y))[0:3]) / 3 for _ in range(3)])

    def get_neighbours(self, x, y):
        neighbours = []

        for ny in range(y-1, y+2):
            for nx in range(x-1, x+2):
                neighbours.append(self.image.get_at((nx, ny)))

        return neighbours

    def apply_kernel(self, kernel, in_place=False):
        if not in_place:
            image = pygame.Surface((self.width, self.height))

        for y in range(1, self.height-1):
            for x in range(1, self.width-1):
                neighbours = self.get_neighbours(x, y)

                c = 0
                for kernel_val, colour in zip(kernel.structure, neighbours):
                    bw_val = sum(colour[0:3]) / 3
                    c += bw_val * kernel_val

                    if   c > 255:
                        c = 255
                    elif c < 0:
                        c = 0


                try:
                    if not in_place:
                        image.set_at((x, y), [c for _ in range(3)])
                    else:
                        self.image.set_at((x, y), [c for _ in range(3)])
                except TypeError:
                    print(c)        
                    quit()

        if not in_place:
            return Image(image)


