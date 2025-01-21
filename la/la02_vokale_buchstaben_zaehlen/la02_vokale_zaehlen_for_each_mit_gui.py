from tkinter import *

root = Tk()
root.title("Vowelcounter")
root.geometry("400x320")    # set starting size of window
root.maxsize(400, 320)      # width x height
root.minsize(400, 320)      # width x height
root.config(bg="#6FAFE7")   # set background color of root window

# Check the input field
def check_input():
    vowels = "aAeEiIoOuU"
    vowel_counter = 0
    
    user_input = input.get()  # get text from Input widget

    for char in user_input:
        if char in vowels:
            vowel_counter += 1

    # Display the result in the output field
    output_field.delete(0, END)  # Clear previous output
    output_field.insert(0, f"Your text has {vowel_counter} vowels.")  # Insert new result

# Heading
heading = Label(root, text="Vowelcounter", bg="#2176C1", fg='white', relief=RAISED)
heading.pack(ipady=5, fill='x')
heading.config(font=("Font", 30))  # change font and size of label

# Input Field
input_frame = Frame(root, bg="#6FAFE7")
input_frame.pack(pady=10)

Label(input_frame, text="Your text to proof:", bg="#6FAFE7").pack(side='left', padx=5)

input = Entry(input_frame, bd=3, width=30)
input.pack(side='right')

# Proof Button
proof_button = Button(root, text="Proof", command=check_input, bg="#6FAFE7", width=15)
proof_button.pack(pady=10)

# Output Field
output_frame = Frame(root, bg="#6FAFE7")
output_frame.pack(pady=10)

output_label = Label(output_frame, text="Result:", bg="#6FAFE7")
output_label.pack(side='left', padx=5)

output_field = Entry(output_frame, bd=3, width=30)
output_field.pack(side='right')

root.mainloop()