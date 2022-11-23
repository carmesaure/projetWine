import sys
import unittest

sys.path.append("./")

from dataset import Dataset_Loader

class Test_dataset(unittest.TestCase):
    def setUp(self):
        self.loader = Dataset_Loader('data/Wines.csv')

    def test_get_train_data(self):
        self.assertEqual(len(self.loader._get_train_data()[0]), 490)

    def test_get_test_data(self):
        self.assertEqual(len(self.loader._get_test_data()[0]), 653)

    def test_get_data(self):
        self.assertEqual(len(self.loader._get_data()[0]), 1143)



if __name__ == '__main__':
    test=Test_dataset()
    test.setUp()
    test.test_get_train_data()
    test.test_get_test_data()
    test.test_get_data()
    print("all tests passed")
    