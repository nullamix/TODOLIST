import psycopg2

conn = psycopg2.connect(
    dbname="todolist",
    user="uni",
    password="321",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()


def displayer():
    cursor.execute("SELECT todo, status_of_todo FROM list")
    todos = cursor.fetchall()

    for todo, status in todos:
        convTF = "done" if status else (
            "not marked" if status is None else "to do")
        print(f"{todo} : {convTF}")


def marking():
    todo = input("enter the todo: ")
    isdone = input("is it done? (yes/no): ").lower()

    status = True if isdone == "yes" else False

    cursor.execute("SELECT id FROM list WHERE todo = %s", (todo,))
    exists = cursor.fetchone()

    if exists:
        cursor.execute(
            "UPDATE list SET status_of_todo = %s WHERE todo = %s",
            (status, todo)
        )
    else:
        cursor.execute(
            "INSERT INTO list (todo, status_of_todo) VALUES (%s, %s)",
            (todo, status)
        )

    conn.commit()


def add_task():
    task = input("enter content of your task:")
    cursor.execute(
        "INSERT INTO list (todo, status_of_todo) VALUES (%s, %s)",
        (task, None)
    )
    conn.commit()


def update_task():
    task = input("enter content of your task:")
    isdone = input("is it done? (yes/no): ").lower()
    status = True if isdone == "yes" else False
    cursor.execute("SELECT id FROM list WHERE todo = %s", (task,))
    exists = cursor.fetchone()

    if exists:
        cursor.execute(
            "UPDATE list SET status_of_todo = %s WHERE todo = %s",
            (status, task)
        )
    else:
        add_task(task)

    conn.commit()


def delete_task():
    task = input("wich task you want to delete?")
    cursor.execute("DELETE FROM list WHERE todo = %s", (task,))
    if cursor.rowcount == 0:
        print("Not found!")
    conn.commit()


def inputGetter():
    caller = input("welcome!\nhow can I help you?\n"
                   "1)display tasks \n2)mark a task\n"
                   "3)add a task\n4)updatea a task\n"
                   "5)delete a task\n")
    while (True):
        try:
            caller = int(caller)
            if (not (0 < caller < 6)):
                caller = input("wrong input; try again :")
            else:
                return (caller)
        except:
            caller = input("wrong input; try again :")


def doer():
    caller = inputGetter()
    if (caller == 1):
        displayer()
    elif (caller == 2):
        marking()
    elif (caller == 3):
        add_task()
    elif (caller == 4):
        update_task()
    elif (caller == 5):
        delete_task()
    isdone = input("you want to do something else? (yes/no)").lower()
    if (isdone == "yes"):
        doer()
    else:
        exit()


doer()

cursor.close()
conn.close()