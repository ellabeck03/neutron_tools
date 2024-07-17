import unittest
import fispact_input_reader
import os


class read_input_test_case(unittest.TestCase):
    """ test for reading the version of output file"""

    def test_read(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'fis_in.i')
        self.assertEqual(len(fispact_input_reader.read_fispact_input(path)),
                         64)


if __name__ == '__main__':
    unittest.main()
