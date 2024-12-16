import unittest
import os
from commands import add_task, delete_task, show_tasks
from database import init_db

class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        if os.path.exists("tasks.db"):
            os.remove("tasks.db")
        init_db()

    def test_delete_task(self):
        add_task("Silinecek görev")
        delete_task(1)
        tasks = show_tasks()
        self.assertNotIn("Silinecek görev", tasks)

if __name__ == "__main__":
    unittest.main()