import sqlite3


def create_db():
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()
    create_table = """create table if not exists todo(
                id integer primary key autoincrement,
                what text not null,
                due text not null,
                finished integer)"""
    cur.execute(create_table)
    conn.close()


def run_program():
    create_db()
    while True:
        selection = input(
            "Choose what to to:\n(a: Add todo, l: List todo, m: Modify todo, q: Quit)? ")
        if selection == 'a':
            add_todo()
        elif selection == 'l':
            sub_selection = input(
                "What items are you looking at (a: All, f: Finished only)? ")
            if sub_selection == 'f':
                list_todo(filter_todo(sub_selection))
            elif sub_selection == 'a':
                list_todo(filter_todo(sub_selection))
        elif selection == 'm':
            modify_todo()
        elif selection == 'q':
            break


def filter_todo(filter):
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()
    sql = ""
    if filter == 'f':
        sql += "select * from todo where finished = 1"
    elif filter == 'a':
        sql += "select * from todo where 1"
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return rows


def add_todo():
    what = input("Todo? ")
    due = input("Due date? ")
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()
    cur.execute(
        "insert into todo (what, due, finished) values (?, ?, ?)", (what, due, 0,))
    conn.commit()
    conn.close()


def list_todo(data):
    print("ID  TODO   DATE   FINISHED?")
    print("---------------------------")
    for row in data:
        print(row[0], row[1], row[2], row[3])
    print()


def modify_todo():
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()
    cur.execute("select * from todo where 1")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    index = input("Record id? ")
    what = input("Todo? ")
    due = input("Due date? ")
    finished = input("Finished (1: yes, 2: no)? ")
    cur.execute("update todo set what = ?, due = ?, finished = ? where id = ?",
                (what, due, finished, index,))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    run_program()
    input_data_test()
