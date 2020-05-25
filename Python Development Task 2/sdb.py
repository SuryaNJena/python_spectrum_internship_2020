import tkinter as tk
import sqlite3


def gui1():
    w = tk.Tk()
    l1 = tk.Label(w, text="Username", font="Ariel")
    l1.grid(row=1, column=1, padx=10, pady=5)
    u = tk.Entry(w)
    u.grid(row=1, column=2, padx=10, pady=5)
    l2 = tk.Label(w, text="Password", font="Ariel")
    l2.grid(row=2, column=1, padx=10, pady=5)
    p = tk.Entry(w)
    p.grid(row=2, column=2, padx=10, pady=5)
    cl.execute('''SELECT * FROM LOGIN''')
    rec = cl.fetchone()

    def ch_log():
        if (rec is not None) and (rec is not None):
            if rec[0] == u.get() and rec[1] == p.get():
                w.destroy()
                gui2()

            else:
                text = tk.Text(w)
                text.grid(row=4, column=2, padx=10, pady=10)
                text.insert(tk.INSERT, "Invalid username or password\n"
                                       "see code main block for default username password")
        else:
            text = tk.Text(w)
            text.grid(row=4, column=4)
            text.insert(tk.INSERT, "Invalid username or password\n"
                                   "see code main block for default username password")

    b = tk.Button(w, text="Submit", font="Consolas", command=ch_log)
    b.grid(row=3, column=3, padx=10, pady=5)
    w.title("StudentDB Login")
    w.mainloop()


def gui2():
    w2 = tk.Tk()
    w2.title("Student Data Entry")
    l1 = tk.Label(w2, text="Name", font="Ariel")
    l1.grid(row=1, column=1, padx=10, pady=5)
    n = tk.Entry(w2)
    n.grid(row=1, column=2, padx=10, pady=5)
    l2 = tk.Label(w2, text="Branch", font="Ariel")
    l2.grid(row=2, column=1, padx=10, pady=5)
    b = tk.Entry(w2)
    b.grid(row=2, column=2, padx=10, pady=5)
    l3 = tk.Label(w2, text="Registration ID", font="Ariel")
    l3.grid(row=3, column=1, padx=10, pady=5)
    r = tk.Entry(w2)
    r.grid(row=3, column=2, padx=10, pady=5)

    def act():
        temp = r.get()
        global mid
        mid = int(temp)
        cmd = """INSERT INTO STUDENTS(NAME,BRANCH,ID,SUBJECT1,SUBJECT2,SUBJECT3) VALUES (?,?,?,?,?,?)"""
        dt = (n.get(), b.get(), mid, 0, 0, 0)
        cs.execute(cmd, dt)
        w2.destroy()
        gui3()

    bu = tk.Button(w2, text="Submit", font="Consolas", command=act)
    bu.grid(row=2, column=3, padx=10, pady=5)
    w2.mainloop()


def gui3():
    w3 = tk.Tk()
    w3.title("Subject Data Entry")
    l1 = tk.Label(w3, text="Subject 1", font="Ariel")
    l1.grid(row=1, column=1, padx=10, pady=5)
    s1 = tk.Entry(w3)
    s1.grid(row=1, column=2, padx=10, pady=5)
    l2 = tk.Label(w3, text="Subject 2", font="Ariel")
    l2.grid(row=2, column=1, padx=10, pady=5)
    s2 = tk.Entry(w3)
    s2.grid(row=2, column=2, padx=10, pady=5)
    l3 = tk.Label(w3, text="Subject 3", font="Ariel")
    l3.grid(row=3, column=1, padx=10, pady=5)
    s3 = tk.Entry(w3)
    s3.grid(row=3, column=2, padx=10, pady=5)

    def at():
        global sam
        sam = int(s1.get()) + int(s2.get()) + int(s3.get())
        cs.execute('''UPDATE STUDENTS SET SUBJECT1=?,SUBJECT2=?,SUBJECT3=? 
                      WHERE ID=?''', (int(s1.get()), int(s2.get()), int(s3.get()), mid))
        w3.destroy()
        gui4()

        s.commit()

    but = tk.Button(w3, text="Submit", font="Consolas", command=at)
    but.grid(row=4, column=3, padx=10, pady=5)
    w3.mainloop()


def gui4():
    w4 = tk.Tk()
    w4.title("Choose")
    c = ((sam / 300) * 100) / 9.5
    if c < 6.5:
        g = "D"
    elif c < 7.5:
        g = "B"
    elif c < 8.5:
        g = "A"
    elif c < 9.5:
        g = "E"
    else:
        g = "O"

    def grade():
        text = tk.Text(w4)
        text.grid(row=4, column=2, padx=10, pady=10)
        text.insert(tk.INSERT, g)

    def cgpa():
        text = tk.Text(w4)
        text.grid(row=4, column=2, padx=10, pady=10)
        text.insert(tk.INSERT, str(c))

    bu1 = tk.Button(w4, text="CGPA", font="Consolas", command=cgpa)
    bu1.grid(row=2, column=1, padx=20, pady=15)
    bu2 = tk.Button(w4, text="GRADE", font="Consolas", command=grade)
    bu2.grid(row=2, column=2, padx=20, pady=15)
    bu3 = tk.Button(w4, text="NEW INPUT", font="Consolas", command=gui1)
    bu3.grid(row=3, column=1, padx=20, pady=15)
    bu4 = tk.Button(w4, text="CLOSE", font="Consolas", command=w4.destroy)
    bu4.grid(row=3, column=2, padx=20, pady=15)
    w4.mainloop()


if __name__ == "__main__":
    s = sqlite3.connect('Student.db')
    login = sqlite3.connect('Secure.db')
    s.execute('''CREATE TABLE IF NOT EXISTS STUDENTS(ID INTEGER PRIMARY KEY,
                NAME  TEXT NOT NULL,
                BRANCH TEXT NOT NULL,
                SUBJECT1 INTEGER,
                SUBJECT2 INTEGER,
                SUBJECT3 INTEGER);''')
    login.execute('''CREATE TABLE IF NOT EXISTS LOGIN(USERNAME TEXT PRIMARY KEY NOT NULL,
                     PASSWORD TEXT NOT NULL);''')

    cs = s.cursor()
    cl = login.cursor()
    try:
        cl.execute('''INSERT INTO LOGIN(USERNAME,PASSWORD) VALUES ("admin","admin")''')
    except sqlite3.IntegrityError:
        pass
    gui1()
    s.commit()
    mid = 0
    sam = 0
    login.commit()
