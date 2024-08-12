import unittest
from datetime import datetime
from Year import get_publication_year

class TestGetPublicationYear(unittest.TestCase):

    def test_none_input(self):
        self.assertIsNone(get_publication_year(None))

    def test_non_numeric_input(self):
        self.assertIsNone(get_publication_year("19A0"))
        self.assertIsNone(get_publication_year("abcd"))
    
    def test_invalid_length_input(self):
        self.assertIsNone(get_publication_year("190"))
        self.assertIsNone(get_publication_year("19001"))
    
    def test_year_greater_than_current(self):
        future_year = datetime.now().year + 1
        self.assertIsNone(get_publication_year(str(future_year)))


     

     
    

if __name__ == '__main__':
    unittest.main()
