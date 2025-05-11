import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime("%I:%M:%S %p")
    label.config(text=current_time)
    label.after(1000,update_time)
root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x200")
label = tk.Label(root,font=('calibri',40,'bold'),background='black',foreground='#00ff00')
label.pack(anchor="center",fill="both", expand=True) 
update_time()
root.mainloop()