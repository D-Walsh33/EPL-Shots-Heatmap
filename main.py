from tkinter import *
from tkinter import ttk
import shotPlot
import pandas as pd

data = None
players = None
player_buttons = []
window = Tk()
window.title('Premier League Shots Heatmap')
window.geometry("400x450")
select_label = Label(text='Select a year:', font=('Arial', 25, 'bold'))
select_label.pack()

def generate_buttons(data, players, year):
    global player_buttons
    for button in player_buttons:
        button.destroy()
    for player in players:
        new_button = Button(text=player, command=lambda player=player: shotPlot.shotPlot(data[data['player']== player], player, year))
        new_button.pack()
        player_buttons.append(new_button)


def year_combo_selected(event):
    global data
    global players
    data = pd.read_csv(f'./data/topShooters{yearvar.get()}.csv')
    players = data['player'].unique()

    generate_buttons(data, players, yearvar.get())



years = [str(year) for year in range(2025, 2014, -1)]
yearvar = StringVar()
year_combo = ttk.Combobox(textvariable=yearvar)
year_combo.bind('<<ComboboxSelected>>', year_combo_selected, )
year_combo['values'] = years
year_combo.pack()

window.mainloop()
