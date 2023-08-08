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

# >>> import bcrypt
# >>> password = b"super secret password"
# >>> # Hash a password for the first time, with a randomly-generated salt
# >>> hashed = bcrypt.hashpw(password, bcrypt.gensalt())
# >>> # Check that an unhashed password matches one that has previously been
# >>> # hashed
# >>> if bcrypt.checkpw(password, hashed):
# ...     print("It Matches!")
# ... else:
# ...     print("It Does not Match :(")
