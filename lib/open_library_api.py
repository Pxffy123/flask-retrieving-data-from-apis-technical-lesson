import json
import requests

class Search:
    def Get_books(self, search_term):
        search_term_format = search_term.replace(" ", "+")
        URL = f'https://openlibrary.org/search.json?title={search_term_format}'
        response = requests.get(URL).json()
        response_formatted = f'Title: {response['docs'][0]['title']}'


book = input('Look for a book: ')
result = Search().Get_books(book)

print(result)