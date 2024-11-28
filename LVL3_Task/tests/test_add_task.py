import unittest
from commands import add_task, show_tasks

class TestAddTask(unittest.TestCase):
    def test_add_and_show_tasks(self):
        add_task("Yeni görev")
        tasks = show_tasks()
        self.assertIn("Yeni görev", tasks)

if __name__ == "__main__":
    unittest.main()
