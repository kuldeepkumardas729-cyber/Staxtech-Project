import tkinter as tr

def click(val):
    text= display.get()
    display.delete(0, tr.END)
    display.insert(0, text + str(val))
    preview()

def clear_dis():
    display.delete(0, tr.END)
    preview_label.config(text="")

def calci():
    try:
        exp= display.get().replace('×', '*').replace('÷', '/')
        ans= eval(exp)
        display.delete(0, tr.END)
        display.insert(0, str(ans))
        preview_label.config(text="")  # Clear preview after equal
    except Exception:
        display.delete(0, tr.END)
        display.insert(0, "Error")
        preview_label.config(text="")

def preview():
    try:
        exp = display.get().replace('×', '*').replace('÷', '/')
        if exp:  # Only if input is not empty
            ans = eval(exp)
            preview_label.config(text=f"= {ans}")
        else:
            preview_label.config(text="")
    except:
        preview_label.config(text="")

# Main window
root = tr.Tk()
root.title("Nikki's calculator")
root.configure(bg="black")
root.resizable(False, False)

# Label
title_label = tr.Label(root, text=" simple calculator by NY", font=("Arial", 14, "bold"),
                       bg="black", fg="#FFD700")
title_label.grid(row=0, column=0, columnspan=4, pady=(8, 4))

# Entry field
display = tr.Entry(root, font=("Arial", 24), bd=3, relief=tr.FLAT,
                   justify="right", bg="black", fg="white", insertbackground="white")
display.grid(row=1, column=0, columnspan=4, padx=8, pady=(0, 2), ipady=10, sticky="we")

# Preview label
preview_label = tr.Label(root, text="", font=("Arial", 16),
                         bg="black", fg="#AAAAAA", anchor="e", padx=10)
preview_label.grid(row=2, column=0, columnspan=4, sticky="we", pady=(0, 6))

# Buttons
buttons = [
    ('C', 3, 0), ('÷', 3, 1), ('×', 3, 2), ('-', 3, 3),
    ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('+', 4, 3),
    ('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('.', 5, 3),
    ('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('=', 6, 3),
    ('0', 7, 0),
]

for (text, row, col) in buttons:
    if text == 'C':
        btn = tr.Button(root, text=text, font=("Arial", 13),
                        bg="#FFD700", fg="black", command=clear_dis)
    elif text == '=':
        btn = tr.Button(root, text=text, font=("Arial", 13),
                        bg="#FFD700", fg="black", command=calci)
        btn.grid(row=row, column=col, rowspan=2, padx=3, pady=3, sticky="nsew")
        continue
    else:
        btn = tr.Button(root, text=text, font=("Arial", 13),
                        bg="white", fg="black", command=lambda t=text: click(t))
    btn.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")

# 00 button
double_zero = tr.Button(root, text='00', font=("Arial", 13),
                     bg="white", fg="black", command=lambda: click('00'))
double_zero.grid(row=7, column=1, columnspan=2, padx=3, pady=3, sticky="nsew")

# Grid adjustments
for i in range(8):
    root.grid_rowconfigure(i, weight=1, minsize=35)
for i in range(4):
    root.grid_columnconfigure(i, weight=1, minsize=45)

# Main loop
root.mainloop()
