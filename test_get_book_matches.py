"""
This Unittest will test the function get_book_matches from books.py
"""
from unittest import TestCase
from books import get_book_matches


class TestGetBookMatches(TestCase):
    def test_get_book_matches_single_case_title(self):
        expected = 'Book1'
        actual = get_book_matches([{'Title': 'Book1', 'Publisher': 'Pub1'}], 1, 'Book1')[0]['Title']
        self.assertEqual(expected, actual)

    def test_get_book_from_small_library_title(self):
        expected = 'Brave New World'
        actual = get_book_matches([{'Title': '1984', 'Author': 'George Orwell', 'Publisher': 'Penguin Classics'},
                                   {'Title': 'Animal Farm', 'Author': 'George Orwell',
                                    'Publisher': 'Penguin Classics'},
                                   {'Title': 'Brave New World', 'Author': 'Aldous Huxley',
                                    'Publisher': 'Penguin Classics'}], 3, 'Penguin Classics')[2]['Title']
        self.assertEqual(expected, actual)

    def test_get_books_from_library_same_publisher(self):
        expected = [{'Title': '1984', 'Author': 'George Orwell', 'Publisher': 'Penguin Classics'},
                    {'Title': 'Animal Farm', 'Author': 'George Orwell',
                     'Publisher': 'Penguin Classics'},
                    {'Title': 'Brave New World', 'Author': 'Aldous Huxley',
                     'Publisher': 'Penguin Classics'}]
        actual = get_book_matches([{'Title': '1984', 'Author': 'George Orwell', 'Publisher': 'Penguin Classics'},
                                   {'Title': 'Animal Farm', 'Author': 'George Orwell',
                                    'Publisher': 'Penguin Classics'},
                                   {'Title': 'Brave New World', 'Author': 'Aldous Huxley',
                                    'Publisher': 'Penguin Classics'}], 3, 'Penguin Classics')
        self.assertEqual(expected, actual)

    def test_get_books_from_library_same_author(self):
        expected = [{'Title': '1984', 'Author': 'George Orwell', 'Publisher': 'Penguin Classics'},
                    {'Title': 'Animal Farm', 'Author': 'George Orwell',
                     'Publisher': 'Penguin Classics'}]
        actual = get_book_matches([{'Title': '1984', 'Author': 'George Orwell', 'Publisher': 'Penguin Classics'},
                                   {'Title': 'Animal Farm', 'Author': 'George Orwell',
                                    'Publisher': 'Penguin Classics'},
                                   {'Title': 'Brave New World', 'Author': 'Aldous Huxley',
                                    'Publisher': 'Penguin Classics'}], 2, 'Orwell')
        self.assertEqual(expected, actual)

    def test_get_single_book_by_partial_author(self):
        expected = [{'Title': 'Animal Farm', 'Author': 'George Orwell', 'Publisher': 'Penguin Classics'}]
        actual = get_book_matches([{'Title': '1984', 'Author': 'George Orwell', 'Publisher': 'Penguin Classics'},
                                   {'Title': 'Animal Farm', 'Author': 'George Orwell',
                                    'Publisher': 'Penguin Classics'},
                                   {'Title': 'Brave New World', 'Author': 'Aldous Huxley',
                                    'Publisher': 'Penguin Classics'}], 1, 'Animal')
        self.assertEqual(expected, actual)

    def test_search_title_no_results_found(self):
        expected = []
        actual = get_book_matches([{'Title': '1984', 'Author': 'George Orwell', 'Publisher': 'Penguin Classics'},
                                   {'Title': 'Animal Farm', 'Author': 'George Orwell',
                                    'Publisher': 'Penguin Classics'},
                                   {'Title': 'Brave New World', 'Author': 'Aldous Huxley',
                                    'Publisher': 'Penguin Classics'}], 1, 'zxy')
        self.assertEqual(expected, actual)

    def test_get_books_by_shelf(self):
        expected = [{'Title': '1984', 'Author': 'George Orwell', 'Publisher': 'Penguin Classics', 'Shelf': '6'},
                    {'Title': 'Animal Farm', 'Author': 'George Orwell',
                     'Publisher': 'Penguin Classics', 'Shelf': '6'}]
        actual = get_book_matches([{'Title': '1984', 'Author': 'George Orwell', 'Publisher': 'Penguin Classics',
                                    'Shelf': '6'},
                                   {'Title': 'Animal Farm', 'Author': 'George Orwell',
                                    'Publisher': 'Penguin Classics', 'Shelf': '6'},
                                   {'Title': 'Brave New World', 'Author': 'Aldous Huxley',
                                    'Publisher': 'Penguin Classics', 'Shelf': '10'}], 4, '6')
        self.assertEqual(expected, actual)
