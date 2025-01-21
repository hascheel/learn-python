import tkinter as tk

# Verarbeiten von Klicks auf den Buttons
def button_click(event):
    global entry_var
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Fehler")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

# Hauptfenster (Grid aus 4 Spalten)
root = tk.Tk()
root.title("Daschnreschnoah")

# Heading
heading = tk.Label(root, text="Daschnreschnoah", bg="#2176C1", fg='white', relief=tk.RAISED)
heading.pack(ipady=5, fill='x')
heading.config(font=("Font", 30))  # change font and size of label
heading.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Eingabefeld
entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font=("Arial", 20), justify="right")
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Aus Buttons-Array mit foreach ein 4x4 Grid erstellen.
row_val, col_val = 2, 0
for button_text in buttons:
    button = tk.Button(
        root, text=button_text, font=("Arial", 18), padx=20, pady=20
    )
    button.grid(row=row_val, column=col_val, padx=5, pady=5)
    button.bind("<Button-1>", button_click)
    col_val += 1
    if col_val > 3:         # Wenn Spalten größer 3 (also 4), dann eine neue Zeile
        col_val = 0
        row_val += 1

# Haupt-Loop starten
root.mainloop()
