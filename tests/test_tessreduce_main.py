# test the main functions in TESSreduce

import unittest
import tessreduce as tr

class TestTESSreduce(unittest.TestCase):

    def setUp(self):
        self.ra = 189.1385817
        self.dec = 11.2316535
        self.tess = tr.tessreduce(ra=self.ra, dec=self.dec)
        self.tess.get_ref()

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

    def test_diff_lc(self):

        self.tess.Diff_lc()

if __name__ == '__main__':
    unittest.main()
