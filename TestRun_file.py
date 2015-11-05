__author__ = 'rahul'

import unittest
import GoogleTest
import WikiTest
import os
import HTMLTestRunner

direct = os.getcwd()

class MyTestSuite(unittest.TestCase):

    def test_Issue(self):

        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(WikiTest.MyWikiTestCase),
            unittest.defaultTestLoader.loadTestsFromTestCase(GoogleTest.MyGoogleTest),
        ])

        outfile = open(direct + "\SmokeTest.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            description='Smoke Tests'
        )

        runner1.run(smoke_test)





if __name__ == '__main__':
    unittest.main()
