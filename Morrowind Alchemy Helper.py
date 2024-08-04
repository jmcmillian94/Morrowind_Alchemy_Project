#import necessary libraries
from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes
from ingredients_dict import ingredients
from ingredients_dict import listOfEffects

#initialize pygame, game screen, and backgorund image
pygame.init()
surface = pygame.display.set_mode((1920,1080))
background_image = pygame.image.load('background.png')
background_image = pygame.transform.scale(background_image, (1920,1080))

#function used in loop that draws background image on screen
def draw_background():
    surface.blit(background_image, (0, 0))

#initialize pygame sound mixer and add background music
pygame.mixer.init()
pygame.mixer.music.load('explore.wav')
pygame.mixer.music.play(-1) 
initial_volume = 0.2
pygame.mixer.music.set_volume(initial_volume)

#create function that allows music to be toggled on and off
music_playing = True

def toggle_music():
    global music_playing
    if music_playing:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    music_playing = not music_playing

#creating a custom theme for pygame menus
custom_theme = themes.THEME_GREEN.copy()
custom_theme.background_color = (0,0,0,0)
custom_theme.title_font = pygame_menu.font.FONT_FIRACODE_BOLD_ITALIC
custom_theme.widget_font = pygame_menu.font.FONT_FIRACODE_BOLD_ITALIC
custom_theme.title_font_color = (0,0,0) 
custom_theme.widget_font_color = (0,0,0)
custom_theme.selection_color = (20,20,150)
custom_theme.widget_selection_effect = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15), arrow_right_margin=5, arrow_vertical_offset=0, blink_ms=2)
custom_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY

#functions needed for the ingredient search menu to work
def ingredient_menu():
    mainmenu._open(ingredient_submenu)
    
ingredient_result_label = None

def search_ingredient(selected, value):
    global ingredient_result_label
    potion_ingredient = value.lower()
    if potion_ingredient in ingredients:
        effects = ingredients[potion_ingredient]
        ingredient_result_label.set_title(', '.join(effects) if effects else 'No ingredients found.')
    else:
        ingredient_result_label.set_title('Ingredient not found. Please try again or type exit to return to previous menu.')

#functions needed for the effect search menu to work
def effect_menu():
    mainmenu._open(effect_submenu)

effect_result_label = None

def search_effect(selected, value):
    global effect_result_label
    potion_effect = value.lower()
    if potion_effect in listOfEffects:
        found_keys = [key for key, value in ingredients.items() if potion_effect in value]
        effect_result_label.set_title(', '.join(found_keys) if found_keys else 'No ingredients found.')
    else:
        effect_result_label.set_title('Effect not found. Please try again or type exit to return to previous menu.')

 
#creating the main menu
mainmenu = pygame_menu.Menu('Morrowind Alchemy Helper', 1920,1080, theme=custom_theme)
mainmenu.add.button('Search by Ingredient', ingredient_menu)
mainmenu.add.button('Search by Effect', effect_menu)
mainmenu.add.button('Music ON/OFF', toggle_music)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

#creating the effect search submenu
effect_submenu = pygame_menu.Menu('Potion Effect Search', 1920,1080, theme=custom_theme)
effect_submenu.add.dropselect(title='effect: ',items=[(effect, effect) for effect in listOfEffects],onchange=search_effect,selection_box_height=7)
effect_result_label = effect_submenu.add.label('Search results will appear here.', max_char=-1, wordwrap=True)

#creating the ingredient search submenu
ingredient_submenu = pygame_menu.Menu('Potion Ingredient Search', 1920,1080, theme=custom_theme)
ingredient_submenu.add.dropselect(title='ingredient: ',items=[(ingredient, ingredient) for ingredient in ingredients.keys()],onchange=search_ingredient,selection_box_height=7)
ingredient_result_label = ingredient_submenu.add.label('Search results will appear here.', max_char=-1, wordwrap=True)

#pygame loop
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    draw_background()
    mainmenu.update(events)
    mainmenu.draw(surface)
    pygame.display.flip()
