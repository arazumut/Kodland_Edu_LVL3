import unittest
from commands import add_task, show_tasks

class TestShowTasks(unittest.TestCase):
    def test_show_tasks(self):
        
        task_id = add_task("Test task to show")
        

        tasks = show_tasks()
        self.assertIn(task_id, [task['id'] for task in tasks])

if __name__ == '__main__':
    unittest.main()