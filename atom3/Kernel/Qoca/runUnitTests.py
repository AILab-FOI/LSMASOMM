
def runUnitTests():
    import unittest    
    suite = unittest.TestSuite()
    
    print 'NOTE: if import fails, try running it from a higher-level directory'
    print 'IE: ..\\atom3\\Kernel> python Qoca\\runUnitTests.py\n'
        
    from unittests.QocaBasicConstraints import QocaBasicConstraints
    suite.addTest(unittest.makeSuite(QocaBasicConstraints))
    
    from unittests.pipeTest import PipeTest
    suite.addTest(unittest.makeSuite(PipeTest))
    
    from unittests.QocaWrapperTest import QocaWrapperTest
    suite.addTest(unittest.makeSuite(QocaWrapperTest))
    
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    runUnitTests()
    
