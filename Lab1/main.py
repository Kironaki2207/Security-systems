import sqlite3 as sql
import os


def authorizate(cur):
    ADMIN = 777
    USER = 100
    login = input("Login : ")
    passwd = input("Passwd : ")
    statement = f"SELECT * from users WHERE username='{login}' AND Password = '{passwd}';"
    cur.execute(statement)
    res = cur.fetchone()
    if not res:
        print("Login failed")
        exit(0)
    else:
        login, _, permition = res
        print(f"Welcome {login}")
        if permition == 1:
                os.system(f"chmod {ADMIN} file_system")
        else:
            os.system(f"chmod {USER} file_system")
        os.chdir("file_system")
        while True:
            com = input(f"{login}: ")
            if com.lower() == "exit":
                break
            os.system(com)


if __name__ == "__main__":
    con = sql.connect("my.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS "users" (
    "username"  TEXT,
    "password"  TEXT,
    "perm" INTEGER
);""")
    cur.execute("""INSERT INTO "users" VALUES ('admin','password','1');""")
    cur.execute("""INSERT INTO "users" VALUES ('user','123','0');""")
    con.commit()
    authorizate(cur)
