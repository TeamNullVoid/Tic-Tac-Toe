def check_who_won(moves: list):
    won = False
    if moves[0] == moves[1] == moves[2]:
        won = True
    elif moves[3] == moves[4] == moves[5]:
        won = True
    elif moves[6] == moves[7] == moves[8]:
        won = True
    elif moves[0] == moves[3] == moves[6]:
        won = True
    elif moves[1] == moves[4] == moves[7]:
        won = True
    elif moves[2] == moves[5] == moves[8]:
        won = True
    elif moves[2] == moves[4] == moves[6]:
        won = True
    elif moves[0] == moves[4] == moves[8]:
        won = True
    return won
