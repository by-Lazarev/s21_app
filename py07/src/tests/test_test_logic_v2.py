# tests/test_test_logic_v2.py

import pytest
from test_logic_v2 import analyze_responses

def test_analyze_responses_human():
    responses = [
        {'respiration': 12, 'heart_rate': 70, 'blushing_level': 1, 'pupillary_dilation': 2},
        {'respiration': 15, 'heart_rate': 80, 'blushing_level': 2, 'pupillary_dilation': 3},
        {'respiration': 10, 'heart_rate': 60, 'blushing_level': 1, 'pupillary_dilation': 2},
        {'respiration': 14, 'heart_rate': 75, 'blushing_level': 3, 'pupillary_dilation': 4},
        {'respiration': 13, 'heart_rate': 65, 'blushing_level': 2, 'pupillary_dilation': 3},
        {'respiration': 12, 'heart_rate': 68, 'blushing_level': 2, 'pupillary_dilation': 3},
        {'respiration': 15, 'heart_rate': 72, 'blushing_level': 1, 'pupillary_dilation': 2},
        {'respiration': 14, 'heart_rate': 76, 'blushing_level': 2, 'pupillary_dilation': 4},
        {'respiration': 13, 'heart_rate': 67, 'blushing_level': 3, 'pupillary_dilation': 3},
        {'respiration': 11, 'heart_rate': 64, 'blushing_level': 1, 'pupillary_dilation': 2}
    ]
    # В этом тесте мы ожидаем, что значения соответствуют "Replicant"
    assert analyze_responses(responses) == "Replicant"

def test_analyze_responses_replicant():
    responses = [
        {'respiration': 30, 'heart_rate': 150, 'blushing_level': 5, 'pupillary_dilation': 8},
        {'respiration': 35, 'heart_rate': 160, 'blushing_level': 6, 'pupillary_dilation': 7},
        {'respiration': 32, 'heart_rate': 155, 'blushing_level': 5, 'pupillary_dilation': 8},
        {'respiration': 33, 'heart_rate': 140, 'blushing_level': 6, 'pupillary_dilation': 7},
        {'respiration': 31, 'heart_rate': 145, 'blushing_level': 5, 'pupillary_dilation': 8},
        {'respiration': 30, 'heart_rate': 150, 'blushing_level': 6, 'pupillary_dilation': 7},
        {'respiration': 32, 'heart_rate': 155, 'blushing_level': 5, 'pupillary_dilation': 8},
        {'respiration': 34, 'heart_rate': 160, 'blushing_level': 6, 'pupillary_dilation': 7},
        {'respiration': 33, 'heart_rate': 140, 'blushing_level': 5, 'pupillary_dilation': 8},
        {'respiration': 31, 'heart_rate': 145, 'blushing_level': 6, 'pupillary_dilation': 7}
    ]
    # В этом тесте мы ожидаем, что значения соответствуют "Replicant"
    assert analyze_responses(responses) == "Replicant"

def test_analyze_responses_edge_case_human():
    # Граничный случай для "Human", когда значение близко к пороговому
    responses = [
        {'respiration': 10, 'heart_rate': 10, 'blushing_level': 1, 'pupillary_dilation': 1},
        {'respiration': 10, 'heart_rate': 10, 'blushing_level': 1, 'pupillary_dilation': 1},
        {'respiration': 10, 'heart_rate': 10, 'blushing_level': 1, 'pupillary_dilation': 1},
        {'respiration': 10, 'heart_rate': 10, 'blushing_level': 1, 'pupillary_dilation': 1},
        {'respiration': 10, 'heart_rate': 10, 'blushing_level': 1, 'pupillary_dilation': 1},
        {'respiration': 10, 'heart_rate': 10, 'blushing_level': 1, 'pupillary_dilation': 1},
        {'respiration': 10, 'heart_rate': 10, 'blushing_level': 1, 'pupillary_dilation': 1},
        {'respiration': 10, 'heart_rate': 10, 'blushing_level': 1, 'pupillary_dilation': 1},
        {'respiration': 10, 'heart_rate': 10, 'blushing_level': 1, 'pupillary_dilation': 1},
        {'respiration': 10, 'heart_rate': 10, 'blushing_level': 1, 'pupillary_dilation': 1}
    ]
    assert analyze_responses(responses) == "Human"

def test_analyze_responses_edge_case_replicant():
    # Граничный случай для "Replicant", когда значение чуть превышает пороговое
    responses = [
        {'respiration': 50, 'heart_rate': 50, 'blushing_level': 5, 'pupillary_dilation': 5},
        {'respiration': 50, 'heart_rate': 50, 'blushing_level': 5, 'pupillary_dilation': 5},
        {'respiration': 50, 'heart_rate': 50, 'blushing_level': 5, 'pupillary_dilation': 5},
        {'respiration': 50, 'heart_rate': 50, 'blushing_level': 5, 'pupillary_dilation': 5},
        {'respiration': 50, 'heart_rate': 50, 'blushing_level': 5, 'pupillary_dilation': 5},
        {'respiration': 50, 'heart_rate': 50, 'blushing_level': 5, 'pupillary_dilation': 5},
        {'respiration': 50, 'heart_rate': 50, 'blushing_level': 5, 'pupillary_dilation': 5},
        {'respiration': 50, 'heart_rate': 50, 'blushing_level': 5, 'pupillary_dilation': 5},
        {'respiration': 50, 'heart_rate': 50, 'blushing_level': 5, 'pupillary_dilation': 5},
        {'respiration': 50, 'heart_rate': 50, 'blushing_level': 5, 'pupillary_dilation': 5}
    ]
    assert analyze_responses(responses) == "Replicant"

