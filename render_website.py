import json

from jinja2 import Environment, FileSystemLoader, select_autoescape

BOOKS_FILENAME = 'books.json'
from livereload import Server


def on_reload():
    with open('books.json', 'r', encoding='UTF-8') as file:
        books = json.load(file)
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    print(books[0])
    rendered_page = template.render(
        books=books,

    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


if __name__ == '__main__':
    on_reload()
    server = Server()
    server.watch('template.html', on_reload)
    server.serve(open_url_delay=1)
