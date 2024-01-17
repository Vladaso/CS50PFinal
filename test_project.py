import pytest
from Quizzer import Quizzer
from project import evaluate,get_cat,load_user
def test_get_cat():
    assert get_cat(0) ==  ["American Shorthair", "Even tempered and quiet."]
    with pytest.raises(KeyError):
        get_cat(31)


def test_Quizzer():
    q = Quizzer()
    assert len(q.questions) == 10
    assert q.questions[0].text is not None
    with pytest.raises(IndexError):
        q.questions[10]


def test_evaluate():
    assert evaluate({'q1': '1', 'q2': '1', 'q3': '1', 'q4': '1', 'q5': '1', 'q6': '1', 'q7': '1', 'q8': '1', 'q9': '1', 'q10': '1'}) == 10
    with pytest.raises(ValueError):
        evaluate({'q1': '1', 'q2': '1', 'q3': '1', 'q4': '1', 'q5': '1', 'q6': '1', 'q7': '1', 'q8': '1', 'q9': '1', 'q10': '100'})


def test_load_user():
    # If user with name 'This is a test 457645' exists in users.json, this test will fail. - Dont know how to fix this
    assert(load_user('This is a test 457645') is None)