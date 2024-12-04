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

    def test_mark_completed_existing(self):
        """Test marking an existing task as completed."""
        self.app_logic = APPLogic()
        self.app_logic.add_task(name="Test Task 1", category="Work", priority="High")
        self.app_logic.add_task(name="Test Task 2", category="Personal", priority="Low")

        task_id = 1  # ID of the first task
        print(f"Task list before marking completed: {self.app_logic.tasks}")
        result = self.app_logic.mark_completed(task_id)
        print(f"Task list after marking completed: {self.app_logic.tasks}")

        # Assert that the task was marked completed
        self.assertTrue(result)  # Ensure mark_completed returns True
        self.assertEqual(self.app_logic.tasks[0]["status"], "Completed")  # Check status

    def test_mark_completed_nonexistent(self):
        """Test marking a non_existent task as completed"""
        task_id = 999 #non-existent task_id
        result = self.app_logic.mark_completed(task_id)

        #Make sure it returns false
        self.assertFalse(result)

    def test_get_completed(self):
        """Test getting all tasks marked as completed."""
        self.app_logic.add_task(name="Task 1", category="Work", priority="High")
        self.app_logic.add_task(name="Task 2", category="Personal", priority="Medium")
        self.app_logic.add_task(name="Task 3", category="Study", priority="Low")

        self.app_logic.mark_completed(1)  # Mark Task 1 as completed
        self.app_logic.mark_completed(3)  # Mark Task 3 as completed

        completed_tasks = self.app_logic.get_completed_tasks()  # Get completed tasks

        self.assertEqual(len(completed_tasks), 2)  # Two tasks should be marked as completed
        self.assertEqual(completed_tasks[0]["id"], 1)  # Check first completed task
        self.assertEqual(completed_tasks[1]["id"], 3)  # Check second completed task
        self.assertTrue(all(task["status"] == "Completed" for task in completed_tasks))  # Verify status

    def test_get_all_tasks(self):
        """Test getting all tasks"""
        self.app_logic.add_task(name="Task 1", category="Work", priority="High")
        self.app_logic.add_task(name="Task 2", category="Personal", priority="Medium")
        self.app_logic.add_task(name="Task 3", category="Study", priority="Low")

        all_tasks = self.app_logic.get_all_tasks()

        # check number of tasks retrieved
        self.assertEqual(len(all_tasks), 3)  # Expect 3 tasks
        # Check if tasks match what was added
        self.assertEqual(all_tasks[0]["name"], "Task 1")
        self.assertEqual(all_tasks[1]["name"], "Task 2")
        self.assertEqual(all_tasks[2]["name"], "Task 3")


if __name__ == '__main__':
    unittest.main()
