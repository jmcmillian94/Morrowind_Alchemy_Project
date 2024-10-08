from tkinter import *
from ingredients_dict import *
import pygame
import tkinter.font as tkfont

#making a root window
root = Tk()
root.title("Morrowind Alchemy Helper")
icon = PhotoImage(file='alchemy.png')
root.iconphoto(False, icon)
root.geometry("1200x400")
root.configure(bg='#af9667')

default_font = tkfont.Font(family="Cinzel", size=12)

# Set the default font for all widgets
root.option_add("*Font", default_font)

#initialize pygame mixer
pygame.mixer.init()

#fucntion that plays background music
def play_background_music():
    pygame.mixer.music.load("explore.wav")  # Load the music file
    pygame.mixer.music.play(-1)  # Play the music in a loop (-1 means infinite loop)

#set music volume
initial_volume = 0.2
pygame.mixer.music.set_volume(initial_volume)

#function that toggles music on/off
def toggle_music():
    if pygame.mixer.music.get_busy():  # Check if music is currently playing
        pygame.mixer.music.pause()  # Pause the music
    else:
        pygame.mixer.music.unpause()  # Unpause the music


# Create frames for layout
left_frame = Frame(root)
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")
left_frame.configure(bg='#af9667')

right_frame = Frame(root, bd=2, relief="sunken", width=230, height=350)
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ns")
right_frame.grid_propagate(False)


info_frame = Frame(root, bd=2, relief="sunken", width=230, height=350)
info_frame.grid(row=0, column=2, padx=10, pady=10, sticky="ns")
info_frame.grid_propagate(False) 

info_frame_2 = Frame(root, bd=2, relief="sunken", width=430, height=350)
info_frame_2.grid(row=0, column=3, padx=10, pady=10, sticky="ns")
info_frame_2.grid_propagate(False) 


Label(right_frame, text="Select an option from the Menu", wraplength=180).grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Function to clear right_frame
def clear_right_frame():
    for widget in right_frame.winfo_children():
        widget.destroy()


search_result = StringVar()
search_result.set("Search results will appear here.")
Label(info_frame, textvariable=search_result, wraplength=180, justify="left", anchor="nw").grid(row=0, column=0, padx=10, pady=10, sticky="nw")

search_result_2 = StringVar()
search_result_2.set("Restocking merchant info will appear here.")
Label(info_frame_2, textvariable=search_result_2, wraplength=400, justify="left", anchor="nw").grid(row=0, column=0, padx=10, pady=10, sticky="nw")

#Fuction that searches ingredient dict
def ingredient_search(value):
    global search_result
    global search_result_2
    potion_ingredient = value.lower()
    if potion_ingredient in ingredients:
        effects = ingredients[potion_ingredient]
        search_result.set('\n'.join(effects) if effects else 'No ingredients found.')
        merchant_locations = []
        for merchant, info in restock_merchants.items():
             if any(potion_ingredient in item for item in info['ingredients']):
                 merchant_locations.append(f'{merchant}, {info["location"]}')
        if merchant_locations:
            search_result_2.set('\n\n'.join(merchant_locations))  
        else:
            search_result_2.set('No merchants found selling this ingredient.')       

    else:
        search_result.set('Ingredient not found. Please try again or type exit to return to previous menu.')


#function that searches list of effects
def search_effect(value):
    global search_result
    search_result_2.set("Restocking merchant info will appear here.")
    potion_effect = value.lower()
    if potion_effect in listOfEffects:
        found_keys = [key for key, value in ingredients.items() if potion_effect in value]
        search_result.set('\n'.join(found_keys) if found_keys else 'No ingredients found.')
    else:
        search_result.set('Effect not found. Please try again or type exit to return to previous menu.')

#Function that makes listbox selection work
def get_selected_value(listbox):
    # Retrieve the selected item from the Listbox
    selection = listbox.curselection()
    if selection:
        return listbox.get(selection[0])
    return None

# Function to display ingredient search
def open_ingredient_search():
    clear_right_frame()
    Label(right_frame, text="Choose an Ingredient:").grid(row=0, column=0, padx=10, pady=10)
    ingredient_listbox = Listbox(right_frame, selectmode=SINGLE, exportselection=False)
    ingredient_listbox.grid(row=1, column=0, padx=10, pady=10)

    sorted_ingredients = sorted(ingredients.keys())

    # Populate the Listbox with ingredients
    for ingredient in sorted_ingredients:
        ingredient_listbox.insert(END, ingredient)

    # Button to trigger the search, passing the selected ingredient
    Button(right_frame, text="Search", command=lambda: ingredient_search(get_selected_value(ingredient_listbox))).grid(row=2, column=0, padx=10, pady=10)


# Function to display effect search
def open_effect_search():
    clear_right_frame()
    Label(right_frame, text="Enter an Effect:").grid(row=0, column=0, padx=10, pady=10)
    effect_listbox = Listbox(right_frame, selectmode=SINGLE, exportselection=False)
    effect_listbox.grid(row=1, column=0, padx=10, pady=10)

    # Populate the Listbox with ingredients
    for effect in listOfEffects:
        effect_listbox.insert(END, effect)

    # Button to trigger the search, passing the selected ingredient
    Button(right_frame, text="Search", command=lambda: search_effect(get_selected_value(effect_listbox))).grid(row=2, column=0, padx=10, pady=10)
    

# Creating buttons in the left frame
Button(left_frame, text="Search by Ingredient", command=open_ingredient_search,width=18,height=2,cursor="hand2",bg='#70552a',relief="raised", font=("Cinzel", 12, "bold")).grid(row=0, column=0, pady=5)
Button(left_frame, text="Search by Effect", command=open_effect_search,width=18,height=2,cursor="hand2",bg='#70552a',relief="raised", font=("Cinzel", 12, "bold")).grid(row=1, column=0, pady=5)
Button(left_frame, text="Quit", command=root.quit,width=18,height=2,cursor="hand2", bg='#70552a',relief="raised", font=("Cinzel", 12, "bold")).grid(row=2, column=0, pady=5)
Button(left_frame, text="Music On/Off", command=toggle_music ,width=12,height=2,cursor="hand2",bg='#70552a',relief="raised", font=("Cinzel", 12, "bold")).grid(row=3, column=0, pady=20)




play_background_music()

root.mainloop()

pygame.mixer.music.stop()