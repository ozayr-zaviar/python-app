#!/usr/bin/python

import application


def test_min():
    values = (2, 3, 1, 4, 6)

    val = application.min(values)
    assert val == 1
