# Wellbeing Application - Ella Harley

# importing reqired tkinter stuff
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import random

# A function to open the breathing exercise game
def breathing_exercise_open():
    breathing_exercise_window = Toplevel(root)
    breathing_exercise_window.title = ("Breathing Exercise")
    breathing_exercise_window.geometry("2900x1200")

    breathing_exercise_title = tk.Label(breathing_exercise_window, text = "Breathing Exercise", font = ("Arial", 40))
    breathing_exercise_title.pack(pady = 50)


# A function to open the memory game
def memory_exercise_open():
    memory_exercise_window = Toplevel(root)
    memory_exercise_window.title = ("Memory Game")
    memory_exercise_window.geometry("2900x1200")

    memory_exercise_title = tk.Label(memory_exercise_window, text = "Memory Game", font = ("Arial", 40))
    memory_exercise_title.pack(pady = 50)


# A function to open the affirmations game, opens window with the title "affirmations"
def affirmations_exercise_open():
    affirmations_exercise_window = Toplevel(root)
    affirmations_exercise_window.title = ("Affirmations")
    affirmations_exercise_window.geometry("2900x1200")

    # adds text that says the window is for affirmations
    affirmations_exercise_title = tk.Label(affirmations_exercise_window, text = "Affirmations", font = ("Arial", 40))
    affirmations_exercise_title.pack(pady = 50)

    # Function that randomizes the affirmaition
    def random_affirmation():
        
        # list of random affirmations
        affirmation_list = ["I have done it before, I will do it again.", "Time will pass and I will be better.", "Big feelings are okay to have, but they are tempoary and will pass.", "I have friends and family who love me and I can go to them for help.", "Only I can make the decision to be better.", "I can have good feelings at the same time as bad ones"]

        # chooses a random item from the affirmations list
        chosen_affirmation = random.choice(affirmation_list)

        # changes the text of the label to the chosen affirmation
        randomized_affirmation.config(text = chosen_affirmation)

    # a command to close the affirmations window
    def close_affirmations():
        affirmations_exercise_window.destroy()


    def editing_affirmations_window(affirmation_list):
        editing_affirmations_window = Toplevel(root)
        editing_affirmations_window.title = ("Editing Affirmations")
        editing_affirmations_window.geometry("2900x1200")

        
        for affirmation in affirmation_list:
            all_affirmations = tk.Label(editing_affirmations_window, text = "what")
            all_affirmations.pack()






        


        
        

    # creates a button that the user can click to randomize an affirmation, runs the random affirmation def when clicked
    randomizer_button_affirmations = tk.Button(affirmations_exercise_window, text = "Random Affirmation", font = ("Arial", 15),  height = 5, width = 30, command = random_affirmation)
    randomizer_button_affirmations.pack(pady = 50)

    editing_button_affirmations = tk.Button(affirmations_exercise_window, text = "Edit Affirmations", font = ("Arial", 15),  height = 2, width = 15, command = editing_affirmations_window)
    editing_button_affirmations.pack(pady = 10)

    # the label that displays the chosen affirmation
    randomized_affirmation = tk.Label(affirmations_exercise_window, text = "", font = ("Arial", 20),  height = 5)
    randomized_affirmation.pack(pady = 20)

    # button that when clicked, closes the affirmations window
    close_affirmations_window = tk.Button(affirmations_exercise_window, text = "Close", font = ("Arial", 10), height = 2, width = 10, command = close_affirmations)
    close_affirmations_window.pack(padx = 20, pady = 10)





   


# A function to open the posing game
def posing_exercise_open():
    posing_exercise_window = Toplevel(root)
    posing_exercise_window.title = ("Posing Game")
    posing_exercise_window.geometry("2900x1200")

    posing_exercise_title = tk.Label(posing_exercise_window, text = "Posing Game", font = ("Arial", 40))
    posing_exercise_title.pack(pady = 50)


# A function to open the wellbeing journal
def journal_exercise_open():
    journal_exercise_window = Toplevel(root)
    journal_exercise_window.title = ("Wellbeing Journal")
    journal_exercise_window.geometry("2900x1200")

    journal_exercise_title = tk.Label(journal_exercise_window, text = "Wellbeing Journal", font = ("Arial", 40))
    journal_exercise_title.pack(pady = 50)


# def that closes the root window when called
def close_mainloop():
    root.destroy()






# Root window, for storing all of the buttons
root = tk.Tk()

# Sets size and the title of the window
root.geometry("2900x1200")
root.title("Managing Your Wellbeing")

# Creates a title at the top of the window
root_title = tk.Label(root, text = "Managing Your Wellbeing", font = ("Arial", 40))
root_title.pack(pady = 50)

# Button that leades to the breathing exercise when clicked
breathing_exercise = tk.Button(root, text = "Breathing Exercise", font = ("Arial", 15),  height = 5, width = 30, command = breathing_exercise_open)
breathing_exercise.pack(padx = 20, pady = 10)

# Button that leads to the memory game when clicked
memory_exercise = tk.Button(root, text = "Memory Game", font = ("Arial", 15),  height = 5, width = 30, command = memory_exercise_open)
memory_exercise.pack(padx = 20, pady = 10)

# Button that leades to the affirmations
affirmations_exercise = tk.Button(root, text = "Affirmations", font = ("Arial", 15),  height = 5, width = 30, command = affirmations_exercise_open)
affirmations_exercise.pack(padx = 20, pady = 10)

# Button that leads to the posing game
posing_exercise = tk.Button(root, text = "Posing Game", font = ("Arial", 15),  height = 5, width = 30, command = posing_exercise_open)
posing_exercise.pack(padx = 20, pady = 10)

# Button that leads to the wellbeing journal
journal_exercise = tk.Button(root, text = "Wellbeing Journal", font = ("Arial", 15),  height = 5, width = 30, command = journal_exercise_open)
journal_exercise.pack(padx = 20, pady = 10)

# Button that closes the program
close_program_button = tk.Button(root, text = "Close", font = ("Arial", 10), height = 2, width = 10, command = close_mainloop)
close_program_button.pack(padx = 20, pady = 10)

# Runs everything in the root mainloop
root.mainloop()