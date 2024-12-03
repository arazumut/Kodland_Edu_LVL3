from database import execute_query

def add_task(description):
    execute_query("INSERT INTO tasks (description) VALUES (?)", (description,))
    return "Görev başarıyla eklendi."

def delete_task(task_id):
    
    execute_query("DELETE FROM tasks WHERE id = ?", (task_id,))
    return "Görev başarıyla silindi."

def show_tasks():
    tasks = execute_query("SELECT id, description, completed FROM tasks")
    if not tasks:
        return "Hiç görev yok."
    return "\n".join([f"{task[0]} - {task[1]} ({'Tamamlandı' if task[2] else 'Tamamlanmadı'})" for task in tasks])

def complete_task(task_id):
    execute_query("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    return "Görev tamamlandı olarak işaretlendi."
