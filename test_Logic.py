import unittest
from Logic import APPLogic

class TestAPPLogic(unittest.TestCase):
    def setUp(self):
        """Create instance of APPLogic class before each test"""
        self.app_logic = APPLogic()

    def test_add_task(self):
        #add a task
        task = self.app_logic.add_task("Test Task", "Work", "High")

        # Test that task was added & return value = a dictionary
        self.assertIsInstance(task, dict)

        # Check that task dictionary has correct keys
        self.assertIn("id", task)
        self.assertIn("name", task)
        self.assertIn("category", task)
        self.assertIn("priority", task)
        self.assertIn("status", task)

        # Check if task values are as expected
        self.assertEqual(task["name"], "Test Task")
        self.assertEqual(task["category"], "Work")
        self.assertEqual(task["priority"], "High")
        self.assertEqual(task["status"], "Pending")  # Default value for status

        # Test that task_id is correct (should be 1 for 1st task)
        self.assertEqual(task["id"], 1)

        # Test that the task is actually added to the tasks list
        self.assertEqual(len(self.app_logic.tasks), 1)
        self.assertEqual(self.app_logic.tasks[0], task)

    def test_multiple_tasks(self):
        # Add more tasks to check if task_id increments correctly
        task_1 = self.app_logic.add_task("Test Task 1", "Personal", "Medium")
        task_2 = self.app_logic.add_task("Test Task 2", "Work", "Low")

        # Verify that IDs are unique and incremented
        self.assertEqual(task_1["id"], 1)
        self.assertEqual(task_2["id"], 2)

        # Verify total number of tasks
        self.assertEqual(len(self.app_logic.tasks), 2)

    def test_delete_existing_task(self):
        """Test deleting a task already existing in a list"""
        #add some tasks
        self.app_logic.add_task("Task 1", "Work", "High")
        self.app_logic.add_task("Task 2", "Personal", "Medium")

        #verify initial task count
        self.assertEqual(len(self.app_logic.tasks), 2)

        #delete first task
        result = self.app_logic.delete_task(1)

        # Assert that deletion was successful
        self.assertTrue(result)

        # Assert that task list has decreased in size
        self.assertEqual(len(self.app_logic.tasks), 1)

        # Assert that the remaining task is the correct one
        self.assertEqual(self.app_logic.tasks[0]["id"], 2)

    def test_delete_nonexistent_task(self):
        """Test deleting a task that does not exist."""
        self.app_logic.add_task("Task 1", "Work", "High")

        # Try to delete a non-existent task
        result = self.app_logic.delete_task(99)  # ID 99 does not exist

        # Assert that deletion was unsuccessful
        self.assertFalse(result)

        # Assert that task list size stays the same
        self.assertEqual(len(self.app_logic.tasks), 1)


if __name__ == '__main__':
    unittest.main()
