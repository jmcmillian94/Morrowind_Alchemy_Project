from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes
 
pygame.init()
surface = pygame.display.set_mode((600, 400))
 
def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)
 
def search_ingredient():
    pass
 
def search_effect():
    mainmenu._open(effect)
 
 
mainmenu = pygame_menu.Menu('Morrowind Alchemy Helper', 600, 400, theme=themes.THEME_DARK)
mainmenu.add.button('Search by Ingredient', search_ingredient)
mainmenu.add.button('Search by Effect', search_effect)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)
 
effect = pygame_menu.Menu('choose an effect', 600, 400, theme=themes.THEME_DARK)
effect.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
 
mainmenu.mainloop(surface)