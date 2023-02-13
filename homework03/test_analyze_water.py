# Daniela Sanchez, dls4848

import pytest

from water_quality import calculate_turbidity, calculate_min_time

def test_caculate_turbidity():
    #testing with a sample from data
    a0 = 0.23
    I90 = [0.22, 0.23, 0.24, 0.25, 0.26]
    result = calculate_turbidity(a0, I90)
    expected = 0.239
    assert result == expected, f"Expected {expected} but got {result}"

    #testing with different values from data
    a0 = 0.35
    I90 = [0.32, 0.34, 0.36, 0.38, 0.40]
    result = calculate_turbidity(a0, I90)
    expected = 0.368
    assert result == expected, f"Expeceted {expected} but got {result}"



def test_calculate_min_time():
    #testing with a sample from data
    Ts = 1.0
    T = 1.5
    d = 0.02
    result = calculate_min_time(Ts, T, d)
    expected = 6.67
    assert result == expected, f"Expected {expected} but got {result}"

    #testing with different sample from data
    Ts = 1.0
    T = 2.0
    d = 0.01
    result = calculate_min_time(Ts, T, d)
    expected = 11.77
    assert result == expected, f"Expected {expected} but got {result}"









