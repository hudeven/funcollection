#!/usr/bin/env python

import unittest

class TestDummy(unittest.TestCase):

    def test_pass(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
