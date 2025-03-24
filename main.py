import tkinter as tk
from tkinter import messagebox


def int_to_bin(num, bits=8):
    """Convert an integer to a binary string with a fixed number of bits."""
    return format(num, f'0{bits}b')


def perform_operation(op):
    try:
        a = int(entry_a.get())
        if op != 'NOT':
            b = int(entry_b.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers.")
        return

    bits = 8  # You can adjust this bit width as needed.
    if op == 'AND':
        res = a & b
    elif op == 'OR':
        res = a | b
    elif op == 'XOR':
        res = a ^ b
    elif op == 'NOT':
        # For NOT, we operate only on a, and ensure the result fits in 'bits' width.
        res = ~a & ((1 << bits) - 1)
    elif op == 'Left Shift':
        res = (a << b) & ((1 << bits) - 1)
    elif op == 'Right Shift':
        res = a >> b
    else:
        res = 0

    result_decimal.set(f"Result (Decimal): {res}")
    result_binary.set(f"Result (Binary): {int_to_bin(res, bits)}")


# Create the main application window
root = tk.Tk()
root.title("Bitwise Visualizer and Calculator")

# Define StringVars to update the result labels dynamically
result_decimal = tk.StringVar()
result_binary = tk.StringVar()

# Layout: Create labels and entry fields for user input
tk.Label(root, text="Enter first integer:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Enter second integer (or shift amount):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=5, pady=5)

# Create buttons for each bitwise operation
operations = ['AND', 'OR', 'XOR', 'NOT', 'Left Shift', 'Right Shift']
row = 2
for op in operations:
    btn = tk.Button(root, text=op, command=lambda op=op: perform_operation(op))
    btn.grid(row=row, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
    row += 1

# Labels to display the results
tk.Label(root, textvariable=result_decimal).grid(row=row, column=0, columnspan=2, padx=5, pady=5)
row += 1
tk.Label(root, textvariable=result_binary).grid(row=row, column=0, columnspan=2, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
