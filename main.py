import pygame
import pipboy as pip

if __name__ == "__main__":
    pygame.init()
    pipboy = pip.PipBoy()
    pipboy.run_loop()
