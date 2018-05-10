import sqlite3

def create_db():
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    create_table = """create table if not exists todo(
                id integer primary key autoincrement,
                what text not null,
                due text not null,
                finished integer default 0)"""
    cur.execute(create_table)
    conn.commit()
    conn.close()

def run_program():
    while True:
        print("Choose what to do:")
        selection = input("(a: Add todo, l: List todo, m: Modify todo, q: Quit)? ")
        print()
        if selection == 'a':
            add_todo()
            print()
        elif selection == 'l':
            list_todo()
            print()
        elif selection == 'm':
            modify_todo()
            print()
        elif selection == 'q':
            break

def add_todo():
    what = input("Todo? ")
    due = input("Due date? ")
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute("insert into todo (what, due) values (?, ?)", (what, due,))
    conn.commit()
    conn.close()

def list_todo():
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute("select * from todo where 1")
    rows = cur.fetchall()
    for row in rows:
        print(row[0], row[1], row[2], row[3])
    conn.close()

def modify_todo():
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute("select * from todo where 1")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    index = input("Record id? ")
    what = input("Todo? ")
    due = input("Due date? ")
    finished = input("Finished (1: yes, 2: no)? ")
    cur.execute("update todo set what = ?, due = ?, finished = ? where id = ?", (what, due, finished, index,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
    run_program()