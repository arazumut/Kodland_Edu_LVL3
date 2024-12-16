import unittest
from commands import add_task, delete_task, show_tasks

class TestDeleteTask(unittest.TestCase):
    def test_delete_task(self):
    
        task_id = add_task("Test task to delete")
        

        delete_task(task_id)
        

        tasks = show_tasks()
        self.assertNotIn(task_id, [task['id'] for task in tasks])

if __name__ == '__main__':
    unittest.main()