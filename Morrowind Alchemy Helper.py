from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes
from ingredients_dict import ingredients
from ingredients_dict import listOfEffects

 
pygame.init()
surface = pygame.display.set_mode((1920, 1080))

background_image = pygame.image.load('morrowind_background.png')
background_image = pygame.transform.scale(background_image, (1920, 1080))

def draw_background():
    surface.blit(background_image, (0, 0))
 
def ingredient_menu():
    mainmenu._open(ingredient)
    
ingredient_result_label = None

def search_ingredient(input_text):
    global ingredient_result_label
    potion_ingredient = input_text.lower()
    if potion_ingredient in ingredients:
            effects = ingredients[potion_ingredient]
            ingredient_result_label.set_title(', '.join(ingredients[potion_ingredient]) if effects else 'No ingredients found.')
    else:
            ingredient_result_label.set_title('Effect not found. Please try again or type exit to return to previous menu.')   
 
def effect_menu():
    mainmenu._open(effect)

effect_result_label = None

def search_effect(input_text):
    global effect_result_label
    potion_effect = input_text.lower()
    if potion_effect in listOfEffects:
        found_keys = [key for key, value in ingredients.items() if potion_effect in value]
        effect_result_label.set_title(', '.join(found_keys) if found_keys else 'No ingredients found.')
    else:
        effect_result_label.set_title('Effect not found. Please try again or type exit to return to previous menu.')    



 
 
mainmenu = pygame_menu.Menu('Morrowind Alchemy Helper', 1024, 768, theme=themes.THEME_DARK)
mainmenu.add.button('Search by Ingredient', ingredient_menu)
mainmenu.add.button('Search by Effect', effect_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)


 
effect = pygame_menu.Menu('Potion Effect Search', 1024, 768, theme=themes.THEME_DARK)
effect.add.text_input(title='effect: ', cursor_selection_enable= True, copy_paste_enable= True, onreturn=search_effect)
effect_result_label = effect.add.label('Search results will appear here.')

ingredient = pygame_menu.Menu('Potion Ingredient Search', 1024, 768, theme=themes.THEME_DARK)
ingredient.add.text_input(title='effect: ', cursor_selection_enable= True, copy_paste_enable= True, onreturn=search_ingredient)
ingredient_result_label = ingredient.add.label('Search results will appear here.')

#mainmenu.mainloop(surface)

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