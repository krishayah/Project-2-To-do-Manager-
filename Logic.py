import csv


class APPLogic:
    """
    Core logic for To-Do List Manager App
    """
    def __init__(self):
        """
        Initialize w/ empty list of tasks.
        """
        self.tasks = []

    def add_task(self, name: str, category: str, priority: str) -> dict:
        """
        Add new task to task list
        Args:
            name(str): Name of task
            category (str): task category (ex. Work, Personal)
        :returns:
            dict: the added task
        """
        #Make a unique ID based on current task count
        task_id = len(self.tasks) + 1

        #Create a task dictionary
        task = {
            "id": task_id,
            "name": name,
            "category": category,
            "priority": priority,
            "status": "Pending"
        }

        # Add task to list
        self.tasks.append(task)
        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Deletes a task by its ID
        Args:
            task_id(int): Unique ID of task to delete
        Returns:
            bool: True if task = deleted, False if task Not Found!
        """
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                return True
            return False

    def mark_completed(self, task_id: int) -> bool:
        """
        Mark a task as completed.
        Args:
            task_id (int): Unique ID of task
        Returns:
             bool: True if marked as completed, False if Task not found.
        """
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "Completed"
                return True
        return False

    def edit_task(self, task_id: int, **kwargs) -> bool:
        """
        Edits an existing task.
        Args:
            task_id (int): Unique ID of the task.
            **kwargs: Fields to update (e.g., name, category, priority).
        Returns:
            bool: True if Task was edited, False if task Not Found.
        """
        for task in self.tasks:
            if task["id"]== task_id:
                #update provided fields
                for key, value in kwargs.items():
                    if key in task:
                        task[key] = value
                return True
        return False

    def get_all_tasks(self) -> list:
        """
        Retrieve all tasks.
        Returns:
            list: List of tasks
        """
        return self.tasks

    def search_tasks(self, keyword: str) -> list:
        """
        Search for tasks matching a keyword.
        Args:
            keyword (str): Search term.
        Returns:
            list: List of matching tasks.
        """
        keyword_lower = keyword.lower()
        return[
            task for task in self.tasks
            if keyword_lower in task["name"].lower()
            or keyword_lower in task["category"].lower()
            or keyword_lower in task["priority"].lower()
            or keyword_lower in task["status"].lower()
        ]

    """UTILITY FUNCTIONS"""
    def validate_input(self, **kwargs):
        """
        Validate task input fields.
        Args:
            **kwargs: Task fields to validate (e.g., name, category, priority).
        Returns:
            bool: True if input is valid, False otherwise.
        """
        #Validation Rules
        if "name" in kwargs:
            name = kwargs["name"]
            if not name: #check if name is empty or None
                print("'name' field is empty")
                return False
            if not isinstance(name, str):  # Check if the name is not a string
                print("Validation failed: 'name' field must be a string.")
                return False

        # Validate the 'category' field
        if "category" in kwargs:
            category = kwargs["category"]
            if not category:  # Check if the category is empty or None
                print("Validation failed: 'category' field is empty.")
                return False
            if not isinstance(category, str):  # Check if the category is not a string
                print("Validation failed: 'category' field must be a string.")
                return False

        # Validate the 'priority' field
        if "priority" in kwargs:
            priority = kwargs["priority"]
            valid_priorities = ["Low", "Medium", "High"]  # List of valid priority levels
            if priority not in valid_priorities:  # Check if the priority is not valid
                print(f"Validation failed: 'priority' must be one of {valid_priorities}.")
                return False

        # If all validations pass, return True
        return True


    def save_to_file(self, filename: str) -> bool:
        """
        Save tasks to a CSV file.
        Args:
            filename (str): Path to the file.
        Returns:
            bool: True if saved successfully, False otherwise.
        """
        try:
            with open(filename, mode="w", newline="", encoding = "utf-8") as file:
                writer = csv.DictWriter (file, fieldnames = ["id", "name", "category", "priority", "status"])
                writer.writeheader()
                writer.writerow(self.tasks)
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False

    def load_tasks_4m_file(self, filename: str) -> bool:
        """
        Load tasks from a CSV file.
        Args:
            filename (str): Path to file.
        Returns:
            bool: True if loaded successfully, False otherwise.
        """
        try:
            with open(filename, mode = "r", newline = "", encoding = "utf-8") as file:
                reader = csv.DictReader(file)
                self.tasks = [
                    {
                        "id": int(row["id"]),
                        "name": row["name"],
                        "category": row["category"],
                        "priority": row ["priority"],
                        "status": row["status"],

                    }
                    for row in reader
                ]
            return True
        except Exception as e:
            print (f"Error loading from file: {e}")
            return False





