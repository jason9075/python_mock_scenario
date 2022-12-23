import example2
from unittest.mock import Mock


def test_main_good():
    dummy = 42
    mock = Mock(spec=example2.Handler)
    mock.run_very_long_func.return_value = 1
    expect = "good"
    actual = example2.main(mock, dummy)
    assert actual == expect


def test_main_bad():
    dummy = 43
    mock = Mock(spec=example2.Handler)
    mock.run_very_long_func.return_value = 123
    expect = "bad"
    actual = example2.main(mock, dummy)

    assert actual == expect
