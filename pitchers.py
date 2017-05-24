import datetime
from my_csv import *
import csv
import mlbgame


def create_pitcher_list(csv_file):
    date = datetime.datetime.now()

    data = open(csv_file)
    data_lines = data.readlines()
    data_lines.pop(0)

    linestring = ""
    for line in data_lines:
        linestring += line

    stringset = parse_csv(linestring)
    day = mlbgame.day(date.year, date.month, date.day)
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
                player_list = [{"Name": pitcher[0]}, {"Team": team}, {"Opponent": team_home}, {"ERA": pitcher[2]},
                               {"BABIP": pitcher[3]}, {"SIERA": pitcher[4]}, {"xFIP": pitcher[5]},
                               {"SwStr%": pitcher[6]}, {"K%": pitcher[7]}, {"GB%": pitcher[8]}, {"FB%": pitcher[9]},
                               {"Contact%": pitcher[10]}, {"Soft%": pitcher[11]}, {"Med%": pitcher[12]},
                               {"Hard%": pitcher[13]}]
                break
            elif team == team_home:
                player_list = [{"Name": pitcher[0]}, {"Team": team}, {"Opponent": team_away}, {"ERA": pitcher[2]},
                               {"BABIP": pitcher[3]}, {"SIERA": pitcher[4]}, {"xFIP": pitcher[5]},
                               {"SwStr%": pitcher[6]}, {"K%": pitcher[7]}, {"GB%": pitcher[8]}, {"FB%": pitcher[9]},
                               {"Contact%": pitcher[10]}, {"Soft%": pitcher[11]}, {"Med%": pitcher[12]},
                               {"Hard%": pitcher[13]}]
                break
        if len(player_list) == 0:
            player_list = [{"Name": pitcher[0]}, {"Team": team}]
        pitcher_list.append(player_list)

    return pitcher_list


# Fix csv writing
def insert_throwing_arm_to_list(p_list):
    count = 0
    for pitcher in p_list:
        x = csv.reader(open("Pitchers_TA.csv"))
        lines = [l for l in x]
        name_exist = False
        for line in lines:
            if pitcher[0]['Name'] == line[0]:
                player = {'Throws': line[1]}
                p_list[count].insert(1, player)
                name_exist = True
                break
        if not name_exist:
            list_length = len(lines)
            print(pitcher[0]['Name'] + " is not on the list.\n")
            arm = input("What is " + pitcher[0]['Name'] + "'s throwing arm? ")
            correct_arm = False
            while not correct_arm:
                if arm is 'Right' or arm is 'Left':
                    print("Invalid input: Please type Right or Left.\n")
                    arm = input("What is " + pitcher[0]['Name'] + "'s throwing arm? ")
                else:
                    print("Is " + arm + " correct?\n")
                    y_or_n = input("Type Y or N")
                    if y_or_n is 'Y':
                        player = {'Throws': arm}
                        p_list[count].insert(1, player)
                        new_line = [pitcher[0]['Name'], arm]
                        lines.insert(list_length, new_line)
                        writer = csv.writer(open('Pitchers_TA.csv', 'w'))
                        writer.writerows(lines)
                        correct_arm = True
                    elif y_or_n is 'N':
                        arm = input("What is " + pitcher[0]['Name'] + "'s throwing arm? ")
            s = 0
        v = pitcher[0]['Name']
        count += 1
        c = 0
