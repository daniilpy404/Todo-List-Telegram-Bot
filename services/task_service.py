from db.database import add_task, get_tasks, toggle_task, delete_task


def create_task(user_id, text):
    add_task(user_id, text)


def list_tasks(user_id):
    return get_tasks(user_id)


def complete_task(task_id):
    toggle_task(task_id)


def remove_task(task_id):
    delete_task(task_id)