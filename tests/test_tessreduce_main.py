# test the main functions in TESSreduce

import unittest
import tessreduce as tr

class TestTESSreduce(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Initial settup run only once before all the tests
        """
        super(TestTESSreduce, cls).setUpClass()

        ra = 189.1385817
        dec = 11.2316535
        cls.tess = tr.tessreduce(ra=ra, dec=dec)
        cls.tess.get_ref()

    #def setUp(self):
    #    ra = 189.1385817
    #    dec = 11.2316535
    #    self.tess = tr.tessreduce(ra=ra, dec=dec)
    #    self.tess.get_ref()

    def test_Make_mask(self):
        self.tess.Make_mask()

    def test_background(self):
        self.tess.background()

    def test_Centroids_DAO(self):
        self.tess.Centroids_DAO()

    def test_Shift_images(self):
        self.tess.Shift_images()

    def test_field_calibrate(self):
        self.tess.field_calibrate()

    def test_Diff_lc(self):
        self.tess.Diff_lc()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_Make_mask'))
    suite.addTest(WidgetTestCase('test_background'))
    suite.addTest(WidgetTestCase('test_Centroids_DAO'))
    suite.addTest(WidgetTestCase('test_Shift_images'))
    suite.addTest(WidgetTestCase('test_field_calibrate'))
    suite.addTest(WidgetTestCase('test_Diff_lc'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
