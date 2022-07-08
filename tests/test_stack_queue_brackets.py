import pytest
from stack_and_queue.stack_queue_brackets import *




def test_bracket():
    actual=validate_brackets("{}(){}")
    expected=True
    assert actual==expected



def test_bracket1():
    actual=validate_brackets("{}({}")
    expected=False
    assert actual==expected


def test_bracket2():
    actual=validate_brackets("")
    expected=True
    assert actual==expected


def test_bracket3():
    actual=validate_brackets("{}{Code}[Fellows](())")
    expected=True
    assert actual==expected

def test_bracket4():
    actual=validate_brackets("()[[Extra Characters]]")
    expected=True
    assert actual==expected

def test_bracket5():
    actual=validate_brackets("[({}]")
    expected=False
    assert actual==expected