import example1


def test_main_good():
    input_value = 42
    expect = "good"
    actual = example1.main(input_value)

    assert actual == expect


def test_main_bad():
    input_value = 43
    expect = "bad"
    actual = example1.main(input_value)

    assert actual == expect
