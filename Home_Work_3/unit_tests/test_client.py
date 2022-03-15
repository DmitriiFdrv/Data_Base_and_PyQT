import sys

from common.utils import *
from common.variables import *
from client import *
from server import *
import unittest
from unittest.mock import patch


class TestClient(unittest.TestCase):
    """создаем тестовый случай"""

    def test_def_presence(self):
        test = create_presence()
        test[TIME] = 1

        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'guest'}})

    def test_def_process_ans(self):
        self.assertEqual(process_ans({RESPONSE: 200}), '200 : OK')


if __name__ == '__main__':
    unittest.main()