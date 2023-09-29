import tkinter as tk
import random

# Create the main application window
root = tk.Tk()
root.title('Dice Rolling App')

# Function to roll the dice
def roll_dice():
    # Generate random values for two dice (1 to 6)
    die1_value = random.randint(1, 6)
    die2_value = random.randint(1, 6)
    
    # Load ASCII art images of dice faces
    die1_image = dice_images[die1_value - 1]
    die2_image = dice_images[die2_value - 1]
    
    # Update the dice labels with the new images
    die1_label.config(text=die1_image)
    die2_label.config(text=die2_image)

# Create and configure the Roll Dice button
roll_button = tk.Button(root, text='Roll Dice', command=roll_dice, padx=20, pady=10, font=("Helvetica", 14))
roll_button.pack(pady=20)

# List of ASCII art images for dice faces
dice_images = [
    '  _______  \n |       | \n |   ●   | \n |       | \n  ‾‾‾‾‾‾‾  ',  # Die 1
    '  _______  \n |     ● | \n |       | \n | ●     | \n  ‾‾‾‾‾‾‾  ',  # Die 2
    '  _______  \n | ●     | \n |   ●   | \n |     ● | \n  ‾‾‾‾‾‾‾  ',  # Die 3
    '  _______  \n | ●   ● | \n |       | \n | ●   ● | \n  ‾‾‾‾‾‾‾  ',  # Die 4
    '  _______  \n | ●   ● | \n |   ●   | \n | ●   ● | \n  ‾‾‾‾‾‾‾  ',  # Die 5
    '  _______  \n | ●   ● | \n | ●   ● | \n | ●   ● | \n  ‾‾‾‾‾‾‾  '   # Die 6
]

# Create labels for the dice with updated styles
label_style = {"font": ("Courier", 16)}
die1_label = tk.Label(root, text='', **label_style)
die1_label.pack()

die2_label = tk.Label(root, text='', **label_style)
die2_label.pack()

# Center the window on the screen
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")

# Run the main application loop
root.mainloop()
