winning_numbers = ['94899145','71143793', '41055355']

def get_last_n_digits(ticket, n):
    return ticket[-n:]

def get_max_maches_for_win_num(ticket, win_num):
    match_count = 0
    for i in range(3,9):
        t = get_last_n_digits(ticket, i)
        w = get_last_n_digits(win_num, i)
        if t == w:
            match_count = i
        else:
            break
    return match_count


