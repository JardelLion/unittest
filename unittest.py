import unittest
import string

def encrypt(message):
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    encrypted_message = "".join([abc[abc.find(char) + 1] if  len(abc) > (abc.find(char) + 1) else abc[idx] for idx, char in enumerate(message)])
    return encrypted_message


class TestEncryption(unittest.TestCase):
    # tests go here

    def setUp(self):
        super().setUp()
        self.my_message = "jardel fgt"

    def test_inputExists(self):
        self.assertIsNotNone(self.my_message)


    def test_inputType(self):
        self.assertIsInstance(self.my_message, str)


    def test_functionReturnSomething(self):
        self.assertIsNotNone(encrypt(self.my_message))


    def test_lenIO(self):
        self.assertEqual(len(self.my_message), len(encrypt(self.my_message)))


    def test_differentIO(self):
        self.assertNotIn(self.my_message,encrypt(self.my_message))


    def test_outputType(self):
        self.assertIsInstance(encrypt(self.my_message), str)

    def test_shiftedCipher(self):
        abc = string.ascii_letters + string.punctuation + string.digits + " "
        encrypted_message = "".join(
            [abc[abc.find(char) + 1] if len(abc) > (abc.find(char) + 1) else abc[idx] for idx, char in
             enumerate(self.my_message)])
        self.assertEqual(encrypt(self.my_message), encrypted_message)
