# use this to test @@ python  -m unittest test_shop.py -k test_successful_purchase


import unittest
from unittest.mock import patch
from io import StringIO

from shop import simulate_shop, InsufficientFundsError

class ShopProgramTest(unittest.TestCase):
    def setUp(self):
        self.items = {
            "aPPlE": 50,
            "bAnaNa": 75,
            "laPtoP": 150
        }

    @patch("builtins.input", side_effect=["aPPlE", "bAnaNa", "laPtoP", "exit"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_successful_purchase(self, mock_stdout, mock_input):
        simulate_shop()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Here's your aPPlE!", output)
        self.assertIn("Here's your bAnaNa!", output)
        self.assertIn("Here's your laPtoP!", output)

    @patch("builtins.input", side_effect=["TaKeaWaY", "exit"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_invalid_item(self, mock_stdout, mock_input):
        simulate_shop()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Invalid input! Please select a valid item.", output)

    @patch("builtins.input", side_effect=["laPtoP", "yes", "50", "bAnaNa", "exit"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_insufficient_funds(self, mock_stdout, mock_input):
        simulate_shop()
        output = mock_stdout.getvalue().strip()
        self.assertIn("You don't have enough money to purchase this item.", output)
        self.assertIn("Additional money added to your balance.", output)
        self.assertIn("Here's your bAnaNa!", output)

    @patch("builtins.input", side_effect=["aPPlE", "aPPlE", "aPPlE", "exit"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_maximum_items_reached(self, mock_stdout, mock_input):
        simulate_shop()
        output = mock_stdout.getvalue().strip()
        self.assertIn("You have reached the maximum number of items to purchase.", output)

    @patch("builtins.input", side_effect=["exit"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_exit_shop(self, mock_stdout, mock_input):
        simulate_shop()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Thank you for visiting the shop!", output)
        self.assertNotIn("Here's your", output)
        self.assertNotIn("Invalid input!", output)

if __name__ == "__main__":
    unittest.main()
