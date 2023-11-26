import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        output.config(text="Result: " + str(result))
    except:
        output.config(text="Invalid Input")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry field
entry = tk.Entry(window, width=30)
entry.pack(pady=10)

# Create the calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Create the output label
output = tk.Label(window, text="Result: ")
output.pack(pady=10)

# Run the main window's event loop
window.mainloop()
