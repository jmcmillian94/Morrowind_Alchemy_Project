from tkinter import *
from ingredients_dict import *

#making a root window
root = Tk()

#creating a lable wiget
title = Label(root, text="Morrowind Alchemy Helper").grid(row=0, column=0)

def open_ingredient_search():
    ingredientSearch = Toplevel(root)
    ingredientSearch.title("seach by Ingredient")
    
    # Add widgets to the new window
    Label(ingredientSearch, text="Choose an Ingredient:").grid(row=0, column=0)
    ingredient_var = StringVar(ingredientSearch)
    OptionMenu(ingredientSearch, ingredient_var, *ingredients).grid(row=1, column=0)
    Button(ingredientSearch, text="Search").grid(row=2, column=0)
ingredientSearchButton = Button(root, text="Search by Ingredient", command=open_ingredient_search).grid(row=1, column=0)

def open_effect_search():
    effectSearch = Toplevel(root)
    effectSearch.title("seach by Effect")
    
    # Add widgets to the new window
    Label(effectSearch, text="Enter an Effect:").grid(row=0, column=0)
    Entry(effectSearch).grid(row=1, column=0)
    Button(effectSearch, text="Search").grid(row=2, column=0)
effectSearchButton = Button(root, text="Search by Effect", comman=open_effect_search).grid(row=2, column=0)

quitButton = Button(root, text="Quit", command=root.quit).grid(row=3, column=0)

root.mainloop()