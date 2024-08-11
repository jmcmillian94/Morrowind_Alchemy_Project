from tkinter import *
from ingredients_dict import *

#making a root window
root = Tk()
root.title("Morrowind Alchemy Helper")
root.geometry("600x400")
root.configure(bg='#eab974')

# Create frames for layout
left_frame = Frame(root)
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")
left_frame.configure(bg='#eab974')

right_frame = Frame(root, bd=2, relief="solid", width=200, height=350)
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ns")
right_frame.grid_propagate(False)

info_frame = Frame(root, bd=2, relief="solid", width=200, height=350)
info_frame.grid(row=0, column=2, padx=10, pady=10, sticky="ns")
info_frame.grid_propagate(False) 


Label(right_frame, text="Select an option from the Menu", wraplength=180).grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Function to clear right_frame
def clear_right_frame():
    for widget in right_frame.winfo_children():
        widget.destroy()


search_result = StringVar()
search_result.set("Search results will appear here.")
Label(info_frame, textvariable=search_result, wraplength=180, justify="left", anchor="nw").grid(row=0, column=0, padx=10, pady=10, sticky="nw")

#Fuction that searches ingredient dict
def ingredient_search(value):
    global search_result
    potion_ingredient = value.lower()
    if potion_ingredient in ingredients:
        effects = ingredients[potion_ingredient]
        search_result.set(', '.join(effects) if effects else 'No ingredients found.')
    else:
        search_result.set('Ingredient not found. Please try again or type exit to return to previous menu.')


#function that searches list of effects
def search_effect(value):
    global search_result
    potion_effect = value.lower()
    if potion_effect in listOfEffects:
        found_keys = [key for key, value in ingredients.items() if potion_effect in value]
        search_result.set(', '.join(found_keys) if found_keys else 'No ingredients found.')
    else:
        search_result.set('Effect not found. Please try again or type exit to return to previous menu.')

# Function to display ingredient search
def open_ingredient_search():
    clear_right_frame()
    Label(right_frame, text="Choose an Ingredient:").grid(row=0, column=0, padx=10, pady=10)
    ingredient_var = StringVar(right_frame)
    OptionMenu(right_frame, ingredient_var, *ingredients).grid(row=1, column=0, padx=10, pady=10)
    Button(right_frame, text="Search", command=lambda: ingredient_search(ingredient_var.get())).grid(row=2, column=0, padx=10, pady=10)

# Function to display effect search
def open_effect_search():
    clear_right_frame()
    Label(right_frame, text="Enter an Effect:").grid(row=0, column=0, padx=10, pady=10)
    effect_var = StringVar(right_frame)
    OptionMenu(right_frame, effect_var, *listOfEffects).grid(row=1, column=0, padx=10, pady=10)
    Button(right_frame, text="Search", command=lambda: search_effect(effect_var.get())).grid(row=2, column=0, padx=10, pady=10)
    

# Creating buttons in the left frame
Button(left_frame, text="Search by Ingredient", command=open_ingredient_search,width=16,height=3,cursor="hand2").grid(row=0, column=0, pady=5)
Button(left_frame, text="Search by Effect", command=open_effect_search,width=16,height=3,cursor="hand2").grid(row=1, column=0, pady=5)
Button(left_frame, text="Quit", command=root.quit,width=16,height=3,cursor="hand2").grid(row=2, column=0, pady=5)


root.mainloop()