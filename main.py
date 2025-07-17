from tkinter import *
from tkinter import ttk
import shotPlot
import pandas as pd

data = None
players = None

window = Tk()
window.title('Premier League Shots Heatmap')

select_label = Label(text='Select a year:', font=('Arial', 25, 'bold'))
select_label.pack()

def generate_buttons(data, players):
    for player in players:
        player_data = data[data['player'] == player]
        new_button = Button(text=player, command=lambda player=player: shotPlot.shotPlot(player_data, player))
        new_button.pack()


def year_combo_selected(event):
    global data
    global players
    data = pd.read_csv(f'./data/topShooters{yearvar.get()}.csv')
    players = data['player'].unique()

    generate_buttons(data, players)



years = [str(year) for year in range(2025, 2010, -1)]
yearvar = StringVar()
year_combo = ttk.Combobox(textvariable=yearvar)
year_combo.bind('<<ComboboxSelected>>', year_combo_selected, )
year_combo['values'] = years
year_combo.pack()

window.mainloop()
