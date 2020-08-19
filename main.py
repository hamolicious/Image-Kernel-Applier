import pygame
from time import time
from kernel_manager import Image, PresetKernels
from os import system ; system('cls')

#region pygame init
pygame.init()
size = (600*2, 600)
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
pygame.display.set_icon(screen)
clock, fps = pygame.time.Clock(), 0

delta_time = 0 ; frame_start_time = 0
#endregion

path = 'path_to_your_image'
image1 = Image(path, size[0]/2, size[1])
image1.to_bw()
image2 = Image(image1.image, size[0]/2, size[1])

image2.apply_kernel(PresetKernels.blur, in_place=True)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    frame_start_time = time()
    screen.fill(0)

    screen.blit(image1.image, (0, 0))
    screen.blit(image2.image, (int(size[0]/2), 0))

    pygame.display.update()
    clock.tick(fps)
    delta_time = time() - frame_start_time
    pygame.display.set_caption(f'Framerate: {int(clock.get_fps())}')






