import unittest
from testcase.监管平台 import test_ownership,test_landlord

smoke_suite = unittest.TestSuite()
smoke_suite.addTest(test_landlord.TestLandLord("test_1_landlord_new"))
smoke_suite.addTest(test_landlord.TestLandLord("test_2_landlord_query"))



# loader=unittest.TestLoader()
# suite1=loader.loadTestsFromModule(test_landlord)
# suite2=loader.loadTestsFromTestCase(test_ownership.TestOwnerShip)
# suite3=loader.loadTestsFromName(test_landlord.TestLandLord.test_1_landlord_new())


# all=unittest.defaultTestLoader.discover(".")

if __name__=="__main__":
    unittest.TextTestRunner(verbosity=2).run(smoke_suite)
