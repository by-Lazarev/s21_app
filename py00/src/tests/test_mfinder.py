import pytest
import os
from mfinder import check_m_pattern

# Вспомогательная функция для создания временного файла с тестовыми данными
def create_temp_file(content, filename='temp_m.txt'):
    with open(filename, 'w') as f:
        f.write(content)
    return filename

def test_mfinder_true(monkeypatch, capsys):
    content = """*d&t*
**h**
*l*!*"""
    filename = create_temp_file(content)
    monkeypatch.setattr('sys.argv', ['mfinder.py', filename])
    check_m_pattern(filename)
    captured = capsys.readouterr()
    assert captured.out.strip() == "True"
    os.remove(filename)

def test_mfinder_false(monkeypatch, capsys):
    content = """*****
*****
*****"""
    filename = create_temp_file(content)
    monkeypatch.setattr('sys.argv', ['mfinder.py', filename])
    check_m_pattern(filename)
    captured = capsys.readouterr()
    assert captured.out.strip() == "False"
    os.remove(filename)

def test_mfinder_error_size(monkeypatch, capsys):
    content = """*d&t*
**h**"""
    filename = create_temp_file(content)
    monkeypatch.setattr('sys.argv', ['mfinder.py', filename])
    check_m_pattern(filename)
    captured = capsys.readouterr()
    assert captured.out.strip() == "False"
    os.remove(filename)

def test_mfinder_no_file(monkeypatch, capsys):
    filename = "non_existent_file.txt"
    monkeypatch.setattr('sys.argv', ['mfinder.py', filename])
    check_m_pattern(filename)
    captured = capsys.readouterr()
    assert "Error: File not found" in captured.out.strip()


