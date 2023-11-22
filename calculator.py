import tkinter as tk
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operator_var.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                quotient = num1 / num2
                remainder = num1 % num2
                result_label.config(text=f"Quotient: {quotient}, Remainder: {remainder}")
            else:
                result_label.config(text="Cannot divide by zero")
            return
        else:
            result = "Invalid operator"

        result_label.config(text="Result: " + str(result))

    except ValueError:
        result_label.config(text="Invalid input")

# Create the main window
window = tk.Tk()
window.title("Calculator")  # Set the title of the window

# Labels and Entry widgets for operands
label_num1 = tk.Label(window, text="First Operand:")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack(pady=5)

label_num2 = tk.Label(window, text="Second Operand:")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack(pady=10)

# Radio buttons for operators
operator_var = tk.StringVar()
operator_var.set("+")  # default operator

operator_label = tk.Label(window, text="Select Operator:")
operator_label.pack()

operator_add = tk.Radiobutton(window, text="+", variable=operator_var, value="+")
operator_subtract = tk.Radiobutton(window, text="-", variable=operator_var, value="-")
operator_multiply = tk.Radiobutton(window, text="*", variable=operator_var, value="*")
operator_divide = tk.Radiobutton(window, text="/", variable=operator_var, value="/")

operator_add.pack()
operator_subtract.pack()
operator_multiply.pack()
operator_divide.pack()

# Button to calculate result
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

# Label to display result
result_label = tk.Label(window, text="Result: ")
result_label.pack()

# Start the main event loop
window.mainloop()
