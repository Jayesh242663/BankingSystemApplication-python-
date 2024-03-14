import tkinter as tk

def on_submit():
    value = entry.get()
    print("Entered text:", value)

# Create the main application window
root = tk.Tk()
root.title("Text Field Example")

# Create a label
label = tk.Label(root, text="Enter text:")
label.pack()

# Create a text field (entry widget)
entry = tk.Entry(root)
entry.pack()

# Create a button to submit the text
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

# Start the Tkinter event loop
root.mainloop()
