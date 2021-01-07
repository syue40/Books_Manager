"""
This Unittest will test the function search_the_library from books.py
"""
import io
import unittest
from unittest import TestCase
from unittest.mock import patch

from books import search_the_library


class TestSearchTheLibrary(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_one_valid_book(self, mock_stdout):
        expected = ("\nYou have 1 item(s) that match your search criteria:\n\n"
                    "#---------------------------------------#\n"
                    "\tResult: #1\n\n"

                    "\tTitle: Seven Stones A Portrait of Arthur Erickson, Architect\n"
                    "\tAuthor: Iglauer\n"
                    "\tPublisher: University of Washington Press\n"
                    "\tShelf: 9\n"
                    "\tCategory: Architecture\n"
                    "\tSubject: Canadian\n"
                    "#---------------------------------------#\n"
                    "\nSearch Completed. Returning to menu...\n\n")

        search_the_library([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                             'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                             'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                     'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',
                                                     'Category': 'Mathematics', 'Subject': 'Algebra'},
                            {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                'Iglauer', 'Publisher': 'University of Washington Press',
                             'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}], 4, '9')
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_two_valid_books(self, mock_stdout):
        expected = ("\nYou have 2 item(s) that match your search criteria:\n\n"
                    "#---------------------------------------#\n"
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
                    "\nSearch Completed. Returning to menu...\n\n"
                    )

        search_the_library([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                             'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                             'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                     'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',
                                                     'Category': 'Mathematics', 'Subject': 'Algebra'},
                            {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                'Iglauer', 'Publisher': 'University of Washington Press',
                             'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}], 4, '27')
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_no_valid_books(self, mock_stdout):
        expected = ("\nYou have 0 item(s) that match your search criteria:\n\n"
                    "\nSearch Completed. Returning to menu...\n\n")
        search_the_library([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                             'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                             'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                     'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',
                                                     'Category': 'Mathematics', 'Subject': 'Algebra'},
                            {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                'Iglauer', 'Publisher': 'University of Washington Press',
                             'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}], 4, 'Noguchi')
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_no_valid_books_partial_shelf(self, mock_stdout):
        expected = ("\nYou have 0 item(s) that match your search criteria:\n\n"
                    "\nSearch Completed. Returning to menu...\n\n")
        search_the_library([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                             'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                             'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                     'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',
                                                     'Category': 'Mathematics', 'Subject': 'Algebra'},
                            {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                'Iglauer', 'Publisher': 'University of Washington Press',
                             'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}], 4, '2')
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_category_author_valid_books(self, mock_stdout):
        expected = ("\nYou have 1 item(s) that match your search criteria:\n\n"
                    "#---------------------------------------#\n"
                    "\tResult: #1\n\n"

                    "\tTitle: Elementary Linear Algebra 3e\n"
                    "\tAuthor: Shields\n"
                    "\tPublisher: Worth\n"
                    "\tShelf: 27\n"
                    "\tCategory: Mathematics\n"
                    "\tSubject: Algebra\n"
                    "#---------------------------------------#\n"
                    "\nSearch Completed. Returning to menu...\n\n")
        search_the_library([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                             'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                             'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                     'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',
                                                     'Category': 'Mathematics', 'Subject': 'Algebra'},
                            {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                'Iglauer', 'Publisher': 'University of Washington Press',
                             'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}], 2, 'Shields')
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_category_author_valid_books_partial_string(self, mock_stdout):
        expected = ("\nYou have 1 item(s) that match your search criteria:\n\n"
                    "#---------------------------------------#\n"
                    "\tResult: #1\n\n"

                    "\tTitle: Elementary Linear Algebra 3e\n"
                    "\tAuthor: Shields\n"
                    "\tPublisher: Worth\n"
                    "\tShelf: 27\n"
                    "\tCategory: Mathematics\n"
                    "\tSubject: Algebra\n"
                    "#---------------------------------------#\n"
                    "\nSearch Completed. Returning to menu...\n\n")
        search_the_library([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                             'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                             'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                     'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',
                                                     'Category': 'Mathematics', 'Subject': 'Algebra'},
                            {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                'Iglauer', 'Publisher': 'University of Washington Press',
                             'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}], 2, 'ields')
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_no_valid_book_category_author(self, mock_stdout):
        expected = ("\nYou have 0 item(s) that match your search criteria:\n\n"
                    "\nSearch Completed. Returning to menu...\n\n")
        search_the_library([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                             'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                             'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                     'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',
                                                     'Category': 'Mathematics', 'Subject': 'Algebra'},
                            {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                'Iglauer', 'Publisher': 'University of Washington Press',
                             'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}], 2, 'asdf')
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_category_title_valid_books(self, mock_stdout):
        expected = ("\nYou have 2 item(s) that match your search criteria:\n\n"
                    "#---------------------------------------#\n"
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
                    "\nSearch Completed. Returning to menu...\n\n"
                    )
        search_the_library([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                             'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                             'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                     'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',
                                                     'Category': 'Mathematics', 'Subject': 'Algebra'},
                            {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                'Iglauer', 'Publisher': 'University of Washington Press',
                             'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}], 1,
                           'Elementary Linear Algebra 3e')
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_category_title_valid_books_partial_string(self, mock_stdout):
        expected = ("\nYou have 2 item(s) that match your search criteria:\n\n"
                    "#---------------------------------------#\n"
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
                    "\nSearch Completed. Returning to menu...\n\n"
                    )
        search_the_library([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                             'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                             'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                     'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',
                                                     'Category': 'Mathematics', 'Subject': 'Algebra'},
                            {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                'Iglauer', 'Publisher': 'University of Washington Press',
                             'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}], 1,
                           'Element')
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_no_valid_book_category_title(self, mock_stdout):
        expected = ("\nYou have 0 item(s) that match your search criteria:\n\n"
                    "\nSearch Completed. Returning to menu...\n\n")
        search_the_library([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                             'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                             'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                     'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',
                                                     'Category': 'Mathematics', 'Subject': 'Algebra'},
                            {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                'Iglauer', 'Publisher': 'University of Washington Press',
                             'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}], 1, 'asdf')
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_category_publisher_valid_books(self, mock_stdout):
        expected = ("\nYou have 1 item(s) that match your search criteria:\n\n"
                    "#---------------------------------------#\n"
                    "\tResult: #1\n\n"

                    "\tTitle: Elementary Linear Algebra 3e\n"
                    "\tAuthor: Shields\n"
                    "\tPublisher: Worth\n"
                    "\tShelf: 27\n"
                    "\tCategory: Mathematics\n"
                    "\tSubject: Algebra\n"
                    "#---------------------------------------#\n"
                    "\nSearch Completed. Returning to menu...\n\n")
        search_the_library([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                             'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                             'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                     'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',
                                                     'Category': 'Mathematics', 'Subject': 'Algebra'},
                            {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                'Iglauer', 'Publisher': 'University of Washington Press',
                             'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}], 3, 'Worth')
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_category_publisher_valid_books_partial_string(self, mock_stdout):
        expected = ("\nYou have 1 item(s) that match your search criteria:\n\n"
                    "#---------------------------------------#\n"
                    "\tResult: #1\n\n"

                    "\tTitle: Elementary Linear Algebra 3e\n"
                    "\tAuthor: Shields\n"
                    "\tPublisher: Worth\n"
                    "\tShelf: 27\n"
                    "\tCategory: Mathematics\n"
                    "\tSubject: Algebra\n"
                    "#---------------------------------------#\n"
                    "\nSearch Completed. Returning to menu...\n\n")
        search_the_library([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                             'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                             'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                     'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',
                                                     'Category': 'Mathematics', 'Subject': 'Algebra'},
                            {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                'Iglauer', 'Publisher': 'University of Washington Press',
                             'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}], 3, 'Wor')
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_no_valid_book_category_publisher(self, mock_stdout):
        expected = ("\nYou have 0 item(s) that match your search criteria:\n\n"
                    "\nSearch Completed. Returning to menu...\n\n")
        search_the_library([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                             'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                             'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                     'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',
                                                     'Category': 'Mathematics', 'Subject': 'Algebra'},
                            {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                'Iglauer', 'Publisher': 'University of Washington Press',
                             'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}], 3, 'bds')
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_category_category_valid_books(self, mock_stdout):
        expected = ("\nYou have 2 item(s) that match your search criteria:\n\n"
                    "#---------------------------------------#\n"
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
                    "\nSearch Completed. Returning to menu...\n\n"
                    )
        search_the_library([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                             'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                             'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                     'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',
                                                     'Category': 'Mathematics', 'Subject': 'Algebra'},
                            {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                'Iglauer', 'Publisher': 'University of Washington Press',
                             'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}], 5, 'Mathematics')
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_category_category_valid_books_partial_string(self, mock_stdout):
        expected = ("\nYou have 2 item(s) that match your search criteria:\n\n"
                    "#---------------------------------------#\n"
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
                    "\nSearch Completed. Returning to menu...\n\n"
                    )
        search_the_library([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                             'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                             'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                     'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',
                                                     'Category': 'Mathematics', 'Subject': 'Algebra'},
                            {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                'Iglauer', 'Publisher': 'University of Washington Press',
                             'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}], 5, 'Math')
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_no_valid_book_category_category(self, mock_stdout):
        expected = ("\nYou have 0 item(s) that match your search criteria:\n\n"
                    "\nSearch Completed. Returning to menu...\n\n")
        search_the_library([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                             'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                             'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                     'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',
                                                     'Category': 'Mathematics', 'Subject': 'Algebra'},
                            {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                'Iglauer', 'Publisher': 'University of Washington Press',
                             'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}], 5, 'bds')
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_category_subject_valid_books(self, mock_stdout):
        expected = ("\nYou have 2 item(s) that match your search criteria:\n\n"
                    "#---------------------------------------#\n"
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
                    "\nSearch Completed. Returning to menu...\n\n"
                    )
        search_the_library([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                             'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                             'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                     'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',
                                                     'Category': 'Mathematics', 'Subject': 'Algebra'},
                            {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                'Iglauer', 'Publisher': 'University of Washington Press',
                             'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}], 6, 'Algebra')
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_category_subject_valid_books_partial_string(self, mock_stdout):
        expected = ("\nYou have 2 item(s) that match your search criteria:\n\n"
                    "#---------------------------------------#\n"
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
                    "\nSearch Completed. Returning to menu...\n\n"
                    )
        search_the_library([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                             'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                             'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                     'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',
                                                     'Category': 'Mathematics', 'Subject': 'Algebra'},
                            {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                'Iglauer', 'Publisher': 'University of Washington Press',
                             'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}], 6, 'Alge')
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_no_valid_book_category_subject(self, mock_stdout):
        expected = ("\nYou have 0 item(s) that match your search criteria:\n\n"
                    "\nSearch Completed. Returning to menu...\n\n")
        search_the_library([{'Title': 'Elementary Linear Algebra 3e', 'Author': 'Anton',
                             'Publisher': 'Wiley', 'Shelf': '27', 'Category': 'Mathematics',
                             'Subject': 'Algebra'}, {'Title': 'Elementary Linear Algebra 3e',
                                                     'Author': 'Shields', 'Publisher': 'Worth', 'Shelf': '27',
                                                     'Category': 'Mathematics', 'Subject': 'Algebra'},
                            {'Title': "Seven Stones A Portrait of Arthur Erickson, Architect", 'Author':
                                'Iglauer', 'Publisher': 'University of Washington Press',
                             'Shelf': '9', 'Category': 'Architecture', 'Subject': 'Canadian'}], 6, 'bds')
        self.assertEqual(mock_stdout.getvalue(), expected)