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

    def test_search_tasks (self):
        """Test searching 4 tasks by keyword"""
        self.app_logic.add_task(name="Work Task", category="Work", priority="High")
        self.app_logic.add_task(name="Personal Task", category="Personal", priority="Medium")
        self.app_logic.add_task(name="Study Task", category="Study", priority="Low")

        # Test search by name
        result = self.app_logic.search_tasks("work")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "Work Task")

        # search by category
        result = self.app_logic.search_tasks("personal")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["category"], "Personal")

        # search by priority
        result = self.app_logic.search_tasks("low")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["priority"], "Low")

        # Test no results
        result = self.app_logic.search_tasks("nonexistent")
        self.assertEqual(len(result), 0)

    def test_edit_task(self):
        self.app_logic.add_task(name="Test Task", category="Work", priority="High")

        task_id = 1  # ID of the task we just added

        # Edit task's name & priority
        result = self.app_logic.edit_task(task_id, name="Updated Task", priority="Low")

        # Assert that task was edited successfully
        self.assertTrue(result)  # Ensure edit_task returns True

        # Get edited task
        task = self.app_logic.tasks[0]

        # Check that task's name & priority were updated
        self.assertEqual(task["name"], "Updated Task")
        self.assertEqual(task["priority"], "Low")

    def test_edit_task_nonexistent(self):
        """Test editing a task that does not exist."""
        result = self.app_logic.edit_task(task_id=999, name="Non-Existent Task")  # Try to edit a task with a non-existent ID

        # check that result = False since task doesn't exist
        self.assertFalse(result)


    """ TEST UTILITY FUNCTIONS!!!"""
    def test_validate_valid_input (self):
        """Test that valid input passes validation."""
        result = self.app_logic.validate_input(name="Test Task", category="Work", priority="High")
        self.assertTrue(result)

    def test_validate_invalid_input(self):
        """Test that empty name fails validation."""
        result = self.app_logic.validate_input(name="", category="Work", priority="High")
        self.assertFalse(result)

    def test_validate_input_invalid_priority(self):
        """Test that an invalid priority fails validation."""
        result = self.app_logic.validate_input(name="Test Task", category="Work", priority="Urgent")
        self.assertFalse(result)

    """TEST SAVING FILE"""
    def test_save_to_file(self):
        """Test saving tasks to a file."""
        # Add a task to save
        self.app_logic.add_task(name="Test Task", category="Work", priority="High")
        result = self.app_logic.save_to_file("tasks.csv")
        self.assertTrue(result)

        # Verify that the file exists and can be read
        with open("tasks.csv", mode="r", newline="", encoding="utf-8") as file:
            lines = file.readlines()
            self.assertGreater(len(lines), 0)  # Ensure the file is not empty

    def test_save_to_file_invalid(self):
        """Test saving tasks to a file with invalid path."""
        result = self.app_logic.save_to_file("/invalid/path/tasks.csv")
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
