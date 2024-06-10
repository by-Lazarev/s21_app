import argparse
import json
import os
import logging
from collections import deque

def load_graph(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print('database not found')
        exit()

def bfs_shortest_path(graph, start, goal, directed=True):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current_node, path = queue.popleft()
        if current_node == goal:
            return path
        if current_node not in visited:
            visited.add(current_node)
            neighbors = graph.get(current_node, [])
            if not directed:
                # Добавляем обратные ребра для ненаправленного графа
                for node in graph:
                    if current_node in graph[node] and node not in neighbors:
                        neighbors.append(node)
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None

def main():
    parser = argparse.ArgumentParser(description="Find the shortest path between two Wikipedia pages in a graph.")
    parser.add_argument('--from-page', type=str, required=True, help='The starting Wikipedia page')
    parser.add_argument('--to-page', type=str, required=True, help='The target Wikipedia page')
    parser.add_argument('--non-directed', action='store_true', help='Treat the graph as non-directed')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    args = parser.parse_args()

    start_page = args.from_page
    target_page = args.to_page
    directed = not args.non_directed
    verbose = args.verbose

    wiki_file = os.getenv('WIKI_FILE')
    if not wiki_file:
        print('WIKI_FILE environment variable not set')
        exit()

    graph = load_graph(wiki_file)
    
    if start_page not in graph or target_page not in graph:
        print('path not found')
        exit()

    path = bfs_shortest_path(graph, start_page, target_page, directed)

    if path:
        if verbose:
            print(' -> '.join(path))
        print(len(path) - 1)
    else:
        print('path not found')

if __name__ == '__main__':
    main()

