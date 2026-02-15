import json
from datetime import datetime

def save_tasks(tasks):
    with open('tasks.json','w',encoding='utf8') as f:
        f.dump(tasks,f,indent=4)

def load_tasks():
    try:
        with open('tasks.json','r',encoding='utf8') as f:
            return json.load(f)
    except FileNotFoundError:
        print('Không tìm thấy file tasks.json')

def add_tasks(tasks,task_name,due_date):
    task = {
        'task_name' : task_name,
        'status' : 'Chưa hoàn thành',
        'due_date' : due_date
    }
    tasks.append(task)
    return tasks

def display_all_tasks(tasks):
    print(tasks)

