import tkinter as tk
from tkinter import ttk
import ttkthemes
import random

def generate_numbers():
    try:
        count = int(count_entry.get())
        max_num = int(max_num_entry.get())
        numbers = [random.randint(1, max_num) for _ in range(count)]
        
        if sort_var.get():
            numbers.sort()
            
        filename = f"{count}.txt"
        with open(filename, 'w') as file:
            file.write('\n'.join(map(str, numbers)))
            
        result_label.config(text=f"Numbers saved to {filename}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Create main window
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme("equilux")  # Modern dark theme
root.title("Random Number Generator")
root.geometry("400x500")

# Create main frame
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

# Title
title_label = ttk.Label(
    main_frame, 
    text="Random Number Generator",
    font=("Helvetica", 16, "bold")
)
title_label.pack(pady=20)

# Number count input
count_frame = ttk.LabelFrame(main_frame, text="How many numbers?", padding="10")
count_frame.pack(fill=tk.X, pady=10)
count_entry = ttk.Entry(count_frame)
count_entry.pack(fill=tk.X)

# Max number input
max_frame = ttk.LabelFrame(main_frame, text="Maximum number?", padding="10")
max_frame.pack(fill=tk.X, pady=10)
max_num_entry = ttk.Entry(max_frame)
max_num_entry.pack(fill=tk.X)

# Sort option
sort_var = tk.BooleanVar()
sort_check = ttk.Checkbutton(
    main_frame, 
    text="Sort numbers?",
    variable=sort_var
)
sort_check.pack(pady=10)

# Generate button
generate_btn = ttk.Button(
    main_frame,
    text="Generate Numbers",
    command=generate_numbers,
    style="Accent.TButton"
)
generate_btn.pack(pady=20)

# Result label
result_label = ttk.Label(
    main_frame,
    text="Enter values and click Generate",
    wraplength=300
)
result_label.pack(pady=10)

# Style configuration
style = ttk.Style()
style.configure("Accent.TButton", font=("Helvetica", 12))

root.mainloop()