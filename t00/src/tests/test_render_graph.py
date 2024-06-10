import pytest
import json
import os
from pathlib import Path
from render_graph import load_graph, render_to_png, render_to_html

# Создаем фикстуру для тестового графа
@pytest.fixture
def test_graph_data():
    return {
        "nodes": [
            {"id": "Page_A"},
            {"id": "Page_B"},
            {"id": "Page_C"},
            {"id": "Page_D"},
            {"id": "Page_E"}
        ],
        "links": [
            {"source": "Page_A", "target": "Page_B"},
            {"source": "Page_B", "target": "Page_C"},
            {"source": "Page_C", "target": "Page_D"},
            {"source": "Page_D", "target": "Page_E"},
            {"source": "Page_E", "target": "Page_A"}  # Цикл для тестирования
        ]
    }

# Фикстура для временного файла JSON с графом
@pytest.fixture
def test_graph_file(tmp_path, test_graph_data):
    file_path = tmp_path / "test_graph.json"
    with open(file_path, 'w') as f:
        json.dump(test_graph_data, f)
    return str(file_path)

# Тест для функции load_graph
def test_load_graph(test_graph_file):
    graph = load_graph(test_graph_file)
    assert len(graph.nodes) == 5
    assert len(graph.edges) == 5
    assert "Page_A" in graph.nodes
    assert ("Page_A", "Page_B") in graph.edges

# Тест для функции render_to_png
def test_render_to_png(test_graph_file, tmp_path):
    graph = load_graph(test_graph_file)
    output_file = tmp_path / "wiki_graph.png"
    render_to_png(graph, str(output_file))
    assert output_file.exists()
    assert output_file.stat().st_size > 0  # Проверяем, что файл не пустой

# Тест для функции render_to_html
def test_render_to_html(test_graph_file, tmp_path):
    graph = load_graph(test_graph_file)
    output_file = tmp_path / "wiki_graph.html"
    render_to_html(graph, str(output_file))
    assert output_file.exists()
    assert output_file.stat().st_size > 0  # Проверяем, что файл не пустой

# Тест для случая, когда файл не найден
def test_load_graph_file_not_found():
    with pytest.raises(SystemExit):  # Ожидаем завершения работы скрипта с ошибкой
        load_graph("non_existent_file.json")

