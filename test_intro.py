"""
This Unittest will test the function intro from books.py
"""
import io
import unittest
from unittest import TestCase
from unittest.mock import patch
from books import intro


class printIntro(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_a_book(self, mock_stdout):
        expected = ("\nHello, welcome to the your virtual library!\n"
                    "Here are some instructions on how to use your library! You have the following options:\n\n"

                    "To search by title enter 1:\n"
                    "To search by author enter 2:\n"
                    "To search by publisher enter 3:\n"
                    "To search by shelf enter 4:\n"
                    "To search by category enter 5:\n"
                    "To search by subject enter 6:\n\n"

                    "To move a book to a different shelf enter 7:\n\n"

                    "And to quit the program and save changes, press 8:\n\n"

                    "After you enter a number for your search criteria, please enter a keyword that you wish to "
                    "search by.\n"
                    "You can enter a full title, name, publisher etc. or a partial one if you're having trouble "
                    "remembering!\n"
                    "If you want to move a book, please search for the exact title of the book you wish to move!\n")

        intro()
        self.assertEqual(mock_stdout.getvalue(), expected)

