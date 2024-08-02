import sys
import string
import pytest
import mock
import builtins

sys.path.append("../src")

from src.pkg.caeser_cipher import *


@pytest.fixture
def get_alphabet():
    return list(string.ascii_lowercase)


@pytest.fixture
def get_plain_text():
    return "Hello, this is testing 123 and #@"


@pytest.fixture
def get_cipher_text():
    return "lipps, xlmw mw xiwxmrk 123 erh #@"


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


def test_caeser_encoding(get_alphabet, get_plain_text, get_cipher_text):
    alphabet = get_alphabet
    operation = "encode"
    plain_text = get_plain_text
    shift_amount = 56
    actual_cipher_text = caeser(operation, plain_text, alphabet, shift_amount)
    expected_cipher = get_cipher_text
    assert actual_cipher_text == expected_cipher


def test_caeser_decoding(get_alphabet, get_plain_text, get_cipher_text):
    alphabet = get_alphabet
    operation = "decode"
    shift_amount = 56
    cipher_text = get_cipher_text
    actual_plain_text = caeser(operation, cipher_text, alphabet, shift_amount)
    expected_plain_text = get_plain_text.lower()
    assert actual_plain_text == expected_plain_text


def test_main_encode(capsys, get_plain_text, get_cipher_text):
    inputs = ["encode", get_plain_text, "56", "no"]
    with mock.patch.object(builtins, "input", lambda _: inputs.pop(0)):
        main()
        captured = capsys.readouterr()
        assert captured.out == f"{get_cipher_text}\nGood Bye!\n"


def test_main_encode_and_decode(capsys, get_plain_text, get_cipher_text):
    inputs = [
        "encode",
        get_plain_text,
        "56",
        "yes",
        "decode",
        get_cipher_text,
        "56",
        "no",
    ]
    with mock.patch.object(builtins, "input", lambda _: inputs.pop(0)):
        main()
        captured = capsys.readouterr()
        expected = f"{get_cipher_text}\n{get_plain_text.lower()}\nGood Bye!\n"
        assert captured.out == expected
