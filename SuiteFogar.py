import unittest

import testAdminRmn
import testAdminRmg

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTest(loader.loadTestsFromModule(testAdminRmn))
suite.addTest(loader.loadTestsFromModule(testAdminRmg))


runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

