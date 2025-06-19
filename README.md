# task-cli
A simple command line tool to create and manage a todo list

https://roadmap.sh/projects/task-tracker

## Features
- Creating tasks, updating their status and deleting them
- Listing all tasks or tasks with a certain status
- Tracking last update date on tasks

## Installation
### Prerequisites
- Python 3.7+

### Install
1. Clone the repo:
git clone https://github.com/MantyckiMateusz/task-cli

## Usage
### Add tasks
```
python task-cli.py add "task description"
```
Output:
```
Task created successfully (ID: 1)
```

### Update tasks

#### Mark as in progress
```
python task-cli.py mark-in-progress taskId
```
#### Mark as done
```
python task-cli.py mark-done taskId
```

### List tasks
```
python task-cli.py list state
```

**state** - if not provided defaults to showing all tasks. Allowed values are:
- all
- todo
- in-progress
- done

Example output:
```
*******************************
Id: 1
description: Example task
status: todo
createdAt: 2025-06-19 17:58:16
updatedAt: 2025-06-19 17:58:16
*******************************
```

### Delete tasks

```
python task-cli.py delete taskId
```

### Show the list of available commands

```
python task-cli.py help
```

## License
MIT © Mateusz Mantycki