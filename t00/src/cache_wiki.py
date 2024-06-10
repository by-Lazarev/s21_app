import argparse
import logging
import requests
from bs4 import BeautifulSoup
import networkx as nx
import json
import urllib.parse

# Настройка логирования
logging.basicConfig(level=logging.INFO)

def download_page(url):
    response = requests.get(url)
    response.raise_for_status()  # Поднять ошибку, если запрос не удался
    return response.content

def extract_wiki_links(content):
    soup = BeautifulSoup(content, 'html.parser')
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('/wiki/') and ':' not in href:
            links.append('https://en.wikipedia.org' + href)
    return links

def build_graph(start_page, depth):
    graph = nx.DiGraph()
    visited = set()

    def crawl(page_url, current_depth):
        if page_url in visited or current_depth > depth:
            return
        visited.add(page_url)
        logging.info(f'Visiting: {page_url}')
        content = download_page(page_url)
        links = extract_wiki_links(content)
        for link in links:
            graph.add_edge(page_url, link)
            crawl(link, current_depth + 1)

    crawl(start_page, 0)
    return graph

def save_graph_to_json(graph, filename):
    data = nx.readwrite.json_graph.node_link_data(graph)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def main():
    parser = argparse.ArgumentParser(description="Download Wikipedia pages and save a graph representation.")
    parser.add_argument('-p', '--page', type=str, default='Web', help='The starting Wikipedia page')
    parser.add_argument('-d', '--depth', type=int, default=3, help='The depth to follow links')
    args = parser.parse_args()

    # Формирование URL страницы
    start_page_title = args.page
    encoded_title = urllib.parse.quote(start_page_title.replace(' ', '_'))
    start_page_url = f'https://en.wikipedia.org/wiki/{encoded_title}'
    
    logging.info(f'Starting URL: {start_page_url}')
    
    depth = args.depth

    graph = build_graph(start_page_url, depth)

    if len(graph) > 1000:
        logging.warning('Graph is too large, stopping.')
    elif len(graph) < 20:
        logging.warning('Graph is too small, consider choosing another start page.')

    save_graph_to_json(graph, 'wiki.json')

if __name__ == '__main__':
    main()

