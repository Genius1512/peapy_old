from .__pygame import pygame


class PeaPy:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("PeaPy")
        self.clock = pygame.time.Clock()

    def update(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        self.delta = self.clock.tick(60) / 1000
        self.screen.fill((255, 255, 255))

        # Update objects

        pygame.display.update()
        return True

    def __repr__(self):
        return "peapy.PeaPy()"
