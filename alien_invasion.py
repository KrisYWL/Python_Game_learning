import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from alien import *

def run_game():

	pygame.init()

	ai_settings = Settings()

	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

	pygame.display.set_caption("Alien Invasion")

	#创建一个外星人
	#alien = Alien(ai_settings,screen)

	#创建一艘飞船
	ship = Ship(ai_settings,screen)
	#创建一个用于存储子弹的编组
	bullets = Group()

	aliens = Group()
	#创建外星人群
	gf.create_fleet(ai_settings,screen,ship,aliens)

	while True:
		gf.check_events(ai_settings,screen,ship,bullets)

		
		ship.update()
		
		gf.update_bullets(aliens,bullets)

		gf.update_aliens(ai_settings,aliens)

		#每次循环都重新绘制屏幕
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)


run_game()