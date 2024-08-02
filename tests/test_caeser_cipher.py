import sys

sys.path.append("../src")

from src.pkg.caeser_cipher import *

def test_find_encrypt_letter_index_with_shift_less_than_26():
    assert find_encrypt_letter_index(3, 5) == 8
    assert find_encrypt_letter_index(5, 8) == 13


def test_find_encrypt_letter_index_with_shift_greater_than_26():
    assert find_encrypt_letter_index(3, 50) == 1
    assert find_encrypt_letter_index(9, 100) == 5

def test_find_decrypt_letter_index_with_shift_less_than_26():
    assert find_decrypt_letter_index(4, 10) == -6
    assert find_decrypt_letter_index(20, 23) == -3

def test_find_decrypt_letter_index_with_shift_greater_than_26():
    assert find_decrypt_letter_index(13, 30) == 9
    assert find_decrypt_letter_index(12, 41) == -3

