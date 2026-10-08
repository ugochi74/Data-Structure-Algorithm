
import unittest
from unittest.mock import patch

from data import resources, borrow_records
from resources import find_resource
from borrowing import borrow_resource


class TestCampusResourceSystem(unittest.TestCase):

    def setUp(self):
        # Reset data before every test
        resources.clear()
        borrow_records.clear()

        resources.extend([
            {
                "id": "R001",
                "name": "Laptop",
                "category": "Electronics",
                "total": 10,
                "available": 10
            },
            {
                "id": "R002",
                "name": "Keyboard",
                "category": "Accessories",
                "total": 5,
                "available": 5
            },
            {
                "id": "R003",
                "name": "Headset",
                "category": "Accessories",
                "total": 3,
                "available": 3
            }
        ])

    def test_find_resource(self):
        resource = find_resource("R001")

        assert resource is not None
        assert resource["name"] == "Laptop"
        assert resource["available"] == 10

    def test_unknown_resource(self):
        resource = find_resource("R999")

        assert resource is None

    @patch("builtins.input", side_effect=["F001", "R001", "2"])
    def test_borrow_resource(self, mock_input):
        result = borrow_resource()

        resource = find_resource("R001")

        assert result is True
        assert resource["available"] == 8

        assert len(borrow_records) == 1
        assert borrow_records[0]["fellow_id"] == "F001"
        assert borrow_records[0]["resource_id"] == "R001"
        assert borrow_records[0]["quantity"] == 2

    @patch("builtins.input", side_effect=["F003", "R003", "4"])
    def test_cannot_borrow_more_than_available(self, mock_input):
        result = borrow_resource()

        resource = find_resource("R003")

        # Borrowing should fail
        assert result is False

        # Stock must remain unchanged
        assert resource["available"] == 3

        # No borrowing record should be created
        assert len(borrow_records) == 0

    @patch("builtins.input", side_effect=["F001", "R001", "0"])
    def test_quantity_must_be_positive(self, mock_input):
        result = borrow_resource()

        resource = find_resource("R001")

        assert result is False
        assert resource["available"] == 10
        assert len(borrow_records) == 0

    @patch("builtins.input", side_effect=["F999", "R001", "2"])
    def test_invalid_fellow(self, mock_input):
        result = borrow_resource()

        resource = find_resource("R001")

        assert result is False
        assert resource["available"] == 10
        assert len(borrow_records) == 0

    def test_starting_resources(self):
        assert len(resources) == 3

        laptop = find_resource("R001")
        keyboard = find_resource("R002")
        headset = find_resource("R003")

        assert laptop["total"] == 10
        assert keyboard["total"] == 5
        assert headset["total"] == 3


if __name__ == "__main__":
    unittest.main()
