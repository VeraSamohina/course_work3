from utils import func


def test_is_account():
    assert func.is_account("Карта 1234123412341234") is False
    assert func.is_account("Счет 12345678123456781234") is True
    assert func.is_account(None) is False


def test_is_card():
    assert func.is_card("Карта 1234123412341234") is True
    assert func.is_card("Счет 12345678123456781234") is False
    assert func.is_card(None) is False


def test_mask_number_card():
    assert func.mask_number_card("Карта 1234123412341234") == "Карта 1234 12** **** 1234"
    assert func.mask_number_card("Visa Gold 8765432187654321") == "Visa Gold 8765 43** **** 4321"


def test_mask_number_account():
    assert func.mask_number_account("Счет 12345678123456781234") == "Счет **1234"


def test_format_date():
    assert func.format_date("2018-06-30T02:08:58.425572") == "30.06.2018"
