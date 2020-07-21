import tkinter as tk

root = tk.Tk()
root.title("Weight Converter"),
#ikon = tk.PhotoImage(file = "w_img.png")
#root.iconphoto(False, ikon)
root.geometry("320x190+334+50")

machine_output = tk.Label(root)
machine_output.config(text = "Weight:")
machine_output.pack()

user_input = tk.Entry(root)
user_input.pack()

entry = None

mode_options = [
    "Select",
    "Kg",
    "Lb"
]

clicked = tk.StringVar()
clicked.set(mode_options[0])

drop = tk.OptionMenu(root, clicked, *mode_options)
drop.pack()

def getoutput():
    weight = int(user_input.get())
    choose = clicked.get()
    if choose == mode_options[2]:
        converted = weight * 0.45
        output = (f"You are {converted} kilos.")
    elif choose == mode_options[1]:
        converted = weight / 0.45
        output = (f"You are {converted} pounds.")
    else:
        output = "Please select a valid mass unit. Weight:"
    machine_output.config(text = output)

enter_button = tk.Button(root)
enter_button.config(text = "Okay", command = getoutput)
enter_button.pack()



root.mainloop()

