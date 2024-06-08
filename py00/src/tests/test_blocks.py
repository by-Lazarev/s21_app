import pytest
import io
import sys
from blocks import process_lines

def test_process_lines(monkeypatch):
    test_input = """00000254b208c0f43409d8dc00439896
abcdef1234567890abcdef1234567890
00000123abcd5678efghijklmnopqrst
0000085a34260d1c84e89865c210ceb4
111110000254b208c0f43409d8dc0043
0000071f49cffeaea4184be3d507086v
000000c94dcb1df204fa4c007c4b4b12
1234567890abcdef1234567890abcdef
00000123abcd5678efghijklmnopqrst
00000254b208c0f43409d8dc00439896"""
    
    expected_output = """00000254b208c0f43409d8dc00439896
00000123abcd5678efghijklmnopqrst
0000085a34260d1c84e89865c210ceb4
0000071f49cffeaea4184be3d507086v
000000c94dcb1df204fa4c007c4b4b12
00000123abcd5678efghijklmnopqrst
00000254b208c0f43409d8dc00439896"""
    
    # Используем monkeypatch для замены sys.stdin на StringIO с нашим тестовым вводом
    monkeypatch.setattr('sys.stdin', io.StringIO(test_input))
    
    output = io.StringIO()
    sys.stdout = output
    
    process_lines(10)
    
    # Получаем строки вывода и сравниваем с ожидаемым результатом
    result = output.getvalue().strip()
    assert result == expected_output

    # Восстанавливаем sys.stdout
    sys.stdout = sys.__stdout__


