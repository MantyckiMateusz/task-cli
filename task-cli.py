from datetime import datetime
import json
import sys

def get_current_tasks() -> dict:
    try:
        with open("tasks.json", 'r', encoding="utf-8") as file:
            data = json.loads(file.read())
    except FileNotFoundError:
        data = {}
    return data

def save_changes(data: dict):
    with open("tasks.json", 'w') as file:
        json.dump(data, file)
    
def add_task(task: str) -> int:
    data = get_current_tasks() 
    task_id = get_index(data) 
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data[task_id] = {
        'description': task,
        'status': 'todo',
        'createdAt': current_date,
        'updatedAt': current_date
    }
    
    save_changes(data)
    return task_id

def delete_task(task_id: str):
    data = get_current_tasks()
    try:
        del data[task_id]
    except KeyError:
        print(f"Task with the specified id doesn't exist (ID: {task_id})")
    else:
        print("Successfully deleted task")
    
    save_changes(data)

def update_task(task_id: str, state: str):
    data = get_current_tasks()
    try:
        if state == 'in_progress':
            data[task_id]["status"] = 'in-progress'
        elif state == 'done':
            data[task_id]["status"] = 'done'
        else:
            raise ValueError('Incorrect value for the state attribute. Allowed states: [in-progress, done]')
        data[task_id]['updatedAt'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    except KeyError:
        print(f"Task with the specified id doesn't exist (ID: {task_id})")
    else:
        save_changes(data)
        print("Successfully updated task")
        
def list_tasks(state: str = "all"):
    data = get_current_tasks()
    if state in ['todo', 'in-progress', 'done']:
        #Filter the data to show only the tasks where status field matches the state property passed to the function
        filtered_data = {taskId:task for taskId, task in data.items() if task["status"] == state}
        display_tasks(filtered_data)
    elif state == "all":
        display_tasks(data)
    else:
        raise ValueError('Incorrect value for the state attribute. Allowed states: [all, todo, in-progress, done]')
        
def display_tasks(data: dict):
    if not data:
        print('No tasks to show!')
        return
    
    separator = '*******************************'
    for taskId, task in data.items():
        print(separator)
        print(f'Id: {taskId}')
        for key, value in task.items():
            print(f'{key}: {value}')
        print(separator)
        
def get_index(data) -> int:
    #Get first free id number in the task list
    i = 1
    while str(i) in data.keys():
        i+=1
    return i

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ValueError('Action not specified')
    
    match str.lower(sys.argv[1]):
        case 'add':
            task_id = add_task(sys.argv[2])
            print(f'Task created successfully (ID: {task_id})')
        case 'delete':
            task_id = sys.argv[2]
            delete_task(task_id)
        case 'mark-in-progress':
            task_id = sys.argv[2]
            update_task(task_id, 'in_progress')
        case 'mark-done':
            task_id = sys.argv[2]
            update_task(task_id, 'done')
        case 'list':
            if len(sys.argv) == 2:
                list_tasks()
            else:
                try:
                    list_tasks(sys.argv[2])
                except ValueError as err:
                    print(err)
        case 'help':
            print("""
                  Possible options:
                    add "task description" 
                        - adds a task with specified description, return the ID of created task
                    delete taskId 
                        - deletes the task with specified ID number
                    mark-in-progress taskId 
                        - marks the task with specified ID number as in progress
                    mark-done taskId 
                        - marks the task with specified ID number as done
                    list state 
                        - shows the list of tasks with specified *state*, if not specified then state defaults to all
                            supported states:
                                all - shows all existing tasks
                                todo - shows all tasks that are currently marked as to do
                                in-progress - shows all tasks that are currently marked as in progress
                                done - shows all tasks that are currently marked as done
                    help 
                        - shows the list of possible options
                  """)
        case _:
            print("Incorrect action. Use \"python task-cli help\" for possible options")
            
        
        