#importing tkinter
import tkinter as tk
from tkinter import *
import os
from functools import partial

#creating the array to store user input
saveButtons = [[], [], [], [], [], []]

#creating a test function
def testing(i, j, k):
    print(saveButtons[i][j][k].get())

          
#defining the functions that we will be using.
#defining the function that will create the header for each page
def createHeader(frame_name):
    header_name = tk.Label(frame_name, text = "Item Name", width = 15).grid(row = 0, column = 0)
    header_description = tk.Label(frame_name, text = "How to obtain recipe!", width = 15).grid(row = 0, column = 1)
    header_recipe_own = tk.Label(frame_name, text = "Recipe Obtained?", width = 15).grid(row = 0, column = 2)
    header_recipe_craft = tk.Label(frame_name, text = "Item Crafted?", width = 15).grid(row = 0, column = 3)


#defining the function that will create each line
def createLine(frame_name, name, description, row_num, page_num):

    #formatting the item name and description
    item_name = tk.Label(frame_name, text = name, width = 15).grid(row = int(row_num), column = 0)
    desc = tk.Label(frame_name, text = str(description), width = 15).grid(row = int(row_num), column = 1)

    #button work
    CheckVar1 = tk.BooleanVar()
    CheckVar2 = tk.BooleanVar()

    saveButtons[page_num].append([CheckVar1, CheckVar2])

    #creates the Buttons seen in the program.
    a = tk.Checkbutton(frame_name,variable = CheckVar1, onvalue = True, offvalue = False, command=partial(testing, page_num, row_num,0))
    a.grid(row=int(row_num), column = 2)

    tk.Checkbutton(frame_name,variable = CheckVar2).grid(row=int(row_num), column = 3)


#creating the save function, which writes the user data inputted to a file
def save():
    if os.path.exists("save.txt"):
      os.remove("save.txt")

    
    File1 = open("save.txt", "w+")
    print("hello")
    for page in saveButtons:
        for column in page:
            for button in column:
                if button != None:
                    File1.write(str(button.get()) + "\n")
            File1.write("C\n")
        File1.write("P\n")
    File1.close()

#loads previously inputted user data
def load():
    if os.path.exists("save.txt"):
        File2 = open("save.txt", "r")
        Page = 0
        Column = 0
        Row = 0
        
        Lines = File2.readlines()
        for x in range(len(Lines)):
            if(Lines[x] == "P\n"):
                Page += 1
                Row = 0
                Column = 0
            if(Lines[x] == "C\n"):
                Column = 0
                Row += 1
            if(Lines[x] == "True\n"):
                saveButtons[Page][Row][Column].set(True)
                Column += 1
            if(Lines[x] == "False\n"):
                saveButtons[Page][Row][Column].set(False)
                Column += 1
        File2.close()
        print(saveButtons[0][0][0].get())


















#creating the classes for all the different 'pages'
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       global icon
       global background_image

       #code to add a background image
       #SCRAPPED: Didn't work as intended
       #background_image=tk.PhotoImage(file = "/Users/vardan/Desktop/Python/background_image.png")
       #background_label = tk.Label(self, image=background_image)
       #background_label.place(x=0, y=0, relwidth=1, relheight=1)
       #background_label.pack(fill = "both", expand = True)


       #code to make the main page look pretty, uncomment and replace directory with your own if you want to see the image
       #icon = tk.PhotoImage(file = "/Users/vardan/Desktop/SBHacks/tothesummit.png")
       #label = tk.Label(self, image = icon)
       #label.pack(side = "top", fill = "x")
       information = tk.Label(self,
                              text = "TOTHESUMMIT is a python tkinter tool designed to help Stardew Valley players achieve the 'Craft Master' achievement."
                                  " To use this tool, click the buttons"
                                  " above to see categories for all the items in the game. Then, mark which items you have the recipe for, or "
                                  """which items you have already crafted. Use the 'Save' button to save your inputted data, and 'Load' to access data previously inputted.
Enjoy!""",
                              wraplength=1050, justify="center")
       information.config(font = ("Courier", 24))
       information.pack(side = "top", fill = "x")
        
class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #creating the page setup for the second page
       createHeader(self)
       createLine(self, "Cherry Bomb", "Mining Level 1", 1, 0)
       createLine(self, "Bomb", "Mining Level 6", 2, 0)
       createLine(self, "Mega Bomb", "Mining Level 8", 3, 0)
       createLine(self, "Gate", "Starter", 4, 0)
       createLine(self, "Wood Fence", "Starter", 5, 0)
       createLine(self, "Stone Fence", "Farming Level 2", 6, 0)
       createLine(self, "Iron Fence", "Farming Level 4", 7, 0)
       createLine(self, "Hardwood Fence", "Farming Level 6", 8, 0)
       createLine(self, "Sprinkler", "Farming Level 2", 9, 0)
       createLine(self, "Quality Sprinkler", "Farming Level 6", 10, 0)
       createLine(self, "Iridium Sprinkler", "Farming Level 9", 11, 0)

       
class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #creating the page setup for the third page
       createHeader(self)
       createLine(self, "Mayo Machine", "Farming Level 2", 1, 1)
       createLine(self, "Bee House", "Farming Level 3", 2, 1)
       createLine(self, "Preserves Jar", "Farming Level 4", 3, 1)
       createLine(self, "Cheese Press", "Farming Level 6", 4, 1)
       createLine(self, "Loom", "Farming Level 7", 5, 1)
       createLine(self, "Keg", "Farming Level 8", 6, 1)
       createLine(self, "Oil Maker", "Farming Level 8", 7, 1)
       createLine(self, "Basic Fert.", "Farming Level 1", 8, 1)
       createLine(self, "Quality Fert.", "Farming Level 9", 9, 1)
       createLine(self, "Deluxe Fert.", "Mr. Qi", 10, 1)
       createLine(self, "Speed-Gro", "Farming Level 3", 11, 1)
       createLine(self, "Deluxe Spd-Gro", "Farming Level 8", 12, 1)
       createLine(self, "Hyper Spd-Gro", "Mr. Qi", 13, 1)
       createLine(self, "Basic Retain. Soil", "Farming Level 4", 14, 1)
       createLine(self, "Quality Retain. Soil", "Farming Level 7", 15, 1)
       createLine(self, "Deluxe Retain. Soil", "Island Trader", 16, 1)
       createLine(self, "Tree Fertilizer", "Foraging Level 7", 17, 1)


class Page4(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #creating the page setup for the fourth page
       createHeader(self)
       createLine(self, "Spinner", "Fishing Level 6", 1, 2)
       createLine(self, "Trap Bobber", "Fishing Level 6", 2, 2)
       createLine(self, "Cork Bobber", "Fishing Level 7", 3, 2)
       createLine(self, "Quality Bobber", "Willy Special Quest", 4, 2)
       createLine(self, "Treasure Hunter", "Fishing Level 7", 5, 2)
       createLine(self, "Dressed Spinner", "Fishing Level 8", 6, 2)
       createLine(self, "Barbed Hook", "Fishing Level 8", 7, 2)
       createLine(self, "Magnet", "Fishing Level 9", 8, 2)
       createLine(self, "Bait", "Fishing Level 2", 9, 2)
       createLine(self, "Wild Bait", "Linus 4 Hearts", 10, 2)
       createLine(self, "Magic Bait", "Mr. Qi", 11, 2)
       createLine(self, "Crab Pot", "Fishiing Level 3", 12, 2)
       createLine(self, "Sturdy Ring", "Combat Level 1", 13, 2)
       createLine(self, "Warrior Ring", "Combat Level 4", 14, 2)
       createLine(self, "Ring of Yoba", "Combat Level 7", 15, 2)
       createLine(self, "Thorns Ring", "Combat Level 7", 16, 2)
       createLine(self, "Glowstone Ring", "Mining Level 4", 17, 2)
       createLine(self, "Iridium Band", "Combat Level 9", 18, 2)
       createLine(self, "Wedding Ring", "Traveling Cart", 19, 2)



class Page5(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #creating the page setup for the fifth page
       createHeader(self)
       createLine(self, "Field Snack", "Foraging Level 1", 1, 3)
       createLine(self, "Bug Steak", "Combat Level 1", 2, 3)
       createLine(self, "Life Elixir", "Combat Level 2", 3, 3)
       createLine(self, "Oil of Garlic", "Combat Level 6", 4, 3)
       createLine(self, "Monster Musk", "Wizard(Special Order)", 5, 3)
       createLine(self, "Fairy Dust", "The Pirate's Wife", 6, 3)
       createLine(self, "Warp Totem: Beach", "Foraging Level 6", 7, 3)
       createLine(self, "Warp Totem: Mtn.", "Foraging Level 7", 8, 3)
       createLine(self, "Warp Totem: Farm", "Foraging Level 8", 9, 3)
       createLine(self, "Warp Totem: Desert", "Desert Trader", 10, 3)
       createLine(self, "Warp Totem: Island", "Volcano Dwarf", 11, 3)
       createLine(self, "Rain Totem", "Foraging Level 9", 12, 3)
       createLine(self, "Tub o' Flowers", "Flower Dance", 13, 3)
       createLine(self, "Wicked Statue", "Krobus", 14, 3)
       createLine(self, "Flute Block", "Robin 6 Heart", 15, 3)
       createLine(self, "Drum Block", "Robin 6 Heart", 16, 3)




class Page6(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #creating the page setup for the sixth page
       createHeader(self)
       createLine(self, "Torch", "Starter", 1, 4)
       createLine(self, "Campfire", "Starter", 2, 4)
       createLine(self, "Wooden Brazier", "Carpenter's Shop", 3, 4)
       createLine(self, "Stone Brazier", "Carpenter's Shop", 4, 4)
       createLine(self, "Gold Brazier", "Carpenter's Shop", 5, 4)
       createLine(self, "Carved Brazier", "Carpenter's Shop", 6, 4)
       createLine(self, "Stump Brazier", "Carpenter's Shop", 7, 4)
       createLine(self, "Barrel Brazier", "Carpenter's Shop", 8, 4)
       createLine(self, "Skull Brazier", "Carpenter's Shop", 9, 4)
       createLine(self, "Marble Brazier", "Carpenter's Shop", 10, 4)
       createLine(self, "Wood Lamp-post", "Carpenter's Shop", 11, 4)
       createLine(self, "Iron Lamp-post", "Carpenter's Shop", 12, 4)
       createLine(self, "Jack-O-Lantern", "Spirit's Eve Shop", 13, 4)
       createLine(self, "Charocal Kiln", "Foraging Level 4", 14, 4)
       createLine(self, "Crystalarium", "Mining Level 9", 15, 4)
       createLine(self, "Furnace", "Clint", 16, 4)
       createLine(self, "Lightning Rod", "Foraging Level 6", 17, 4)
       createLine(self, "Solar Panel", "Caroline(SO)", 18, 4)
       createLine(self, "Recycling Machine", "Fishing Level 4", 19, 4)
       createLine(self, "Seed Maker", "Farming Level 9", 20, 4)
       createLine(self, "Slime Incubator", "Combat Level 8", 21, 4)
       createLine(self, "Ostrich Incubator", "Island Field Office", 22, 4)
       createLine(self, "Slime Egg-Press", "Combat Level 6", 23, 4)
       createLine(self, "Tapper", "Foraging Level 3", 24, 4)
       createLine(self, "Heavy Tapper", "Mr. Qi", 25, 4)
       createLine(self, "Worm Bin", "Fishing Level 8", 26, 4)
       createLine(self, "Bone Mill", "Gunther(SO)", 27, 4)
       createLine(self, "Geode Crusher", "Clint(Special Order)", 28, 4)






class Page7(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #creating the page setup for the seventh page
       createHeader(self)
       createLine(self, "Chest", "Starter", 1, 5)
       createLine(self, "Stone Chest", "Robin Special Order", 2, 5)
       createLine(self, "Wood Sign", "Starter", 3, 5)
       createLine(self, "Stone Sign", "Starter", 4, 5)
       createLine(self, "Dark Sign", "Krobus 3 Heart", 5, 5)
       createLine(self, "Garden Pot", "Complete Greenhouse", 6, 5)
       createLine(self, "Scarecrow", "Farming Level 1", 7, 5)
       createLine(self, "Deluxe Scarecrow", "Get All Rarecrows", 8, 5)
       createLine(self, "Staircase", "Mining Level 2", 9, 5)
       createLine(self, "Explosive Ammo", "Combat Level 8", 10, 5)
       createLine(self, "Transmute(Fe)", "Mining Level 4", 11, 5)
       createLine(self, "Transmute(Au)", "Mining Level 7", 12, 5)
       createLine(self, "Mini-Jukebox", "Gus 5 Heart", 13, 5)
       createLine(self, "Mini-Obelisk", "Wizard Special Order", 14, 5)
       createLine(self, "Farm Computer", "Demetrius/Willy SO", 15, 5)
       createLine(self, "Hopper", "Mr. Qi", 16, 5)
       createLine(self, "Hopper", "Foraging Level 9", 17, 5)


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
        #pageArray = [p2, p3, p4, p5, p6, p7]

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
        b8 = tk.Button(buttonframe, text="Save",command=save)
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
    root.wm_geometry("1200x850")
    root.mainloop()
