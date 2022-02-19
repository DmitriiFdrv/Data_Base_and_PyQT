import sys

from common.utils import *
from common.variables import *
from client import *
from server import *
import unittest
from unittest.mock import patch


class TestServer(unittest.TestCase):
    """создаем тестовый случай"""

    err_dict = {
        RESPONSE: 400,
        ERROR: 'bad request'
    }
    ok_dict = {RESPONSE: 200}

    def test_def_message_check(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'guest'}}
        ), self.ok_dict)

    def test_def_message_no_action(self):
        self.assertEqual(process_client_message(
            {TIME: '1.1', USER: {ACCOUNT_NAME: 'guest'}}
        ), self.err_dict)

    def test_def_message_no_time(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'guest'}}
        ), self.err_dict)

    def test_def_message_no_user(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: '1.1'}
        ), self.err_dict)


if __name__ == '__main__':
    unittest.main()