import unittest
from commands import add_task, complete_task, show_tasks

class TestCompleteTask(unittest.TestCase):
    def test_complete_task(self):
        
        task_id = add_task("Test task to complete")
        
    
        complete_task(task_id)
        
    
        tasks = show_tasks()
        completed_task = next(task for task in tasks if task['id'] == task_id)
        self.assertTrue(completed_task['completed'])

if __name__ == '__main__':
    unittest.main()