#Building the GUI.
#Need to study and learn more about tkinter!
from tkinter import *
from tkinter import ttk


def test():
    year_label.config(text=year_combo.get())

root = Tk()
root.title("Premier League Shooters!")
root.geometry('600x400')

# Create a ComboBox
year_list = [2018, 2019,
             2020, 2021,
             2022, 2023,
             2024]
year_combo = ttk.Combobox(root, values=year_list, state='readonly')
year_combo.pack(pady=20)

#set default year
year_combo.set('2024')

year_label = Label(root, text='', font=("Helvetica", 18))
year_label.pack(pady=20)

year_button = Button(root, text='Submit', command=test)
year_button.pack(pady=20)



root.mainloop()