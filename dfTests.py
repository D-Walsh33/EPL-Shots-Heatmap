import pandas as pd
shotDataDF = pd.read_csv(f'./data/topShooters2024.csv')
shotDataDF[['xG', 'X', 'Y']] = shotDataDF[['xG', 'X', 'Y']].apply(pd.to_numeric)

print(shotDataDF[shotDataDF['player'] == shotDataDF['player'].value_counts().index[0]])
