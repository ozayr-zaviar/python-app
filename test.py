#!/usr/bin/python

import application


def test_min():
    values = (2, 3, 1, 4, 6)

    val = application.min(values)
    assert val == 1


def test_max():
    values = (2, 3, 1, 4, 6)

    val = application.max(values)
    assert val == 6


def test_max_2():
    values = (2, 3, 1, 4, 6, 7)

    val = application.max(values)
    assert val == 7



