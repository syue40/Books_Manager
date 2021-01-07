"""
This Unittest will test the function print_book_list for correct formatting
"""
import io
import unittest
from unittest import TestCase
from unittest.mock import patch

from books import print_book_list


class printBookList(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_a_book(self, mock_stdout):
        expected = ("#---------------------------------------#\n"
                    "\tResult: #1\n\n"

                    "\tTitle: Seven Stones A Portrait of Arthur Erickson, Artist\n"
                    "\tAuthor: Iglauer\n"
                    "\tPublisher: University of Washington Press\n"
                    "\tShelf: 9\n"
                    "\tCategory: Architecture\n"
                    "\tSubject: Canadian\n"
                    "#---------------------------------------#\n")

        print_book_list([{'Title': "Seven Stones A Portrait of Arthur Erickson, Artist", 'Author':
            'Iglauer', 'Publisher': 'University of Washington Press',
                          'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}])
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_multiple_books(self, mock_stdout):
        expected = ("#---------------------------------------#\n"
                    "\tResult: #1\n\n"

                    "\tTitle: Elementary Linear Algebra 3e\n"
                    "\tAuthor: Anton\n"
                    "\tPublisher: Wiley\n"
                    "\tShelf: 27\n"
                    "\tCategory: Mathematics\n"
                    "\tSubject: Algebra\n"
                    "#---------------------------------------#\n"
                    "#---------------------------------------#\n"
                    "\tResult: #2\n\n"

                    "\tTitle: Elementary Linear Algebra 3e\n"
                    "\tAuthor: Shields\n"
                    "\tPublisher: Worth\n"
                    "\tShelf: 27\n"
                    "\tCategory: Mathematics\n"
                    "\tSubject: Algebra\n"
                    "#---------------------------------------#\n"
                    "#---------------------------------------#\n"
                    "\tResult: #3\n\n"

                    "\tTitle: Seven Stones A Portrait of Arthur Erickson, Artist\n"
                    "\tAuthor: Iglauer\n"
                    "\tPublisher: University of Washington Press\n"
                    "\tShelf: 9\n"
                    "\tCategory: Architecture\n"
                    "\tSubject: Canadian\n"
                    "#---------------------------------------#\n")
        print_book_list([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                                   'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                                   'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                           'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',
                                                           'Category': 'Mathematics', 'Subject': 'Algebra'},
                                  {'Title': "Seven Stones A Portrait of Arthur Erickson, Artist", 'Author':
                                      'Iglauer', 'Publisher': 'University of Washington Press',
                                   'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}])
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_some_empty_parameters(self, mock_stdout):
        expected = ("#---------------------------------------#\n"
                    "\tResult: #1\n\n"

                    "\tTitle: Necronomicon\n"
                    "\tAuthor: Old Gods\n"
                    "\tPublisher: \n"
                    "\tShelf: 9\n"
                    "\tCategory: Forbidden\n"
                    "\tSubject: \n"
                    "#---------------------------------------#\n")
        print_book_list([{'Title': 'Necronomicon', 'Author': 'Old Gods', 'Publisher': '',
                                   'Shelf': '9', 'Category': 'Forbidden', 'Subject': ''}])
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_all_empty_parameters(self, mock_stdout):
        expected = ("#---------------------------------------#\n"
                    "\tResult: #1\n\n"

                    "\tTitle: \n"
                    "\tAuthor: \n"
                    "\tPublisher: \n"
                    "\tShelf: \n"
                    "\tCategory: \n"
                    "\tSubject: \n"
                    "#---------------------------------------#\n")
        print_book_list([{'Title': '', 'Author': '', 'Publisher': '',
                                   'Shelf': '', 'Category': '', 'Subject': ''}])
        self.assertEqual(mock_stdout.getvalue(), expected)
