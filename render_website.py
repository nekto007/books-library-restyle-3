import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
BOOKS_FILENAME = 'books.json'


def fetch_books_from_json(filename) -> list[dict]:
    with open(filename, 'r', encoding='utf-8') as file:
        books = json.loads(file.read())

    for book in books:
        book['image_src'] = book['image_src'].replace('\\', '/')
        book['book_path'] = book['book_path'].replace('\\', '/')

    return books


def main():
    # books = fetch_books_from_json(BOOKS_FILENAME)
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
    main()
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
