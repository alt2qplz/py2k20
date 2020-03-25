import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
	'''Класс для управления ресурсами и поведением игры'''

	def __init__(self):
		'''Инициализирует игру и создает игровые ресурсы'''
		pygame.init()
		self.settings = Settings()

		# self.screen = pygame.display.set_mode(
		# 	(self.settings.screen_width, self.settings.screen_height))


		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height


		pygame.display.set_caption('Alien Invasion')

		self.ship = Ship(self)


	def run_game(self):
		'''запуска основного цикла игры'''
		while True:
			self._check_events()
			self._update_screen()
			self.ship.update()
			
	def _check_events(self):
		# Отслеживание событий клавиатуры и мыши
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		'''Реагирует на НАЖАТИЕ клавиш'''
		if event.key == pygame.K_RIGHT:
			# Переместить корабль вправо
			self.ship.moving_right = True
		if event.key == pygame.K_LEFT:
			# Переместить корабль вправо
			self.ship.moving_left = True
		if event.key == pygame.K_UP:
			# Переместить корабль вверх
			self.ship.moving_up = True
		if event.key == pygame.K_DOWN:
			# Переместить корабль вниз
			self.ship.moving_down = True
		if event.key == pygame.K_q:
			sys.exit()

	def _check_keyup_events(self, event):
		'''Реагирует на ОТПУСКАНИЕ клавиш'''
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		if event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		if event.key == pygame.K_UP:
			self.ship.moving_up = False
		if event.key == pygame.K_DOWN:
			self.ship.moving_down = False

	def _update_screen(self):
		# При каждом прохождении цикла перерисовывается экран
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		# Отображение последнего прорисованного экрана
		pygame.display.flip()


if __name__ == '__main__':
	# Создание экземпляра запуска игры
	ai = AlienInvasion()
	ai.run_game()