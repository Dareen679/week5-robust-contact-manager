"""Unit tests for the contact manager's main features and error handling."""

import unittest
from contextlib import redirect_stdout
from io import StringIO

import contact_manager


class TestContactManager(unittest.TestCase):
    """Check successful actions and the errors users might encounter."""

    def setUp(self):
        """Start with fresh contacts so tests do not affect one another."""
        contact_manager.contacts.clear()

    def test_add_new_contact(self):
        """A newly added contact should be stored with its phone number."""
        with redirect_stdout(StringIO()):
            contact_manager.add_contact("Alice", "555-0101")
        self.assertEqual(contact_manager.contacts["Alice"], "555-0101")

    def test_find_existing_contact(self):
        """Finding a saved name should return the correct phone number."""
        contact_manager.contacts["Bob"] = "555-0102"
        with redirect_stdout(StringIO()):
            result = contact_manager.find_contact("Bob")
        self.assertEqual(result, "555-0102")

    def test_find_missing_contact(self):
        """Finding an unknown name should return None, not crash."""
        output = StringIO()
        with redirect_stdout(output):
            result = contact_manager.find_contact("Missing")
        self.assertIsNone(result)
        self.assertIn("Contact not found.", output.getvalue())

    def test_delete_existing_contact(self):
        """Deleting a saved name should remove it from the dictionary."""
        contact_manager.contacts["Carlos"] = "555-0103"
        with redirect_stdout(StringIO()):
            contact_manager.delete_contact("Carlos")
        self.assertNotIn("Carlos", contact_manager.contacts)

    def test_delete_missing_contact(self):
        """Deleting an unknown name should print a message, not crash."""
        output = StringIO()
        with redirect_stdout(output):
            contact_manager.delete_contact("Missing")
        self.assertIn("Contact not found.", output.getvalue())

    def test_duplicate_contact_raises_error(self):
        """Adding the same name twice should raise our custom exception."""
        contact_manager.contacts["Alice"] = "555-0101"
        with self.assertRaises(contact_manager.DuplicateContactError):
            contact_manager.add_contact("Alice", "555-9999")
        self.assertEqual(contact_manager.contacts["Alice"], "555-0101")


if __name__ == "__main__":
    unittest.main()
