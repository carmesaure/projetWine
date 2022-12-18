import sys
import unittest

sys.path.append("./")

from app.dataset import Dataset_Loader


"""
    This class is used to test the function from the class Dataset_Loader
"""
class Test_dataset(unittest.TestCase):

    """
        Load the data
    """
    def setUp(self):
        self.loader = Dataset_Loader('data/Wines.csv')

    """
        Test the train dataset size
    """
    def test_get_train_data(self):
        self.assertEqual(len(self.loader._get_train_data()[0]), 815)

    """
        Test the validation dataset size
    """
    def test_get_val_data(self):
        self.assertEqual(len(self.loader._get_val_data()[0]), 43)

    """
        Test the test dataset size
    """
    def test_get_test_data(self):
        self.assertEqual(len(self.loader._get_test_data()[0]), 285)

    """
        Test the dataset size
    """
    def test_get_data(self):
        self.assertEqual(len(self.loader._get_data()[0]), 1143)


#Run the tests
if __name__ == '__main__':
    test=Test_dataset()
    test.setUp()
    test.test_get_train_data()
    test.test_get_val_data()
    test.test_get_test_data()
    test.test_get_data()
    print("all tests passed")
    