import tkinter as tk


def ConnectToPi():
    print("Connecting")


root = tk.Tk()

# "Connect To Pi" Button

connect = tk.Button(root, text="Connect To Pi",
                    command=ConnectToPi, width=15, height=3)

connect.pack(side="bottom")

# Quit Button

quitBt = tk.Button(root, command=quit, text="Quit", foreground="Red")

quitBt.pack(side="top")

root.geometry("500x400")
root.mainloop()
