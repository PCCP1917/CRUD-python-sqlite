import sqlite3

#Create conection to DB

conn= sqlite3.connect('database.db')
cursor= conn.cursor()

#Create table if not exist

cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT
                )
                """)
conn.commit()

#Create register ->C
def Create_User(name:str,email:str) -> str:
    cursor.execute('INSERT INTO users(name,email) VALUES(? , ?)', (name,email))
    conn.commit()
    return "Usuario Agregado"

#Read register ->R
def Read_Users()->list:
    cursor.execute('SELECT id, name, email FROM users')
    users= cursor.fetchall()
    users_list=[]
    for user in users:
        users_list.append(user)
    return users_list

#Read register by id ->R
def Read_unique_user(id:int)->str:
    cursor.execute('SELECT id, name, email FROM users WHERE id=?',(id,))
    user= cursor.fetchone()
    if user:
        return user
    return "User not found"

#Update User by id ->U
def Update_User(id:int,name:str,email:str)->str:
    cursor.execute('UPDATE users SET name=?,email=? WHERE id=?',(name,email,id))
    conn.commit()
    return "Usuario Actualizado"

#Delete User by id
def Delete_User(id:int)->str:
    cursor.execute('DELETE FROM users WHERE id= ? ',(id,))
    conn.commit()
    return "Usuario Eliminado"

#Script
#Create User

#Create_User("Martin","martin_prince@example.com")
#Create_User("Tony","tony_blair@example.com")
#Create_User("Joseph","joseph_joestar@example.com")

#Print Users
#print(Read_Users())

#Print unique user
#print(Read_unique_user(3))

#Update user
#print(Update_User(3,"Lisa","Simpson"))

#Delete User
#print(Delete_User(5))