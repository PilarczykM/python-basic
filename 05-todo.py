import sqlite3

connection = sqlite3.connect("todo.db")


def create_table(db_connection):
    try:
        cur = db_connection.cursor()
        cur.execute("""CREATE TABLE task(task text)""")
    except:
        pass


def show_tasks(db_connection):
    cur = db_connection.cursor()
    cur.execute("""SELECT rowid, task FROM task""")
    result = cur.fetchall()

    for row in result:
        print(str(row[0]) + " - " + row[1])


def add_task(db_connection):
    print("Adding task")
    task = input("Enter the task text: ")
    if task == "0":
        print("Return to the menu")
    else:
        cur = db_connection.cursor()
        cur.execute("""INSERT INTO task(task) VALUES(?)""", (task,))
        db_connection.commit()
        print("Task added!")


def delete_task(db_connection):
    task_index = int(input("Enter the index of the job to be deleted: "))

    cur = db_connection.cursor()
    rows_deleted = cur.execute("""DELETE FROM task WHERE rowid=?""", (task_index,)).rowcount
    db_connection.commit()

    if rows_deleted == 0:
        print("Such a task does not exist!")
    else:
        print("Task deleted!")


create_table(connection)

while True:
    print()
    print("1. Show tasks")
    print("2. Add a task")
    print("3. Delete task")
    print("0. Exit")

    user_choice = int(input("Choose a number: "))
    print()

    if user_choice == 1:
        show_tasks(connection)

    if user_choice == 2:
        add_task(connection)

    if user_choice == 3:
        delete_task(connection)

    if user_choice == 0:
        break

connection.close()
