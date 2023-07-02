import json
import os
from math import ceil
from more_itertools import ichunked
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server

BOOKS_FILENAME = 'books.json'


def on_reload():
    os.makedirs('pages', exist_ok=True)
    books_on_page = 10
    with open('books.json', 'r', encoding='UTF-8') as file:
        books = json.load(file)
    for page, block_books in enumerate(ichunked(books, books_on_page), start=1):
        env = Environment(
            loader=FileSystemLoader('.'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        template = env.get_template('template.html')
        print(books[0])
        rendered_page = template.render(
            books=block_books,
            page=page,
            max_pages=ceil(len(books) / books_on_page),
        )
        path_page = os.path.join('pages', f'index{str(page)}.html')
        with open(path_page, 'w', encoding="utf8") as file:
            file.write(rendered_page)


if __name__ == '__main__':
    on_reload()
    server = Server()
    server.watch('template.html', on_reload)
    server.serve(open_url_delay=1)
