"""
This Unittest will test the function get_single_book_to_move from books.py
"""
from unittest import TestCase
from unittest.mock import patch
from books import get_single_book_to_move


class TestGetSingleBook(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_getting_book_match(self, mock_input):
        expected = [{'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                     'Iglauer', 'Publisher': 'University of Washington Press',
                     'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}]

        actual = get_single_book_to_move([{'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                           'Iglauer', 'Publisher': 'University of Washington Press',
                                           'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'},
                                          {'Title': "Seven Stones A Portrait of Arthur Erickson, Artist", 'Author':
                                           'Iglauer', 'Publisher': 'University of Washington Press',
                                           'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}])
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_other_duplicate_book_second_copy(self, mock_input):
        expected = [{'Title': 'Elementary Linear Algebra 3e',
                     'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',
                     'Category': 'Mathematics', 'Subject': 'Algebra'}]
        actual = get_single_book_to_move([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                                           'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                                           'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                                   'Author': 'Shields', 'Publisher': 'Worth',
                                                                   'Shelf': '27',
                                                                   'Category': 'Mathematics', 'Subject': 'Algebra'}])
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1'])
    def test_other_duplicate_book_first_copy(self, mock_input):
        expected = [{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                     'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                     'Subject': 'Algebra'}]
        actual = get_single_book_to_move([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                                           'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                                           'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                                   'Author': 'Shields', 'Publisher': 'Worth',
                                                                   'Shelf': '27',
                                                                   'Category': 'Mathematics', 'Subject': 'Algebra'}])
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['hi', '1'])
    def test_getting_invalid_valid_value(self, mock_input):
        expected = [{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                     'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                     'Subject': 'Algebra'}]
        actual = get_single_book_to_move([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                                           'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                                           'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                                   'Author': 'Shields', 'Publisher': 'Worth',
                                                                   'Shelf': '27',
                                                                   'Category': 'Mathematics', 'Subject': 'Algebra'}])
        self.assertEqual(expected, actual)
