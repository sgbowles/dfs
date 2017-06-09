# dfs main
from __future__ import print_function
from pitchers import *
from stack import *

def mlb_main():
    stack_main()
    daily_pitchers_list = create_pitcher_list("Fangraphs_Leaderboard.csv")
    daily_pitchers_list = insert_throwing_arm_to_list(daily_pitchers_list)
    x = 98



if __name__ == "__main__":
    mlb_main()