import pytest
import subprocess
import json
import os
import sys

# Создаем фикстуру для тестового графа
@pytest.fixture
def test_graph_file(tmp_path):
    graph = {
        "Page_A": ["Page_B"],
        "Page_B": ["Page_C"],
        "Page_C": ["Page_D"],
        "Page_D": ["Page_E"],
        "Page_E": []
    }
    file_path = tmp_path / "test_graph.json"
    with open(file_path, 'w') as f:
        json.dump(graph, f)
    return str(file_path)

# Вспомогательная функция для запуска скрипта
def run_script(args, env):
    # Используем путь к текущему интерпретатору Python
    python_executable = sys.executable
    result = subprocess.run(
        [python_executable, "shortest_path.py"] + args,
        capture_output=True,
        text=True,
        env=env
    )
    return result

# Тест для случая, когда путь существует
def test_path_exists(test_graph_file):
    env = {"WIKI_FILE": test_graph_file}
    result = run_script(["--from-page", "Page_A", "--to-page", "Page_D"], env)
    assert result.returncode == 0
    assert result.stdout.strip() == "3"

# Тест для случая, когда путь не найден
def test_path_not_found(test_graph_file):
    env = {"WIKI_FILE": test_graph_file}
    result = run_script(["--from-page", "Page_A", "--to-page", "Page_Z"], env)
    assert result.returncode == 0
    assert "path not found" in result.stdout.strip()

# Тест для ненаправленного графа
def test_non_directed_path(test_graph_file):
    env = {"WIKI_FILE": test_graph_file}
    result = run_script(["--from-page", "Page_D", "--to-page", "Page_A", "--non-directed"], env)
    assert result.returncode == 0
    assert result.stdout.strip() == "3"

# Тест для логирования пути
def test_verbose_path(test_graph_file):
    env = {"WIKI_FILE": test_graph_file}
    result = run_script(["--from-page", "Page_A", "--to-page", "Page_D", "-v"], env)
    assert result.returncode == 0
    expected_path = "Page_A -> Page_B -> Page_C -> Page_D"
    assert expected_path in result.stdout.strip()
    assert result.stdout.strip().endswith("3")

# Тест для случая, когда файл не найден
def test_database_not_found():
    env = {"WIKI_FILE": "non_existent_file.json"}
    result = run_script(["--from-page", "Page_A", "--to-page", "Page_D"], env)
    assert result.returncode == 0
    assert "database not found" in result.stdout.strip()

# Тест для случая, когда переменная WIKI_FILE не установлена
def test_no_wiki_file_env():
    result = run_script(["--from-page", "Page_A", "--to-page", "Page_D"], env={})
    assert result.returncode == 0
    assert "WIKI_FILE environment variable not set" in result.stdout.strip()

