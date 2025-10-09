import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        # 🧱 أولاً: اقتل الكويكب الحالي
        self.kill()

        # 🪨 لو الكويكب صغير جدًا، ماينقسمش
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # 📐 توليد زاوية عشوائية (بين 20 و 50 درجة)
        random_angle = random.uniform(20, 50)

        # 🔁 إنشاء اتجاهين جديدين بناءً على السرعة القديمة
        new_vector_1 = self.velocity.rotate(random_angle)
        new_vector_2 = self.velocity.rotate(-random_angle)

        # 📏 نصف قطر الكويكبات الجديدة
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # 🪨🪨 إنشاء كويكبين جديدين في نفس الموقع
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        # 🚀 تعيين السرعات الجديدة (أسرع شوية ×1.2)
        asteroid_1.velocity = new_vector_1 * 1.2
        asteroid_2.velocity = new_vector_2 * 1.2