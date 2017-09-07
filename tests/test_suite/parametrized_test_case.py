# Taken from: http://eli.thegreenplace.net/2011/08/02/python-unit-testing-parametrized-test-cases

import unittest

class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', parameter=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.parameter = parameter

    @staticmethod
    def parametrize(testcase_klass, parameter=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'parameter'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, parameter=parameter))
        return suite
