"""
This Unittest will test the function open_file from books.py
"""
import unittest
from unittest import TestCase
from unittest.mock import patch

from books import open_file


class TestOpenFile(TestCase):
    @patch('books.open', unittest.mock.mock_open(read_data="Author	Title	Publisher	Shelf	Category	Subject\n\
Dupre	Skyscrapers	BD&L	12	Architecture	20th Century\n"), create=True)
    def test_open_file_one_book_file(self):
        expected = ([{'Author': 'Dupre',
                      'Category': 'Architecture',
                      'Publisher': 'BD&L',
                      'Shelf': '12',
                      'Subject': '20th Century',
                      'Title': 'Skyscrapers'}],
                    {'Skyscrapers'},
                    {'12'})
        actual = open_file('books.txt')
        self.assertEqual(actual, expected)

    @patch('books.open', unittest.mock.mock_open(read_data="Author	Title	Publisher	Shelf	Category	Subject\n"
                                                 ), create=True)
    def test_open_file_only_criteria_line(self):
        expected = ([], set(), set())
        actual = open_file('books.txt')
        self.assertEqual(actual, expected)

    @patch('books.open', unittest.mock.mock_open(read_data=""), create=True)
    def test_open_file_empty_file(self):
        expected = ([], set(), set())
        actual = open_file('books.txt')
        self.assertEqual(actual, expected)

    @patch('books.open', unittest.mock.mock_open(read_data="Author	Title	Publisher	Shelf	Category	Subject\n\
Dupre	Skyscrapers	BD&L	12	Architecture	20th Century\n\
Hollingsworth	Architecture of the 20th Century	Exeter	6	Architecture	20th Century\n\
Johnson Burgee	Architecture 1979-1985	Rizzoli	6	Architecture	20th Century\n\
Tzonis	Santiago Calatrava The Complete Works Expanded Edition	Rizzoli	12	Architecture	20th Century\n\
Breeze	L. A. Deco	Rizzoli	16	Architecture	American Architecture\n"), create=True)
    def test_open_file_small_file(self):
        expected = ([{'Author': 'Dupre',
                      'Category': 'Architecture',
                      'Publisher': 'BD&L',
                      'Shelf': '12',
                      'Subject': '20th Century',
                      'Title': 'Skyscrapers'},
                     {'Author': 'Hollingsworth',
                      'Category': 'Architecture',
                      'Publisher': 'Exeter',
                      'Shelf': '6',
                      'Subject': '20th Century',
                      'Title': 'Architecture of the 20th Century'},
                     {'Author': 'Johnson Burgee',
                      'Category': 'Architecture',
                      'Publisher': 'Rizzoli',
                      'Shelf': '6',
                      'Subject': '20th Century',
                      'Title': 'Architecture 1979-1985'},
                     {'Author': 'Tzonis',
                      'Category': 'Architecture',
                      'Publisher': 'Rizzoli',
                      'Shelf': '12',
                      'Subject': '20th Century',
                      'Title': 'Santiago Calatrava The Complete Works Expanded Edition'},
                     {'Author': 'Breeze',
                      'Category': 'Architecture',
                      'Publisher': 'Rizzoli',
                      'Shelf': '16',
                      'Subject': 'American Architecture',
                      'Title': 'L. A. Deco'}],
                    {'Architecture 1979-1985',
                     'Architecture of the 20th Century',
                     'L. A. Deco',
                     'Santiago Calatrava The Complete Works Expanded Edition',
                     'Skyscrapers'},
                    {'16', '12', '6'})
        actual = open_file('books.txt')
        self.assertEqual(actual, expected)
