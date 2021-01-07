"""
This function tests the quit_books function in books.py.
"""
from unittest import TestCase
from unittest.mock import patch
from books import quit_books
import io


class TestQuitBooks(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_quit_books(self, mock_output):
        filename = 'test_quit_books_dummy.txt'
        expected = None
        expected_2 = 'Saved!\n'
        actual = quit_books([{'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                            'Iglauer', 'Publisher': 'University of Washington Press',
                              'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'},
                             {'Title': "Skyscrapers", 'Author':
                                 'Dupre', 'Publisher': 'DB&L',
                              'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                             {'Title': '1984', 'Author': 'George Orwell', 'Publisher': 'Penguin Classics',
                              'Shelf': '', 'Category': 'Architecture', 'Subject': '20th Century'},
                             {'Title': 'Animal Farm', 'Author': 'George Orwell', 'Publisher': 'Penguin Classics',
                              'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'}], filename)
        self.assertEqual(actual, expected)
        self.assertEqual(mock_output.getvalue(), expected_2)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_quit_books_with_empty_values(self, mock_output):
        filename = 'test_quit_books_dummy.txt'
        expected = None
        expected_2 = 'Saved!\n'
        actual = quit_books([{'Title': '', 'Author': '', 'Publisher': '',
                              'Shelf': '', 'Category': '', 'Subject': ''},
                             {'Title': "Skyscrapers", 'Author': 'Dupre', 'Publisher': 'DB&L',
                              'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                             {'Title': '1984', 'Author': 'George Orwell', 'Publisher': 'Penguin Classics',
                              'Shelf': '', 'Category': 'Architecture', 'Subject': '20th Century'},
                             {'Title': 'Animal Farm', 'Author': 'George Orwell', 'Publisher': 'Penguin Classics',
                              'Shelf': '', 'Category': '', 'Subject': ''}], filename)
        self.assertEqual(actual, expected)
        self.assertEqual(mock_output.getvalue(), expected_2)
