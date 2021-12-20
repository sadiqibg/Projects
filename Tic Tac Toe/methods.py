"""

This script store all the necessary function for the game to fucntion fully


"""
import random
from tkinter import *
from tkinter import ttk
import config



# The function is used to place a marker
def place_marker(location):
    # Make the maker locations global
   
    # Confirms that the game is still one
    if config.game_on:
        config.message.config(text="Player {}'s Turn".format(config.marker))
        if not Check_win():
            if location == '1' and config.label1.cget("text") == "":
                config.label1.config(text=config.marker)
                change()
                config.turn+=1
            elif location == '2' and config.label2.cget("text") == "":
                config.label2.config(text=config.marker)
                change()
                config.turn+=1
            elif location == '3' and config.label3.cget("text") == "":
                config.label3.config(text=config.marker)
                change()
                config.turn+=1
            elif location == '4' and config.label4.cget("text") == "":
                config.label4.config(text=config.marker)
                change()
                config.turn+=1
            elif location == '5' and config.label5.cget("text") == "":
                config.label5.config(text=config.marker)
                change()
                config.turn+=1
            elif location == '6' and config.label6.cget("text") == "":
                config.label6.config(text=config.marker)
                change()
                config.turn+=1
            elif location == '7' and config.label7.cget("text") == "":
                config.label7.config(text=config.marker)
                change()
                config.turn+=1
            elif location == '8' and config.label8.cget("text") == "":
                config.label8.config(text=config.marker)
                change()
                config.turn+=1
            elif location == '9'and config.label9.cget("text") == "":
                config.label9.config(text=config.marker)
                change()
                config.turn+=1
            else:
                config.message.config    (text="Invalid input Please try again") 
    
    
    if Check_win():
        config.game_on = False
        config.message.config(text="Congratulations Player {} for winning".format(config.marker))
    elif config.turn >=9:
        config.game_on = False
        config.message.config(text="The game is a draw !! ")

    
  




# This methods checks for a win 
def Check_win():

    # Check for win condition for 8 cases
    if config.label1.cget("text") == config.marker and config.label2.cget("text") == config.marker and config.label3.cget("text") == config.marker:
        config.game_on = False
        return True
    elif config.label4.cget("text") == config.marker and config.label5.cget("text") == config.marker and config.label6.cget("text") == config.marker:
        config.game_on = False
        return True 
    elif config.label7.cget("text") == config.marker and config.label8.cget("text") == config.marker and config.label9.cget("text") == config.marker:
        config.game_on = False
        return True
    elif config.label1.cget("text") == config.marker and config.label4.cget("text") == config.marker and config.label7.cget("text") == config.marker:
        config.game_on = False
        return True
    elif config.label2.cget("text") == config.marker and config.label5.cget("text") == config.marker and config.label8.cget("text") == config.marker:
        config.game_on = False
        return True
    elif config.label3.cget("text") == config.marker and config.label6.cget("text") == config.marker and config.label9.cget("text") == config.marker:
        config.game_on = False
        return True
    elif config.label1.cget("text") == config.marker and config.label5.cget("text") == config.marker and config.label9.cget("text") == config.marker:
        config.game_on = False
        return True
    elif config.label3.cget("text") == config.marker and config.label5.cget("text") == config.marker and config.label7.cget("text") == config.marker:
        config.game_on = False
        return True

    # No Win
    return False



# This method resets the board 
def start_game():

    # randomly selecting the marker for player 1 and player 2
    pick = random.randint(1,2)
    if pick == 1:
        config.ply1_selection.config(text="X")
        config.ply2_selection.config(text="O")
    else:
        config.ply1_selection.config(text="O")
        config.ply2_selection.config(text="X")

    # Clear the fields 
    config.label1.config(text="")
    config.label2.config(text="")
    config.label3.config(text="")
    config.label4.config(text="")
    config.label5.config(text="")
    config.label6.config(text="")
    config.label7.config(text="")
    config.label8.config(text="")
    config.label9.config(text="")

    # Assign marker for player 1
    config.marker = config.ply1_selection.cget("text")
    config.turn = 1
    config.game_on = True
    config.message.config(text="Please select a location !!")


# change the marker for the next player
def change():

     if config.marker == "X":
         config.marker = "O"
     else:
         config.marker = "X"   


# This method clears the board and ends game
def end_game():
    config.game_on = False

    # Clear the fields 
    config.label1.config(text="")
    config.label2.config(text="")
    config.label3.config(text="")
    config.label4.config(text="")
    config.label5.config(text="")
    config.label6.config(text="")
    config.label7.config(text="")
    config.label8.config(text="")
    config.label9.config(text="")

    config.ply1_selection.config(text="")
    config.ply2_selection.config(text="")
    config.message.config(text="Please select start to begin")

 