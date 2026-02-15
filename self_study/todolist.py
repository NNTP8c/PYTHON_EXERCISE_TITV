import json
from datetime import datetime

def save_tasks(tasks):
    with open('tasks.json','w',encoding='utf8') as f:
        json.dump(tasks,f,indent=4)

def load_tasks():
    try:
        with open('tasks.json','r',encoding='utf8') as f:
            return json.load(f)
    except FileNotFoundError:
        print('Không tìm thấy file tasks.json')
        return []

def add_tasks(tasks,task_name,due_date):
    task = {
        'task_name' : task_name,
        'status' : 'Chưa hoàn thành',
        'due_date' : due_date
    }
    tasks.append(task)
    save_tasks(tasks)

def display_all_tasks(tasks):
    for id,task in enumerate(tasks,1):
        print(f'{id}.{task["task_name"]} - Trạng thái: {task["status"]} - Hạn cuối:{task["due_date"]}')

def mark_completed_task(tasks,index):
    if 0<= index < len(tasks):
        tasks[index]['status'] = 'Hoàn thành'
    else:
        print('Không tìm thấy công việc!')

def delete_completed_task(tasks):
    tasks = [task for task in tasks if task['status'] != 'Hoàn thành']
    save_tasks(tasks)
    return tasks

def sort_tasks_by_due_date(tasks):
    tasks.sort(key = lambda task:datetime.strptime(task['due_date'], '%d/%m/%Y'))
    save_tasks(tasks)

def run():
    tasks = load_tasks()
    while True:
        print('\nỨng dụng quản lý công việc')
        print('1. Thêm công việc mới')
        print('2. Hiển thị tất cá công việc')
        print('3. Đánh dấu hoàn thành công việc ')
        print('4. Xóa công việc đã hoàn thành')
        print('5. Sắp xếp theo ngày')
        print('6. Thoát và lưu')

        choice = input('Lựa chọn: ')
        
        if choice == '1':
            name = input('\nNhập tên công việc: ')
            due_date = input('Nhập ngày hạn cuối: ')
            add_tasks(tasks,name,due_date)
        elif choice == '2':
            display_all_tasks(tasks)
        elif choice == '3':
            display_all_tasks(tasks)
            index = int(input('\nNhập vị trí muốn đánh dấu hoàn thành: ')) - 1
            mark_completed_task(tasks,index)
        elif choice == '4':
            tasks = delete_completed_task(tasks)
        elif choice == '5':
            sort_tasks_by_due_date(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print('\nĐã lưu và thoát!')
            break
        else:
            print('Lựa chọn không đúng: ')

if __name__ == '__main__':
    run()