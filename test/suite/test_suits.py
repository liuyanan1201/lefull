import sys
import unittest

sys.path.append("../..")
from test.case.监管平台.test_landlord import TestLandLord


smoke_suit = unittest.TestSuite()
smoke_suit.addTest(TestLandLord('test_landlord_new'))

def get_suit(suite_name):
    return globals().get(suite_name)