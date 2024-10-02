#Building the GUI.
#Need to study and learn more about tkinter!
from tkinter import *
from tkinter import ttk
import asyncio
import aiohttp
import pandas as pd
import matplotlib.pyplot as plt

from understat import Understat
from mplsoccer import VerticalPitch





def test():
    year_label.config(text=year_combo.get())

def shotPlot(data, name):
    data['X'] = data['X'] * 100
    data['Y'] = data['Y'] * 100

    total_shots = data.shape[0]
    total_goals = data[data['result'] == 'Goal'].shape[0]
    total_xG = data['xG'].sum()
    xG_per_shot = total_xG / total_shots
    points_avg_dist = data['X'].mean()
    actual_avg_dist = 120 - (data['X'] * 1.2).mean()

    background_color = '#0C0D0E'
    import matplotlib.font_manager as font_manager
    font_path = './fonts/Arvo-Regular.ttf'
    font_props = font_manager.FontProperties(fname = font_path)

    fig = plt.figure(figsize=(8,12))
    fig.patch.set_facecolor(background_color)

    ax1 = fig.add_axes([0, .7, 1, .2])
    ax1.set_facecolor(background_color)
    ax1.set_xlim(0,1)
    ax1.set_ylim(0,1)
    ax1.set_axis_off()
    ax1.text(
        x=.5,
        y=.85,
        s= name,
        fontsize=20,
        fontproperties=font_props,
        fontweight='bold',
        color='white',
        ha='center'
    )

    ax1.text(
        x=.5,
        y=.70,
        s= 'All shots in the Premier League 2024 Season',
        fontsize=14,
        fontproperties=font_props,
        fontweight='bold',
        color='white',
        ha='center'
    )

    ax1.text(
        x=.25,
        y=.5,
        s= 'Low Quality Chance',
        fontsize=12,
        fontproperties=font_props,
        fontweight='bold',
        color='white',
        ha='center'
    )

    ax1.scatter(
        x= .37,
        y= .53,
        s= 100,
        color = background_color,
        edgecolor='white',
        linewidth= .8
    )

    ax1.scatter(
        x= .42,
        y= .53,
        s= 200,
        color = background_color,
        edgecolor='white',
        linewidth= .8
    )

    ax1.scatter(
        x= .48,
        y= .53,
        s= 300,
        color = background_color,
        edgecolor='white',
        linewidth= .8
    )

    ax1.scatter(
        x= .54,
        y= .53,
        s= 400,
        color = background_color,
        edgecolor='white',
        linewidth= .8
    )

    ax1.scatter(
        x= .6,
        y= .53,
        s= 500,
        color = background_color,
        edgecolor='white',
        linewidth= .8
    )


    ax1.text(
        x=.75,
        y=.5,
        s= 'High Quality Chance',
        fontsize=12,
        fontproperties=font_props,
        fontweight='bold',
        color='white',
        ha='center'
    )

    ax1.text(
        x=.45,
        y=.28,
        s=f'Goal',
        fontsize=10,
        fontproperties=font_props,
        color='white',
        ha='right'
    )

    ax1.scatter(
        x=.47,
        y=.3,
        s=100,
        color='red',
        edgecolor='white',
        linewidth=.8,
        alpha=.7
    )
    ax1.scatter(
    x=.53,
    y=.3,
    s=100,
    color=background_color,
    edgecolor='white',
    linewidth=.8
    )   

    ax1.text(
        x=.55,
        y=.28,
        s=f'No Goal',
        fontsize=10,
        fontproperties=font_props,
        color='white',
        ha='left'
    )


    ax2 = fig.add_axes([.05, .25, .9, .5])
    ax2.set_facecolor(background_color)
    ax2.set_axis_off()

    pitch = VerticalPitch(
        pitch_type='opta',
        half=True,
        pitch_color=background_color,
        pad_bottom=.5,
        line_color='white',
        linewidth=.75,
        axis=True,
        label=True
    )
    pitch.draw(ax=ax2)

    ax2.scatter(
        x=90, 
        y=points_avg_dist, 
        s=100,
        color='white',
        linewidth=.8
    )

    ax2.plot([90,90], [100, points_avg_dist], color='white', linewidth=2)
    ax2.text(
        x=90,
        y= points_avg_dist - 4,
        s=f'Average Distance \n{actual_avg_dist: .1f} yards',
        fontsize=10,
        fontproperties = font_props,
        color='white',
        ha='center'
    )

    for x in data.to_dict(orient='records'):
        pitch.scatter(
            x['X'],
            x['Y'],
            s= 300 * x['xG'],
            color = 'red' if x['result'] == 'Goal' else background_color,
            ax=ax2,
            alpha=.7,
            linewidth=.8,
            edgecolor='white'
        )

    ax3 = fig.add_axes([0, .2, 1, .05])
    ax3.set_facecolor(background_color)
    ax3.set_axis_off()

    ax3.text(
        x=.20,
        y=.5,
        s='Shots',
        fontsize=20,
        fontproperties=font_props,
        fontweight='bold',
        color='white',
        ha='center'
    )
    ax3.text(
        x=.20,
        y=0,
        s=f'{total_shots}',
        fontsize=16,
        fontproperties=font_props,
        color='red',
        ha='center'
    )

    ax3.text(
        x=.40,
        y=.5,
        s='Goals',
        fontsize=20,
        fontproperties=font_props,
        fontweight='bold',
        color='white',
        ha='center'
    )

    ax3.text(
        x=.40,
        y=0,
        s=f'{total_goals}',
        fontsize=16,
        fontproperties=font_props,
        color='red',
        ha='center'
    )


    ax3.text(
        x=.60,
        y=.5,
        s='xG',
        fontsize=20,
        fontproperties=font_props,
        fontweight='bold',
        color='white',
        ha='center'
    )

    ax3.text(
        x=.60,
        y=0,
        s=f'{total_xG: .2f}',
        fontsize=16,
        fontproperties=font_props,
        color='red',
        ha='center'
    )

    ax3.text(
        x=.80,
        y=.5,
        s='xG/Shot',
        fontsize=20,
        fontproperties=font_props,
        fontweight='bold',
        color='white',
        ha='center'
    )

    ax3.text(
        x=.80,
        y=0,
        s=f'{xG_per_shot: .2f}',
        fontsize=16,
        fontproperties=font_props,
        color='red',
        ha='center'
    )
    plt.show()


async def get_players():
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        players = await understat.get_league_players(
            'epl', year_combo.get()
        )
        return players

async def get_shots_24(player_id):
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        player_shots = await understat.get_player_shots(
            player_id, {'season': str(year_combo.get())}
        )
        return player_shots

def call():
    loop = asyncio.get_event_loop()
    players = loop.run_until_complete(get_players())
    # turn that data into a DataFrame
    playersDF = pd.DataFrame(players)
    playersDF['shots'] = playersDF['shots'].apply(pd.to_numeric)
    # find the top ten players with the most shots
    top_10 = playersDF.nlargest(10, 'shots')
    shotData = []
    top_dic = top_10.to_dict(orient='records')
    for x in top_dic:
        loop = asyncio.get_event_loop()
        data = loop.run_until_complete(get_shots_24(x['id']))
        dataDF = pd.DataFrame(data)
        dataDF[['xG', 'X', 'Y']] = dataDF[['xG', 'X', 'Y']].apply(pd.to_numeric)
        shotData.append(dataDF)
    # build new window with buttons of players
    new_window = Toplevel()
    for i in range(len(top_dic)):
        button = ttk.Button(new_window, text=top_dic[i]['player_name'], command=lambda i=i: shotPlot(shotData[i], top_dic[i]['player_name']))
        button.pack()



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
year_combo.set(2024)

year_label = Label(root, text='', font=("Helvetica", 18))
year_label.pack(pady=20)

year_button = Button(root, text='Submit', command=call)
year_button.pack(pady=20)

root.mainloop()