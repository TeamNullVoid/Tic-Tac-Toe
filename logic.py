def check_who_won(moves: list):
    won = (False, 0)
    if moves[0] == moves[1] == moves[2] != 0:
        won = (True, moves[0])
    elif moves[3] == moves[4] == moves[5] != 0:
        won = (True, moves[3])
    elif moves[6] == moves[7] == moves[8] != 0:
        won = (True, moves[6])
    elif moves[0] == moves[3] == moves[6] != 0:
        won = (True, moves[0])
    elif moves[1] == moves[4] == moves[7] != 0:
        won = (True, moves[1])
    elif moves[2] == moves[5] == moves[8] != 0:
        won = (True, moves[2])
    elif moves[2] == moves[4] == moves[6] != 0:
        won = (True, moves[2])
    elif moves[0] == moves[4] == moves[8] != 0:
        won = (True, moves[0])
    return won


def check_draw(moves: list):
    if 0 not in moves:
        return True
    else:
        return False
