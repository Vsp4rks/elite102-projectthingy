import unittest
import main

class Test(unittest.TestCase):

    def test_connection(self):
        result = main.connection.cursor()
        self.assertIsNotNone(result)

    def test_account_add(self):
        result = main.accountcreate("99", "woowow", "genesis" "81109")
        self.assertIsNotNone(result)


if __name__ == '__main__':
    print("toodles!")
    unittest.main()