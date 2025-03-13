import tkinter as tk
import random
from EmbeddingClasses import Phrase

root = tk.Tk()
root.title("Embedding Test")

runes = ["ᚠ", "ᚢ", "ᚦ", "ᚨ", "ᚱ", "ᚷ", "ᚹ", "ᚺ"]

# Create frames for different sections
entry_frame = tk.Frame(root, borderwidth=2, relief="groove")
button_frame = tk.Frame(root, borderwidth=2, relief="groove")
display_frame = tk.Frame(root, borderwidth=2, relief="groove")

# Use grid to place frames, rowspan for multiple rows
entry_frame.grid(row=0, column=0, padx=5, pady=5)
button_frame.grid(row=1, column=0, padx=5, pady=5)
display_frame.grid(row=0, column=1, rowspan=2, padx=5, pady=5)

# Create entry fields
entry_widgets = []

# Add data entries
entry_label_font = ("Arial", 18) #Default font: TkTextFont
entry_box_width = 50
entry_box_height = 2

for i, rune in enumerate(runes):

    tk.Label(entry_frame, text=rune, font=entry_label_font).grid(row=i, column=0, padx=2, pady=2)
    entry = tk.Text(entry_frame, width=entry_box_width, height=entry_box_height)
    entry.grid(row=i, column=1, padx=2, pady=2)
    entry_widgets.append(entry)

# Define a function to convert values to colors
def get_color(value):
    """maps a -1 to 1 value to a color gradient"""
    normalized = int((value + 1) * 127.5)
    return f"#ff{normalized:02x}{255 - normalized:02x}" # A Red-Blue Gradient

# Define display region for heatmap
display_label_font = ("Arial", 14) #Default font: TkTextFont
heatmap_labels = [[None for _ in range(8)] for _ in range(8)] # <---- This will hold the lables that make up our heatmap.
for i in range(8):
    tk.Label(display_frame, text=runes[i], font=display_label_font).grid(row=i+1, column=0)
    tk.Label(display_frame, text=runes[i], font=display_label_font).grid(row=0, column=i+1)
    for j in range(8):
        rand_color = get_color(random.uniform(-1, 1))
        heatmap_labels[i][j] = tk.Label(display_frame, width =4, height =2, bg=rand_color)
        heatmap_labels[i][j].grid(row=i+1, column=j+1)

# Define function for button
def print_entries():
    """prints out every entry for testing purposes"""
    for rune, entry in zip(runes, entry_widgets):
        print(f"{rune}: {entry.get('1.0', 'end-1c')}")

def display_cosine():
    phrases = []
    for entry in entry_widgets:
        phrases.append(Phrase(entry.get('1.0', 'end-1c')))
    for i in range(8):
        for j in range(8):
            heatmap_labels[i][j].config(bg = get_color(phrases[i].cosine_similarity(phrases[j])))

#Add buttons
tk.Button(button_frame, text="Submit", command=display_cosine).pack()

if __name__=="__main__":
    root.mainloop()
