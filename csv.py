def num_or_str(x):
    """The argument is a string; convert to a number if
       possible, or strip it."""
    try:
        return int(x)
    except ValueError:
        try:
            return float(x)
        except ValueError:
            return str(x).strip()


def parse_csv(input, delim=','):
    lines = [line for line in input.splitlines() if line.strip()]
    final_list = []
    for line in lines:
        words = line.split(delim)
        player_list = []
        for word in words:
            myword = word.strip('\n').replace('\"', '')
            myword = num_or_str(myword)
            player_list.append(myword)
        final_list.append(player_list)
    return final_list