import tkinter as tk

def update_entry(value):
    current = display_var.get()
    display_var.set(current + str(value))

def evaluate():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except:
        display_var.set("Invalid")

def clear_display():
    display_var.set("")

app = tk.Tk()
app.title("Simple Calculator")
app.geometry("320x420")

display_var = tk.StringVar()
entry_box = tk.Entry(app, textvariable=display_var, font=("Arial", 18), bd=10, relief=tk.SUNKEN, justify="right")
entry_box.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

for row_num, row_values in enumerate(buttons):
    for col_num, text in enumerate(row_values):
        if text == '=':
            btn = tk.Button(app, text=text, width=8, height=3, command=evaluate, bg="#87CEFA")
        elif text == 'C':
            btn = tk.Button(app, text=text, width=8, height=3, command=clear_display, bg="#FF6F61")
        else:
            btn = tk.Button(app, text=text, width=8, height=3, command=lambda val=text: update_entry(val))

        btn.grid(row=row_num + 1, column=col_num, padx=5, pady=5)

app.mainloop()
