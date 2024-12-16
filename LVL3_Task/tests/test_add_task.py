import unittest
from commands import add_task, show_tasks

class TestAddTask(unittest.TestCase):
    def test_add_task(self):
        
        task_id = add_task("Test task to add")
        
        
        tasks = show_tasks()
        self.assertIn(task_id, [task['id'] for task in tasks])

if __name__ == '__main__':
    unittest.main()