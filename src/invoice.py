winning_numbers = ['94899145','71143793', '41055355']
# Unit test
def get_last_n_digits(ticket, n):
    return ticket[-n:]

if __name__ == "__main__":
    ticket = '94899145'
    last_4_digits = get_last_n_digits(ticket, 4)
    assert last_4_digits == '9145'