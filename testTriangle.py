#!/usr/bin/env python

"""
Verification d'un triangle quelconque

"""

# ----------------------------------------------------------------------------------------------------------------------
import unittest

# ----------------------------------------------------------------------------------------------------------------------
import triangle


# ----------------------------------------------------------------------------------------------------------------------
class TestUM(unittest.TestCase):
    # ------------------------------------------------------------------------------------------------------------------
    def test_print(self):
        test_triangle = triangle.triangle(3, 4, 5)
        self.assertEqual('Triangle: 3, 4, 5', "%s" % test_triangle)

    # ------------------------------------------------------------------------------------------------------------------
    def test_perimetre(self):
        test_triangle = triangle.triangle(3, 4, 5)
        self.assertEqual(3 + 4 + 5, test_triangle.perimetre())

    # ------------------------------------------------------------------------------------------------------------------
    def test_isocele(self):
        test_triangle = triangle.triangle(3, 4, 3)
        self.assertTrue(test_triangle.isIsocele())

    # ------------------------------------------------------------------------------------------------------------------
    def test_isocele_text(self):
        test_triangle = triangle.triangle(3, 4, 3)
        self.assertEqual(r"Triangle: 3, 4, 3 ISOCELE", test_triangle.__str__())

    # ------------------------------------------------------------------------------------------------------------------
    def test_equilateral(self):
        test_triangle = triangle.triangle(2, 2, 2)
        self.assertTrue(test_triangle.isEquilateral())

    # ------------------------------------------------------------------------------------------------------------------
    def test_equilateral_text(self):
        test_triangle = triangle.triangle(2, 2, 2)
        self.assertEqual(r"Triangle: 2, 2, 2 EQUILATERAL TEST", test_triangle.__str__())

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
