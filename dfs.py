# dfs main
from __future__ import print_function
import mlbgame
from csv import *
import re
import string

def mlb_main():
    data = open("Fangraphs_Leaderboard.csv")
    data_lines = data.readlines()

    linestring = ""
    for line in data_lines:
        linestring += line
    stringset = parse_csv(linestring)
    stringset.pop(0)
    day = mlbgame.day(2017, 5, 15)
    pitcher_list = []
    for pitcher in stringset:
        player_list = []
        team = pitcher[1]
        if team == "Diamondbacks":
            team = "D-backs"
        for game in day:
            team_away = game.away_team
            team_home = game.home_team
            if team == team_away:
                player_list = [{"Name": pitcher[0]}, {"Team": team}, {"Opponent": team_home}, {"ERA": pitcher[15]},
                               {"xFIP": pitcher[17]}]
                break
            elif team == team_home:
                player_list = [{"Name": pitcher[0]}, {"Team": team}, {"Opponent": team_away}, {"ERA": pitcher[15]},
                               {"xFIP": pitcher[17]}]
                break
        if len(player_list) == 0:
            player_list = [{"Name": pitcher[0]}, {"Team": team}]
        pitcher_list.append(player_list)

    x=0


if __name__ == "__main__":
    mlb_main()