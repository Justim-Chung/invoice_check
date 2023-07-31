from src.invoice import get_last_n_digits

def test_get_last_3_digits():
    ticket = '94899145'
    last_3_digits = get_last_n_digits(ticket, 3)
    assert last_3_digits == '145'

def test_get_last_8_digits():
    ticket = '94899145'
    last_8_digits = get_last_n_digits(ticket, 8)
    assert last_8_digits == '94899145'