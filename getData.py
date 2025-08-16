import asyncio
import aiohttp
import pandas as pd


from understat import Understat

#years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
years = [2025]


async def get_players_prem(year):
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        players = await understat.get_league_players(
            'epl', year
        )
        return players

async def get_shots(player_id):
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        player_shots = await understat.get_player_shots(
            player_id, {'season': str(year)}
        )
        return player_shots
for year in years:  
    loop = asyncio.get_event_loop()
    players = loop.run_until_complete(get_players_prem(year))

    # turn that data into a DataFrame
    playersDF = pd.DataFrame(players)
    playersDF['shots'] = playersDF['shots'].apply(pd.to_numeric)

    # find the top ten players with the most shots
    top_10 = playersDF.nlargest(10, 'shots')

    top_dic = top_10.to_dict(orient='records')

    #print(top_dic)

    shotData = []

    for x in top_dic:
        loop = asyncio.get_event_loop()
        data = loop.run_until_complete(get_shots(x['id']))
        dataDF = pd.DataFrame(data)
        dataDF[['xG', 'X', 'Y']] = dataDF[['xG', 'X', 'Y']].apply(pd.to_numeric)
        shotData.append(dataDF)

    for i in range(len(shotData)):
        if i == 0:
            shotData[i].to_csv(f'./data/topShooters{year}.csv', mode='w')
        else:
            shotData[i].to_csv(f'./data/topShooters{year}.csv', mode='a', header=False)