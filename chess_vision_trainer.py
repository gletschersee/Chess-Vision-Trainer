"""
This module tests chess_vision_trainer.py to prevent Errors.
"""


from chess_vision_trainer import *
import pytest


def test_get_to_find():
    """
    Test whether the return of get_to_find is a string.
    As long as get_to_find stays unchanged, there is no need to test more precisely whether the random output is an actual square.
    """
    assert type(get_to_find()) == str


def test_welcome():
    """
    Test whether welcome handles both possible cases correctly.
    """
    assert welcome("guest_session") == "Welcome, stranger! :)"
    assert welcome("great carlini") == "Welcome back, great carlini!"


def test_click_handler():
    """
    Test three cases for click_handler to return the correct click value.
    """
    assert click_handler([440, 40], None, "lives") == "timed"
    assert click_handler([300, 130], "home", None) == "User button"
    assert click_handler([100, 100], None, None) == None


def test_click_square_translator():
    """
    Test whether two out of 64 squares are retrieved correctly from the position of the left click.
    """
    assert click_square_translator(60, 410) == "a5"
    assert click_square_translator(128, 256) == "b8"


def test_square_to_position_translator():
    """
    Test whether two out of 64 squares are translated correctly to their position on the screen.
    """
    assert square_to_position_translator("b3") == (100, 500)
    assert square_to_position_translator("f2") == (300, 550)


def test_validate_guess():
    """
    Test whether guess handling works as expectedly by the usage of different cases.
    """
    assert validate_guess("e2", "e2", None, None) == ("Correct!", True)
    assert validate_guess("e5", "f3", "lives", 2) == ("One life remaining.", True)
    assert validate_guess("c3", "h5", "timed", None) == ("Nope. Tick Tock...", False)


def test_get_feedback():
    """
    Test whether feedback giving works as expectedly by the usage of different cases.
    """
    assert get_feedback("timed", None, None, None) == "Mode changed!"
    assert get_feedback("a4", "Try again!", 0, None) == f"You played a4. Try again! :)"
    assert get_feedback(None, "Try again!", 2, 5) == "We both know, you can do better!"
