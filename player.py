import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS

class Player(CircleShape):
    def __init__(self, x, y):
        # نستدعي الـ constructor بتاع CircleShape
        super().__init__(x, y, PLAYER_RADIUS)
        # اتجاه السفينة (بدرجات) - 0 يعني لفوق
        self.rotation = 0  

    # الدالة دي بترجع نقاط (vertices) المثلث اللي يرسم السفينة
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # نرسم المثلث كـ Polygon أبيض
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
