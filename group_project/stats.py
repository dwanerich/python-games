import pandas as pd
from pathlib import Path

stats_file = Path("stats.csv")

def getStats(gameNum, gameCount, numWins):
    currentStats = pd.read_csv(stats_file)
    gameNumber = gameNum + 1
    getGames=1
    getWins=1
    getGames = currentStats.loc[gameNumber, 'numgames']
    getWins = currentStats.loc[gameNumber, 'wins']
    return getGames, getWins


def sendStats(gameNum, gameCount, updWins):
    currentStats = pd.read_csv(stats_file)
    gameNumber = gameNum + 1
    currentStats.loc[gameNumber, 'numgames'] += gameCount
    currentStats.loc[gameNumber, 'wins'] += updWins
    currentStats.to_csv(stats_file, index=False)
    return

def getAllStats():
    return pd.read_csv(stats_file)
