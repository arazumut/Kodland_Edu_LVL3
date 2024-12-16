import unittest
import os
from commands import add_task, complete_task, show_tasks
from database import init_db

class TestCompleteTask(unittest.TestCase):
    def setUp(self):
        if os.path.exists("tasks.db"):
            os.remove("tasks.db")
        init_db()

    def test_complete_task(self):
        add_task("Tamamlanacak görev")
        complete_task(1)
        tasks = show_tasks()
        self.assertIn("Tamamlandı", tasks)

if __name__ == "__main__":
    unittest.main()