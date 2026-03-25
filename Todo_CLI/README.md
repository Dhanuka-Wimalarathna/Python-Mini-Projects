# 📝 Task Tracker CLI

A simple command-line interface (CLI) application to track and manage your tasks. Built with Python — no external libraries required.

---

## 📋 Features

- ✅ Add new tasks
- ✏️ Update task status (`Todo`, `In Progress`, `Done`)
- 🗑️ Delete all tasks
- 📄 View all tasks in a formatted table

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your machine
- No external libraries needed

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/task-tracker-cli.git
   ```

2. Navigate to the project folder:
   ```bash
   cd task-tracker-cli
   ```

3. Run the application:
   ```bash
   python task.py
   ```

---

## 💻 Usage

When you run the application, you will see a menu:

```
 01. Add New Task
 02. Update Status of Selected Task
 03. Delete All Tasks
 04. View All Tasks
 05. Exit
```

### Adding a Task

Select option `1` and enter your task description:

```
Select one option: 1
Enter the task: Buy groceries
Task "Buy groceries" saved! (ID: 1)
```

### Updating a Task Status

Select option `2`, choose a task by ID, then select a new status:

```
Select one option: 2
Enter the task ID need to update: 1

 01. Todo
 02. In progress
 03. Done

Enter new status: 2
Task 1 updated successfully.
```

### Viewing All Tasks

Select option `4` to see all tasks in a table:

```
+-----+-------------------------+---------------+----------------------+----------------------+
| ID  | Description             | Status        | Created At           | Updated At           |
+-----+-------------------------+---------------+----------------------+----------------------+
| 1   | Buy groceries           | In progress   | 2026-03-24 10:30:00  | 2026-03-24 11:00:00  |
+-----+-------------------------+---------------+----------------------+----------------------+
| 2   | Write report            | Todo          | 2026-03-24 10:35:00  | 2026-03-24 10:35:00  |
+-----+-------------------------+---------------+----------------------+----------------------+
```

### Deleting All Tasks

Select option `3` and confirm with `Y`:

```
Select one option: 3
Are you sure you want to delete all tasks? (Y/N): Y
All Tasks are deleted.
```

---

## 🗂️ Task Properties

Each task stored in `TODOS.json` has the following properties:

| Property | Description |
|---|---|
| `id` | Unique identifier for the task |
| `description` | Short description of the task |
| `status` | Current status: `Todo`, `In progress`, or `Done` |
| `createdAt` | Date and time the task was created |
| `updatedAt` | Date and time the task was last updated |

### Example `TODOS.json`

```json
[
    {
        "id": 1,
        "description": "Buy groceries",
        "status": "In progress",
        "createdAt": "2026-03-24 10:30:00",
        "updatedAt": "2026-03-24 11:00:00"
    },
    {
        "id": 2,
        "description": "Write report",
        "status": "Todo",
        "createdAt": "2026-03-24 10:35:00",
        "updatedAt": "2026-03-24 10:35:00"
    }
]
```

---

## 📁 Project Structure

```
task-tracker-cli/
│
├── task.py        # Main application file
├── TODOS.json     # Auto-generated task storage file
└── README.md      # Project documentation
```

---

## ⚙️ How It Works

- Tasks are stored locally in a `TODOS.json` file
- The file is **automatically created** if it does not exist
- No database or internet connection is required
- Uses only Python's built-in `json`, `os`, and `datetime` modules

---

## 🛠️ Built With

- **Python 3** — Programming language
- **json** — Built-in module for reading/writing JSON
- **os** — Built-in module for file system operations
- **datetime** — Built-in module for timestamps

---

## 📌 Project Inspiration

This project is inspired by the [Task Tracker](https://roadmap.sh/projects/task-tracker) project on roadmap.sh.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
