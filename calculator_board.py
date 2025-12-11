import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear_entry():
    entry.delete(0, tk.END)

def button_click(char):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(char))

# Create the main window
root = tk.Tk()
root.title("Calculator Board")

# Create an entry widget for display
entry = tk.Entry(root, width=30, borderwidth=5, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define calculator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 3)
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == '0':
        btn = tk.Button(root, text=text, padx=30, pady=20, font=('Arial', 16), command=lambda t=text: button_click(t))
        btn.grid(row=row, column=col, columnspan=2)
    else:
        btn = tk.Button(root, text=text, padx=30, pady=20, font=('Arial', 16), command=lambda t=text: button_click(t))
        btn.grid(row=row, column=col)

# Special buttons
clear_btn = tk.Button(root, text="C", padx=30, pady=20, font=('Arial', 16), command=clear_entry)
clear_btn.grid(row=4, column=2)

equal_btn = tk.Button(root, text="=", padx=30, pady=20, font=('Arial', 16), command=calculate)
equal_btn.grid(row=5, column=3)


# Run the application
root.mainloop()
