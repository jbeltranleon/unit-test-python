import unittest

from main import print_hi, printer, op
from unittest.mock import patch, mock_open

from util.helper import Utility
from util import helper


class MyTestCase(unittest.TestCase):

    @patch.object(Utility, 'process')
    def test_something_else(self, mock_process):
        name = 'Python'

        return_value = 'Mock Python Mock'

        mock_process.return_value = return_value

        message = printer(name)

        actual_message = 'Hi, Mock Python Mock'
        self.assertEqual(message, actual_message)
        mock_process.assert_called()


    @patch('builtins.open')
    def test_opener(self, mock_op):
        file = '1.txt'

        op(file)
        mock_op.assert_called_once()


if __name__ == '__main__':
    unittest.main()
