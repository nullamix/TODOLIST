# ToDo List CLI with PostgreSQL & Python

This is a simple command-line ToDo list manager built with Python and PostgreSQL.

## Prerequisites

Before running the application, make sure you have the following:

-   Python 3.x installed
-   PostgreSQL database server installed and running
-   `psycopg2` library installed (`pip install psycopg2`)

## Setup

1.  **Database Setup**:
    *   Create a PostgreSQL database named `todolist`.
    *   Create a user `uni` with password `321` and grant it necessary privileges to access the `todolist` database.

    ```sql
    CREATE DATABASE todolist;
    CREATE USER uni WITH PASSWORD '321';
    GRANT ALL PRIVILEGES ON DATABASE todolist TO uni;
    ```

2.  **Table Setup**:
    *   Create a table named `list` with columns `id` (SERIAL PRIMARY KEY), `todo` (TEXT), and `status_of_todo` (BOOLEAN).

    ```sql
    \c todolist;

    CREATE TABLE list (
    id SERIAL PRIMARY KEY,
    todo VARCHAR(200) NOT NULL,
    status_of_todo BOOLEAN
    );
    ```

3.  **Install `psycopg2`**:

    ```bash
    pip install psycopg2
    ```

## Usage

1.  **Save the Code**:
    *   Save the provided code in a file (e.g., `db_todo.py`).

2.  **Run the Application**:

    ```bash
    python db_todo.py
    ```

3.  **Interaction**:
    *   The application will display a menu with options to display tasks, mark a task as done, add a task, update a task, or delete a task.
    *   Follow the prompts to interact with the to-do list.

