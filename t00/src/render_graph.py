import os
import json
import networkx as nx
import matplotlib.pyplot as plt
from bokeh.io import output_file, save
from bokeh.plotting import figure, from_networkx
from bokeh.models import Circle, ColumnDataSource, GraphRenderer
from bokeh.plotting import show


def load_graph(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        # Используем DiGraph для загрузки графа
        return nx.node_link_graph(data, directed=True)
    except FileNotFoundError:
        print('database not found')
        exit()

def render_to_png(graph, filename):
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(graph)
    
    if isinstance(graph, nx.DiGraph):
        in_degree = dict(graph.in_degree())
    else:
        in_degree = dict(graph.degree())
    
    sizes = [in_degree[node] * 100 for node in graph.nodes]
    
    nx.draw_networkx_nodes(graph, pos, node_size=sizes, node_color='blue', alpha=0.7)
    nx.draw_networkx_edges(graph, pos, alpha=0.5)
    nx.draw_networkx_labels(graph, pos, font_size=10)
    
    plt.savefig(filename, format="PNG")
    plt.close()

def render_to_html(graph, filename):
    # Определяем размер полотна
    plot = figure(title="Wiki Graph", x_range=(-1.1, 1.1), y_range=(-1.1, 1.1),
                  tools="", toolbar_location=None)

    pos = nx.spring_layout(graph)

    # Преобразуем граф в объект Bokeh
    graph_renderer = from_networkx(graph, pos, scale=1, center=(0, 0))

    in_degree = dict(graph.in_degree())
    sizes = [in_degree[node] * 0.1 + 0.1 for node in graph.nodes]  # Добавляем смещение для минимального размера

    # Используем ColumnDataSource для задания размеров узлов
    graph_renderer.node_renderer.data_source.data['size'] = sizes
    graph_renderer.node_renderer.glyph = Circle(radius='size', fill_color='blue')

    plot.renderers.append(graph_renderer)
    output_file(filename)
    save(plot)

def main():
    wiki_file = os.getenv('WIKI_FILE')
    if not wiki_file:
        print('WIKI_FILE environment variable not set')
        exit()

    graph = load_graph(wiki_file)
    
    # Визуализация графа как PNG
    render_to_png(graph, "wiki_graph.png")

    # Опциональная интерактивная визуализация как HTML
    render_to_html(graph, "wiki_graph.html")

if __name__ == '__main__':
    main()

