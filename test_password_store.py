import unittest

from password_store import PasswordStore


class TestPasswordStore(unittest.TestCase):
    def test_can_add_username_password(self):
        password_store = PasswordStore()
        password_store.add('user', 'password')

        true_result = password_store.verify('user', 'password')
        wrong_password_result = password_store.verify('user', 'not_the_password')
        wrong_username_result = password_store.verify('not_the_user', 'password')

        self.assertTrue(true_result)
        self.assertFalse(wrong_username_result)
        self.assertFalse(wrong_password_result)