"""
This Unittest will test the function menu from books.py
"""
from unittest import TestCase
from unittest.mock import patch

from books import menu


class TestMenu(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_using_menu(self, mock_input):
        expected = 1
        actual = menu()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['8'])
    def test_using_menu_greatest_value(self, mock_input):
        expected = 8
        actual = menu()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2'])
    def test_using_next_value(self, mock_input):
        expected = 2
        actual = menu()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['12', '3'])
    def test_using_invalid_valid(self, mock_input):
        expected = 3
        actual = menu()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['hi', '10', '1'])
    def test_using_invalid_invalid_then_valid(self, mock_input):
        expected = 1
        actual = menu()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['6', 'hi', '2'])
    def test_using_valid_invalid_valid(self, mock_input):
        expected = 6
        actual = menu()
        self.assertEqual(actual, expected)




