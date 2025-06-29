# Wellbeing Application - Ella Harley

# importing reqired tkinter stuff
import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

# Tracking the buttons and the numbers that have been clicked in lists and dictionaries. Count keeps track of buttons clicked for the memory game
count = 0
match_answer_list = []
match_answer_dictionary = {}
journal_entries = {}

# A function to open the breathing exercise game
def breathing_exercise_open():
    breathing_exercise_window = Toplevel(root)
    breathing_exercise_window.title = ("Breathing Exercise")
    breathing_exercise_window.geometry("2900x1200")

    # Function that closes the window
    def close_breathing():
        breathing_exercise_window.destroy()

    # Label for the title of the window
    breathing_exercise_title = tk.Label(breathing_exercise_window, text = "Breathing Exercise", font = ("Arial", 40))
    breathing_exercise_title.pack(pady = 50)

    # Introduces the type of breathing exercise
    breathing_title = tk.Label(breathing_exercise_window, text = "Box Breathing", font = ("Arial", 20))
    breathing_title.pack(pady = 10)

    # Instructions for the breathing exercise
    breathing_instructions = tk.Label(breathing_exercise_window, text = "Breathe in, hold for four seconds, breathe out, hold for four seconds\n Trace the box with your finger to help you stay in a rhythm\n Relax. Remember to take it slow.", font = ("Arial", 15))
    breathing_instructions.pack(pady = 1)

    # The box visual
    box_breathing = tk.Label(breathing_exercise_window, text = "o", font = ("Wingdings", 400))
    box_breathing.pack(pady = 1)

    # Button for closing the window
    close_breathing_button = tk.Button(breathing_exercise_window, text = "Close", font = ("Arial", 10),height = 2, width = 10, command = close_breathing)
    close_breathing_button.pack()


# A function to open the memory game
def memory_exercise_open():
    memory_exercise_window = tk.Toplevel(root)
    memory_exercise_window.title = ("Memory Game")
    memory_exercise_window.geometry("2900x1200")

    # Title of the window
    memory_exercise_title = tk.Label(memory_exercise_window, text = "Memory Game", font = ("Arial", 40))
    memory_exercise_title.pack()

    # Creates match pairs
    memory_matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]


    # Randomizes the matches inside the list so the buttons display the numbers randomly
    random.shuffle(memory_matches)

    # Function that activates when clicking one of the buttons
    def match_click(button, number):
        
        # Global variables so they can be used in other functions
        global count, match_answer_list, match_answer_dictionary

        # If the button text is nothing and count is less than two, the button is assigned a number from the randomized list
        if button["text"] == " " and count < 2:
            button["text"] = memory_matches[number]

            # the buttons that are clicked are stored in the list
            match_answer_list.append(number)

            # Whatever number underneath a button is assigned to eachother in a dictonary. ex. {memory_button1 : 2, memory_button7 : 4}
            match_answer_dictionary[button] = memory_matches[number]

            # Increment the counter
            count += 1

        # If the answer list has two buttons stored in it (Two buttons have been clicked)
        if len(match_answer_list) == 2:

            # and if the first two buttons clicked (stored in the list) had numbers that matched
            if memory_matches[match_answer_list[0]] == memory_matches[match_answer_list[1]]:

                # makes a messagebox pop up that indicates that a match has been made, parent makes the window appear above the selected window
                messagebox.showinfo(" ", "It's a match!", parent = memory_exercise_window)
                
                # greys out the buttons if there is a match so they cannot be clicked again
                for key in match_answer_dictionary:
                    key["state"] = "disabled"

                # Set the count back to 0 and empty the list and dictonary
                count = 0
                match_answer_list = []
                match_answer_dictionary = {}

                # Checking if all of the buttons are greyed out (if all button states are disabled)
                check_win = all(button["state"] == "disabled" for button in memory_buttons)

                # if all buttons are disabled
                if check_win: 
                    # show a messagebox congratulating the player
                    messagebox.showinfo(" ", "Congratulations! You matched all of the pairs!", parent = memory_exercise_window)
                return
            
            # If the first two buttons clicked are not a match
            else:
                def reset_mismatch():
                    global count, match_answer_list, match_answer_dictionary
                    # resets buttons
                    for key in match_answer_dictionary:
                        key["text"] = ' '   
                    
                    count = 0
                    match_answer_list = []
                    match_answer_dictionary = {}

            # Show messagebox (waits for user click), then reset after 200ms
            messagebox.showinfo(" ", "Not a match. Try again!", parent = memory_exercise_window)
            memory_exercise_window.after(200, reset_mismatch)


    # Create frame for all of the buttons
    memory_buttonframe = tk.Frame(memory_exercise_window)
    memory_buttonframe.pack(pady = 50)

    # Creating the buttons and places them all into a grid
    memory_button1 = tk.Button(memory_buttonframe, text = ' ', font = ("Arial", 25), height = 4, width = 9, command = lambda: match_click(memory_button1, 0))
    memory_button2 = tk.Button(memory_buttonframe, text = ' ', font = ("Arial", 25), height = 4, width = 9, command = lambda: match_click(memory_button2, 1))
    memory_button3 = tk.Button(memory_buttonframe, text = ' ', font = ("Arial", 25), height = 4, width = 9, command = lambda: match_click(memory_button3, 2))
    memory_button4 = tk.Button(memory_buttonframe, text = ' ', font = ("Arial", 25), height = 4, width = 9, command = lambda: match_click(memory_button4, 3))

    memory_button5 = tk.Button(memory_buttonframe, text = ' ', font = ("Arial", 25), height = 4, width = 9, command = lambda: match_click(memory_button5, 4))
    memory_button6 = tk.Button(memory_buttonframe, text = ' ', font = ("Arial", 25), height = 4, width = 9, command = lambda: match_click(memory_button6, 5))
    memory_button7 = tk.Button(memory_buttonframe, text = ' ', font = ("Arial", 25), height = 4, width = 9, command = lambda: match_click(memory_button7, 6))
    memory_button8 = tk.Button(memory_buttonframe, text = ' ', font = ("Arial", 25), height = 4, width = 9, command = lambda: match_click(memory_button8, 7))

    memory_button9 = tk.Button(memory_buttonframe, text = ' ', font = ("Arial", 25), height = 4, width = 9, command = lambda: match_click(memory_button9, 8))
    memory_button10 = tk.Button(memory_buttonframe, text = ' ', font = ("Arial", 25), height = 4, width = 9, command = lambda: match_click(memory_button10, 9))
    memory_button11 = tk.Button(memory_buttonframe, text = ' ', font = ("Arial", 25), height = 4, width = 9, command = lambda: match_click(memory_button11, 10))
    memory_button12 = tk.Button(memory_buttonframe, text = ' ', font = ("Arial", 25), height = 4, width = 9, command = lambda: match_click(memory_button12, 11))

    memory_button13 = tk.Button(memory_buttonframe, text = ' ', font = ("Arial", 25), height = 4, width = 9, command = lambda: match_click(memory_button13, 12))
    memory_button14 = tk.Button(memory_buttonframe, text = ' ', font = ("Arial", 25), height = 4, width = 9, command = lambda: match_click(memory_button14, 13))
    memory_button15 = tk.Button(memory_buttonframe, text = ' ', font = ("Arial", 25), height = 4, width = 9, command = lambda: match_click(memory_button15, 14))
    memory_button16 = tk.Button(memory_buttonframe, text = ' ', font = ("Arial", 25), height = 4, width = 9, command = lambda: match_click(memory_button16, 15))

    # A list of all buttons so they can be checked if they are all disabled for the win condition
    memory_buttons = [
    memory_button1, memory_button2, memory_button3, memory_button4,
    memory_button5, memory_button6, memory_button7, memory_button8,
    memory_button9, memory_button10, memory_button11, memory_button12,
    memory_button13, memory_button14, memory_button15, memory_button16
]

    # PLacing all of the buttons into a grid
    memory_button1.grid(row = 0, column = 0, padx = 5, pady = 5)
    memory_button2.grid(row = 0, column = 1, padx = 5, pady = 5)
    memory_button3.grid(row = 0, column = 2, padx = 5, pady = 5)
    memory_button4.grid(row = 0, column = 3, padx = 5, pady = 5)

    memory_button5.grid(row = 1, column = 0, padx = 5, pady = 5)
    memory_button6.grid(row = 1, column = 1, padx = 5, pady = 5)
    memory_button7.grid(row = 1, column = 2, padx = 5, pady = 5)
    memory_button8.grid(row = 1, column = 3, padx = 5, pady = 5)

    memory_button9.grid(row = 2, column = 0, padx = 5, pady = 5)
    memory_button10.grid(row = 2, column = 1, padx = 5, pady = 5)
    memory_button11.grid(row = 2, column = 2, padx = 5, pady = 5)
    memory_button12.grid(row = 2, column = 3, padx = 5, pady = 5)

    memory_button13.grid(row = 3, column = 0, padx = 5, pady = 5)
    memory_button14.grid(row = 3, column = 1, padx = 5, pady = 5)
    memory_button15.grid(row = 3, column = 2, padx = 5, pady = 5)
    memory_button16.grid(row = 3, column = 3, padx = 5, pady = 5)

    # Function that closes the memory window
    def close_memory():
        memory_exercise_window.destroy()

    # Button that when clicked runs the above function
    close_memory_window = tk.Button(memory_exercise_window, text = "Close", font = ("Arial", 10), height = 2, width = 10, command = close_memory)
    close_memory_window.pack()


# A function to open the affirmations game, opens window with the title "affirmations"
def affirmations_exercise_open():
    affirmations_exercise_window = tk.Toplevel(root)
    affirmations_exercise_window.title = ("Affirmations")
    affirmations_exercise_window.geometry("2900x1200")

    # adds text that says the window is for affirmations
    affirmations_exercise_title = tk.Label(affirmations_exercise_window, text = "Affirmations", font = ("Arial", 40))
    affirmations_exercise_title.pack(pady = 50)

    # Function that randomizes the affirmaition
    def random_affirmation():
        
        # list of random affirmations
        affirmation_list = ["I have done it before, I will do it again.", "Time will pass and I will be better.", 
                            "Big feelings are okay to have, but they are tempoary and will pass.", "I have friends and family who love me and I can go to them for help.", 
                            "Only I can make the decision to be better.", "I can have good feelings at the same time as bad ones", "I will think positively today", 
                            "I am capable of so much", "I will do what I can to succeed", "It gets easier every day", "I will be okay"]

        # chooses a random item from the affirmations list
        chosen_affirmation = random.choice(affirmation_list)

        # changes the text of the label to the chosen affirmation
        randomized_affirmation.config(text = chosen_affirmation)

    # a command to close the affirmations window
    def close_affirmations():
        affirmations_exercise_window.destroy()

    # creates a button that the user can click to randomize an affirmation, runs the random affirmation def when clicked
    randomizer_button_affirmations = tk.Button(affirmations_exercise_window, text = "Random Affirmation", font = ("Arial", 15),  height = 5, width = 30, command = random_affirmation)
    randomizer_button_affirmations.pack(pady = 50)

    # the label that displays the chosen affirmation
    randomized_affirmation = tk.Label(affirmations_exercise_window, text = "", font = ("Arial", 20),  height = 5)
    randomized_affirmation.pack(pady = 20)

    # button that when clicked, closes the affirmations window
    close_affirmations_window = tk.Button(affirmations_exercise_window, text = "Close", font = ("Arial", 10), height = 2, width = 10, command = close_affirmations)
    close_affirmations_window.pack(padx = 20, pady = 10)


# A function to open the posing game
def posing_exercise_open():
    posing_exercise_window = Toplevel(root)
    posing_exercise_window.title = ("Posing")
    posing_exercise_window.geometry("2900x1200")

    # closes the posing window
    def posing_close():
        posing_exercise_window.destroy()
    
    # Generates a prompt from the dictionary
    def generate_prompt():
        # Turns all of the keys in the dictionary into a list and chooses a random option from them
        chosen_prompt = random.choice(list(posing_descriptions.keys()))
        # Chooses the correct description that matches with the chosen prompt
        prompt_description = posing_descriptions[chosen_prompt]
        # Changes the text on the prompt label to the prompt -- prompt description (f strings go before variables in a string)
        posing_prompt.config(text=f"{chosen_prompt} -- {prompt_description}")

    # All of the posing prompts
    posing_descriptions = {
        "Lion": "Let out a big roar!",
        "Mouse": "Crouch down low and scurry like a mouse!",
        "Seal": "Lie on your tummy and clap your hands together!",
        "Fish": "Lie on the floor and flop around!",
        "Giraffe": "Reach your hands tall like a long neck!",
        "Elephant": "Stretch your arms infront of you like a long trunk",
        "Dog": "Let out some big barks!",
        "Cat": "Meow like a kitty!",
        "Horse": "Gallop in place!",
        "Monkey": "Jump around like a cheeky ape!"
    } 

    # Title label
    posing_exercise_title = tk.Label(posing_exercise_window, text = "Animal Posing", font = ("Arial", 40))
    posing_exercise_title.pack(pady = 50)

    # Prompt label
    posing_prompt = tk.Label(posing_exercise_window, text = " ", font = ("Arial", 30))
    posing_prompt.pack(pady = 30)

    # Button to generate a prompt when clicked
    generate_prompt_button = tk.Button(posing_exercise_window, text = "Generate Prompt", font = ("Arial", 15), width = 20, height = 1, command = generate_prompt)
    generate_prompt_button.pack(pady = 30)

    # Button that closes the application when clicked
    close_posing = tk.Button(posing_exercise_window, text = "Close", font = ("Arial", 10), width = 10, height = 1, command = posing_close)
    close_posing.pack(pady = 10)

    
# A function to open the journaling exercise
def journal_exercise_open():
    journal_exercise_window = Toplevel(root)
    journal_exercise_window.title("Wellbeing Journal")
    journal_exercise_window.geometry("2900x1200")

    # Function that closes the journal
    def close_journal():
        journal_exercise_window.destroy()

    # Function that saves the journal entries
    def save_journal():
        global journal_entries
        
        # pulls the text from the date and entry textboxes and assigns it to the date and entry variables
        date = journaling_date.get("1.0",'end-1c')
        entry = journaling_space.get("1.0",'end-1c')

        # If nothing is assigned to the date or entry variables (meaning one of them is empty) A warning appears alerting the user and the journal entry does not save
        if not date or not entry:
            messagebox.showwarning(" ", "Please make sure to fill out all both a date and an entry before saving!", parent = journal_exercise_window)
            return
        
        # makes the key for journal entries assigned to the date variable, and the item becomes the entry variable
        journal_entries[date] = entry

        # Shows a messagebox that confirms the saving of the journal entries (f string so a variable can be used in a string)
        messagebox.showinfo(" ", f"Your entry for {date} has been saved!", parent = journal_exercise_window)
        

    # Function that allows the user to view past entries - opens up a new window
    def view_past_entries():
        journal_all_window = Toplevel(root)
        journal_all_window.title("Previous Entries")
        journal_all_window.geometry("500x600")

        # for every date and entry in the journal dictionary
        for date, entry in journal_entries.items():
            # creates a label that displays the entry with the date and the text.
            entry_label = tk.Label(journal_all_window, text = f"{date}: \n {entry}", font = ("Arial", 10))
            entry_label.pack()


    # title label
    journal_exercise_title = tk.Label(journal_exercise_window, text = "Wellbeing Journal", font = ("Arial", 40))
    journal_exercise_title.pack(pady = 50)

    # Brief for the journal
    journal_brief = tk.Label(journal_exercise_window, text = "What's on your mind today?\n \n Did anything good happen today? Or did something not go as well? Feel free to let it all go", font = ("Arial", 15))
    journal_brief.pack(pady = 10)

    # A grid to store the date and date textbox next to eachother
    date_grid = tk.Frame(journal_exercise_window)
    date_grid.pack(pady = 10)

    # Date prompt
    date_label = tk.Label(date_grid, text = "Date: ", font = ("Arial", 10))
    date_label.grid(row = 0, column = 0)

    # Textbox for storing the date
    journaling_date = tk.Text(date_grid, font = ("Arial", 10), width = 20, height = 1)
    journaling_date.grid(row = 0, column = 1)

    # Space for writing
    journaling_space = tk.Text(journal_exercise_window, font = ("Arial", 10), width = 120, height = 14)
    journaling_space.pack(pady = 5)

    # Button that saves the journal entries when clicked
    save_entries_button = tk.Button(journal_exercise_window, font = ("Arial", 10), text = "Save", width = 10, height = 1, command = save_journal)
    save_entries_button.pack(pady = 10)

    # Button that displays the past entries when clicked
    past_entries_button = tk.Button(journal_exercise_window, font = ("Arial", 10), text = "Past Entries", width = 10, height = 1, command = view_past_entries)
    past_entries_button.pack(pady = 10)

    # Button that closes the window when clicked
    close_journal_button = tk.Button(journal_exercise_window, font = ("Arial", 10), text = "Close", width = 10, height = 1, command = close_journal)
    close_journal_button.pack(pady = 10)


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