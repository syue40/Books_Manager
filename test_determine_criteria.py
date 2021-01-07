"""
This Unittest will test the function determine_criteria from books.py
"""
from unittest import TestCase
from books import determine_criteria


class TestDetermineCriteria(TestCase):
    def test_determine_criteria_title(self):
        expected = 'Title'
        actual = determine_criteria(1)
        self.assertEqual(expected, actual)

    def test_determine_criteria_author(self):
        expected = 'Author'
        actual = determine_criteria(2)
        self.assertEqual(expected, actual)

    def test_determine_criteria_shelf(self):
        expected = 'Shelf'
        actual = determine_criteria(4)
        self.assertEqual(expected, actual)

    def test_determine_criteria_category(self):
        expected = 'Category'
        actual = determine_criteria(5)
        self.assertEqual(expected, actual)
