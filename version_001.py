#importing tkinter
import tkinter as tk
from tkinter import *
import os

#saveButtons = [[[None for k in range(29)] for j in range(29)] for i in range(29)]

#defining the functions that we will be using.
#defining the function that will create the header for each page
def createHeader(frame_name):
    header_name = tk.Label(frame_name, text = "Item Name", width = 15).grid(row = 0, column = 0)
    header_description = tk.Label(frame_name, text = "How to obtain recipe!", width = 15).grid(row = 0, column = 1)
    header_recipe_own = tk.Label(frame_name, text = "Recipe Obtained?", width = 15).grid(row = 0, column = 2)
    header_recipe_craft = tk.Label(frame_name, text = "Item Crafted?", width = 15).grid(row = 0, column = 3)


#defining the function that will create each line
def createLine(frame_name, name, description, row_num, page_num):

    #formattiing the item name and description
    item_name = tk.Label(frame_name, text = name, width = 15).grid(row = int(row_num), column = 0)
    desc = tk.Label(frame_name, text = str(description), width = 15).grid(row = int(row_num), column = 1)

    #button work
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()

    tk.Checkbutton(frame_name,variable = CheckVar1, onvalue = True, offvalue = False).grid(row=int(row_num), column = 2)
    #saveButtons[row_num][2][page_num] = a

    tk.Checkbutton(frame_name,variable = CheckVar2).grid(row=int(row_num), column = 3)
    #saveButtons[row_num][3][page_num] = a


def save(pageArray):
    if os.path.exists("save.txt"):
      os.remove("save.txt")

    File1 = open("save.txt", "w+")
    File1.close()

def load():
    return



















#creating the classes for all the different 'pages'
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Welcome...TOTHESUMMIT!")
       label.grid(sticky = "N")
       #label.pack(side="top", fill="both", expand=True)
       label.config(font=("Courier", 100))
        
class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #creating the page setup for the second page
       createHeader(self)
       createLine(self, "Cherry Bomb", "Mining Level 1", 1, 2)
       createLine(self, "Bomb", "Mining Level 6", 2, 2)
       createLine(self, "Mega Bomb", "Mining Level 8", 3, 2)
       createLine(self, "Gate", "Starter", 4, 2)
       createLine(self, "Wood Fence", "Starter", 5, 2)
       createLine(self, "Stone Fence", "Farming Level 2", 6, 2)
       createLine(self, "Iron Fence", "Farming Level 4", 7, 2)
       createLine(self, "Hardwood Fence", "Farming Level 6", 8, 2)
       createLine(self, "Sprinkler", "Farming Level 2", 9, 2)
       createLine(self, "Quality Sprinkler", "Farming Level 6", 10, 2)
       createLine(self, "Iridium Sprinkler", "Farming Level 9", 11, 2)

       
class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #creating the page setup for the third page
       createHeader(self)
       createLine(self, "Mayo Machine", "Farming Level 2", 1, 3)
       createLine(self, "Bee House", "Farming Level 3", 2, 3)
       createLine(self, "Preserves Jar", "Farming Level 4", 3, 3)
       createLine(self, "Cheese Press", "Farming Level 6", 4, 3)
       createLine(self, "Loom", "Farming Level 7", 5, 3)
       createLine(self, "Keg", "Farming Level 8", 6, 3)
       createLine(self, "Oil Maker", "Farming Level 8", 7, 3)
       createLine(self, "Basic Fert.", "Farming Level 1", 8, 3)
       createLine(self, "Quality Fert.", "Farming Level 9", 9, 3)
       createLine(self, "Deluxe Fert.", "Mr. Qi", 10, 3)
       createLine(self, "Speed-Gro", "Farming Level 3", 11, 3)
       createLine(self, "Deluxe Spd-Gro", "Farming Level 8", 12, 3)
       createLine(self, "Hyper Spd-Gro", "Mr. Qi", 13, 3)
       createLine(self, "Basic Retain. Soil", "Farming Level 4", 14, 3)
       createLine(self, "Quality Retain. Soil", "Farming Level 7", 15, 3)
       createLine(self, "Deluxe Retain. Soil", "Island Trader", 16, 3)
       createLine(self, "Tree Fertilizer", "Foraging Level 7", 17, 3)


class Page4(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #creating the page setup for the fourth page
       createHeader(self)
       createLine(self, "Spinner", "Fishing Level 6", 1, 4)
       createLine(self, "Trap Bobber", "Fishing Level 6", 2, 4)
       createLine(self, "Cork Bobber", "Fishing Level 7", 3, 4)
       createLine(self, "Quality Bobber", "Willy Special Quest", 4, 4)
       createLine(self, "Treasure Hunter", "Fishing Level 7", 5, 4)
       createLine(self, "Dressed Spinner", "Fishing Level 8", 6, 4)
       createLine(self, "Barbed Hook", "Fishing Level 8", 7, 4)
       createLine(self, "Magnet", "Fishing Level 9", 8, 4)
       createLine(self, "Bait", "Fishing Level 2", 9, 4)
       createLine(self, "Wild Bait", "Linus 4 Hearts", 10, 4)
       createLine(self, "Magic Bait", "Mr. Qi", 11, 4)
       createLine(self, "Crab Pot", "Fishiing Level 3", 12, 4)
       createLine(self, "Sturdy Ring", "Combat Level 1", 13, 4)
       createLine(self, "Warrior Ring", "Combat Level 4", 14, 4)
       createLine(self, "Ring of Yoba", "Combat Level 7", 15, 4)
       createLine(self, "Thorns Ring", "Combat Level 7", 16, 4)
       createLine(self, "Glowstone Ring", "Mining Level 4", 17, 4)
       createLine(self, "Iridium Band", "Combat Level 9", 18, 4)
       createLine(self, "Wedding Ring", "Traveling Cart", 19, 4)



class Page5(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #creating the page setup for the fifth page
       createHeader(self)
       createLine(self, "Field Snack", "Foraging Level 1", 1, 5)
       createLine(self, "Bug Steak", "Combat Level 1", 2, 5)
       createLine(self, "Life Elixir", "Combat Level 2", 3, 5)
       createLine(self, "Oil of Garlic", "Combat Level 6", 4, 5)
       createLine(self, "Monster Musk", "Wizard(Special Order)", 5, 5)
       createLine(self, "Fairy Dust", "The Pirate's Wife", 6, 5)
       createLine(self, "Warp Totem: Beach", "Foraging Level 6", 7, 5)
       createLine(self, "Warp Totem: Mtn.", "Foraging Level 7", 8, 5)
       createLine(self, "Warp Totem: Farm", "Foraging Level 8", 9, 5)
       createLine(self, "Warp Totem: Desert", "Desert Trader", 10, 5)
       createLine(self, "Warp Totem: Island", "Volcano Dwarf", 11, 5)
       createLine(self, "Rain Totem", "Foraging Level 9", 12, 5)
       createLine(self, "Tub o' Flowers", "Flower Dance", 13, 5)
       createLine(self, "Wicked Statue", "Krobus", 14, 5)
       createLine(self, "Flute Block", "Robin 6 Heart", 15, 5)
       createLine(self, "Drum Block", "Robin 6 Heart", 16, 5)




class Page6(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #creating the page setup for the sixth page
       createHeader(self)
       createLine(self, "Torch", "Starter", 1, 6)
       createLine(self, "Campfire", "Starter", 2, 6)
       createLine(self, "Wooden Brazier", "Carpenter's Shop", 3, 6)
       createLine(self, "Stone Brazier", "Carpenter's Shop", 4, 6)
       createLine(self, "Gold Brazier", "Carpenter's Shop", 5, 6)
       createLine(self, "Carved Brazier", "Carpenter's Shop", 6, 6)
       createLine(self, "Stump Brazier", "Carpenter's Shop", 7, 6)
       createLine(self, "Barrel Brazier", "Carpenter's Shop", 8, 6)
       createLine(self, "Skull Brazier", "Carpenter's Shop", 9, 6)
       createLine(self, "Marble Brazier", "Carpenter's Shop", 10, 6)
       createLine(self, "Wood Lamp-post", "Carpenter's Shop", 11, 6)
       createLine(self, "Iron Lamp-post", "Carpenter's Shop", 12, 6)
       createLine(self, "Jack-O-Lantern", "Spirit's Eve Shop", 13, 6)
       createLine(self, "Charocal Kiln", "Foraging Level 4", 14, 6)
       createLine(self, "Crystalarium", "Mining Level 9", 15, 6)
       createLine(self, "Furnace", "Clint", 16, 6)
       createLine(self, "Lightning Rod", "Foraging Level 6", 17, 6)
       createLine(self, "Solar Panel", "Caroline(Special Order)", 18, 6)
       createLine(self, "Recycling Machine", "Fishing Level 4", 19, 6)
       createLine(self, "Seed Maker", "Farming Level 9", 20, 6)
       createLine(self, "Slime Incubator", "Combat Level 8", 21, 6)
       createLine(self, "Ostrich Incubator", "Island Field Office", 22, 6)
       createLine(self, "Slime Egg-Press", "Combat Level 6", 23, 6)
       createLine(self, "Tapper", "Foraging Level 3", 24, 6)
       createLine(self, "Heavy Tapper", "Mr. Qi", 25, 6)
       createLine(self, "Worm Bin", "Fishing Level 8", 26, 6)
       createLine(self, "Bone Mill", "Gunther(Special Order)", 27, 6)
       createLine(self, "Geode Crusher", "Clint(Special Order)", 28, 6)






class Page7(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #creating the page setup for the seventh page
       createHeader(self)
       createLine(self, "Chest", "Starter", 1, 7)
       createLine(self, "Stone Chest", "Robin Special Order", 2, 7)
       createLine(self, "Wood Sign", "Starter", 3, 7)
       createLine(self, "Stone Sign", "Starter", 4, 7)
       createLine(self, "Dark Sign", "Krobus 3 Heart", 5, 7)
       createLine(self, "Garden Pot", "Complete Greenhouse", 6, 7)
       createLine(self, "Scarecrow", "Farming Level 1", 7, 7)
       createLine(self, "Deluxe Scarecrow", "Get All Rarecrows", 8, 7)
       createLine(self, "Staircase", "Mining Level 2", 9, 7)
       createLine(self, "Explosive Ammo", "Combat Level 8", 10, 7)
       createLine(self, "Transmute(Fe)", "Mining Level 4", 11, 7)
       createLine(self, "Transmute(Au)", "Mining Level 7", 12, 7)
       createLine(self, "Mini-Jukebox", "Gus 5 Heart", 13, 7)
       createLine(self, "Mini-Obelisk", "Wizard Special Order", 14, 7)
       createLine(self, "Farm Computer", "Demetrius/Willy SO", 15, 7)
       createLine(self, "Hopper", "Mr. Qi", 16, 7)
       createLine(self, "Hopper", "Foraging Level 9", 17, 7)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)
        p5 = Page5(self)
        p6 = Page6(self)
        p7 = Page7(self)
        pageArray = [p2, p3, p4, p5, p6, p7]

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        #placing each frame in the container nicely
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p7.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        #defining the button widgets, along with their names
        b1 = tk.Button(buttonframe, text="Main", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Bombs/Fences/Sprinklers", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Artisan Equipment/Fertilizer", command=p3.lift)
        b4 = tk.Button(buttonframe, text="Fishing/Rings", command=p4.lift)
        b5 = tk.Button(buttonframe, text="Edible Items/Consumables/Furniture", command=p5.lift)
        b6 = tk.Button(buttonframe, text="Lighting/Refining Equipment", command=p6.lift)
        b7 = tk.Button(buttonframe, text="Miscellanous", command=p7.lift)
        b8 = tk.Button(buttonframe, text="Save",command=save(pageArray))
        b9 = tk.Button(buttonframe, text="Load",command=load)

        #packing all the buttons to the left of the button frame
        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")
        b6.pack(side="left")
        b7.pack(side="left")
        b8.pack(side="left")
        b9.pack(side="left")

        p1.show()

#main code
if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()
