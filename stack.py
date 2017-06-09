import mlbgame


def calc_FD(player):
    singles = player.h - player.d - player.t - player.hr
    score = singles * 3 + player.d * 6 + player.t * 9 + player.hr * 12 + player.rbi * 3.5 + player.r * 3.2 + player.bb * 3 + \
            player.sb * 6 + player.hbp * 3
    return score


def stack_stats(stack_info, game):
    # game = mlbgame.day(2017, 6, 8, home="D-backs")[0]
    stats = mlbgame.player_stats(game.game_id)
    order_count = 1
    stack_home = [game.home_team]
    for player in stats['home_batting']:
        if order_count > 9:
            break
        if player.pos == 'P':
            batter = {order_count: 0}
            stack_home.append(batter)
            order_count += 1
        else:
            sub_check = player.bo % 100
            if sub_check == 0:
                FD_points = calc_FD(player)
                batter = {order_count: FD_points}
                stack_home.append(batter)
                order_count += 1

    order_count = 1
    stack_away = [game.away_team]
    for player in stats['away_batting']:
        if order_count > 9:
            break
        if player.pos == 'P':
            batter = {order_count: 0}
            stack_away.append(batter)
            order_count += 1
        else:
            sub_check = player.bo % 100
            if sub_check == 0:
                FD_points = calc_FD(player)
                batter = {order_count: FD_points}
                stack_away.append(batter)
                order_count += 1

    stack_info.append(stack_home)
    stack_info.append(stack_away)
    return stack_info


def sort_stacks(stack_info):
    first = second = third = fourth = fifth = sixth = seventh = eighth = ninth = 0
    for stack in stack_info:
        first += stack[1][1]
        second += stack[2][2]
        third += stack[3][3]
        fourth += stack[4][4]
        fifth += stack[5][5]
        sixth += stack[6][6]
        seventh += stack[7][7]
        eighth += stack[8][8]
        ninth += stack[9][9]
    stack_final = [first, second, third, fourth, fifth, sixth, seventh, eighth, ninth]
    return stack_final



def stack_main():
    day = mlbgame.day(2017, 6, 7)
    stack_info = []
    for game in day:
        stack_info = stack_stats(stack_info, game)
    calculated_stacks = sort_stacks(stack_info)

    s = 0