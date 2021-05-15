"""
This file is the Mother of All Tests, it serves as the hub for all test suites
and is used to run the entire test suite.

Author: Samuel Rodriguez (sar325@cornell.edu)
Last Updated: 05/15/21
"""
import unittest

if __name__ == "__main__":
    testsuite = unittest.TestLoader().discover('.', pattern='*_test.py')
    unittest.TextTestRunner(verbosity=2).run(testsuite)
