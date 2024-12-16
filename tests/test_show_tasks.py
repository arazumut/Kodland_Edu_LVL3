import unittest
import os
from commands import add_task, show_tasks
from database import init_db

# Produced By K.Umut Araz

class TestShowTasks(unittest.TestCase):
    def setUp(self):
        if os.path.exists("tasks.db"):
            os.remove("tasks.db")
        init_db()

    def test_show_tasks(self):
        add_task("Gösterilecek görev")
        tasks = show_tasks()
        self.assertIn("Gösterilecek görev", tasks)

if __name__ == "__main__":
    unittest.main()