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


class TestSocket:
    """создаем тестовый случай"""
    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_message = None
        self.received_message = None

    def send(self, message_to_send):
        json_test_message = json.dumps(self.test_dict)
        self.encoded_message = json_test_message.encode(ENCODING)
        self.received_message = message_to_send

    def recv(self, max_len):
        json_test_message = json.dumps(self.test_dict)
        return json_test_message.encode(ENCODING)


class TestUtils(unittest.TestCase):
    test_dict_send = {
        ACTION: PRESENCE,
        TIME: 1.1,
        USER: {ACCOUNT_NAME: 'test'}
    }
    test_dict_recv_ok = {RESPONSE: 200}
    test_dict_recv_err = {
        RESPONSE: 400,
        ERROR: 'bad request'
    }

    def test_send_mess(self):
        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        self.assertEqual(test_socket.encoded_message, test_socket.received_message)

    def test_get_mess(self):
        test_socket_ok = TestSocket(self.test_dict_recv_ok)

        self.assertEqual(get_message(test_socket_ok), self.test_dict_recv_ok)


if __name__ == '__main__':
    unittest.main()
