"""
This Unittest will test the function move_books from books.py
"""
from unittest import TestCase
from unittest.mock import patch
from books import move_books
import io


class TestMoveBooks(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['Skyscrapers', '9'])
    def test_move_book(self, mock_input, mock_output):
        expected = None
        expected_2 = ("\nYour book is currently in shelf 12!\n\nBook successfully"
                      " moved! Returning to menu...\n")
        actual = move_books([{'Title': 'Skyscrapers', 'Author': 'Dupre', 'Publisher': 'DB&L', 'Shelf': '12',
                              'Category': 'Architecture', 'Subject': '20th Century'},
                             {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                 'Iglauer', 'Publisher': 'University of Washington Press',
                              'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}],
                            {'Skyscrapers', 'Seven Stones A Portrait of Arthur Erickson, Architect'},
                            {'12', '9'})
        self.assertEqual(expected, actual)
        self.assertEqual(mock_output.getvalue(), expected_2)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['hello'])
    def test_move_book_invalid_book(self, mock_input, mock_output):
        expected = None
        expected_2 = "That book title isn't in the library! Returning to menu...\n"
        actual = move_books([{'Title': 'Skyscrapers', 'Author': 'Dupre', 'Publisher': 'DB&L', 'Shelf': '12',
                              'Category': 'Architecture', 'Subject': '20th Century'},
                             {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                 'Iglauer', 'Publisher': 'University of Washington Press',
                              'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}],
                            {'Skyscrapers', 'Seven Stones A Portrait of Arthur Erickson, Architect'},
                            {'12', '9'})
        self.assertEqual(expected, actual)
        self.assertEqual(mock_output.getvalue(), expected_2)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['Skyscrapers', '123'])
    def test_move_book_invalid_shelf(self, mock_input, mock_output):
        expected = None
        expected_2 = ("\nYour book is currently in shelf 12!\n\nThat shelf isn't in "
                      "the library! Returning to menu...\n")
        actual = move_books([{'Title': 'Skyscrapers', 'Author': 'Dupre', 'Publisher': 'DB&L', 'Shelf': '12',
                              'Category': 'Architecture', 'Subject': '20th Century'},
                             {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                 'Iglauer', 'Publisher': 'University of Washington Press',
                              'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}],
                            {'Skyscrapers', 'Seven Stones A Portrait of Arthur Erickson, Architect'},
                            {'12', '9'})
        self.assertEqual(expected, actual)
        self.assertEqual(mock_output.getvalue(), expected_2)
