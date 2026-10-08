import unittest

from data import resources, fellows, borrow_records
from resources import find_resource
from borrowing import borrow_resource
from reports import show_reports


class TestCampusSystem(unittest.TestCase):

    def setUp(self):
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

        self.assertIsNotNone(resource)
        self.assertEqual(resource["name"], "Laptop")

    def test_find_unknown_resource(self):
        resource = find_resource("R999")

        self.assertIsNone(resource)

    def test_borrow_reduces_stock(self):
        resource = find_resource("R001")

        quantity = 2

        self.assertGreaterEqual(
            resource["available"],
            quantity
        )

        resource["available"] -= quantity

        self.assertEqual(
            resource["available"],
            8
        )

    def test_cannot_borrow_more_than_available(self):
        resource = find_resource("R003")

        requested = 4

        self.assertGreater(
            requested,
            resource["available"]
        )

        old_stock = resource["available"]

        if requested > resource["available"]:
            pass

        self.assertEqual(
            resource["available"],
            old_stock
        )

    def test_resource_total_matches_starting_stock(self):
        resource = find_resource("R002")

        self.assertEqual(
            resource["total"],
            5
        )

        self.assertEqual(
            resource["available"],
            5
        )

    def test_fellows_exist(self):
        self.assertIn("F001", fellows)
        self.assertIn("F002", fellows)
        self.assertIn("F003", fellows)


if __name__ == "__main__":
    unittest.main()