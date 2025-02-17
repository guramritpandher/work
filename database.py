import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="King#123",
    database="my_database"
)

cursor = conn.cursor()

#To create database 
'''cursor.execute("CREATE DATABASE my_database")
print("Created New One!!")'''


'''To create table'''
# cursor.execute("""
# CREATE TABLE if not exists users (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     email VARCHAR(100) UNIQUE NOT NULL,
#     password VARCHAR(255) NOT NULL,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
# """)

'''Insert Data'''
# sql="INSERT into users(name,email,password) Values(%s,%s,%s)"
# values=[
# ("Michel","mic@example.com","pass6"),
# ("Gami","gami@example.com","pass7"),
# ("Kat","kat@gmail.com", "pass8"),
# ("Ishman","ish@example.com","pass9")
# ]
# cursor.executemany(sql,values)

'''To fetch all data'''
# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

'''To fetch single row:'''
# cursor.execute("SELECT * FROM users where id=5")
# row=cursor.fetchone()
# print(row)

'''Updating data'''
# sql = "UPDATE users SET email = %s WHERE id = 4"
# values = ("newemail@example.com",)

# cursor.execute(sql, values)

'''Deleting Data'''
# sql="DELETE from users where id =5"
# cursor.execute(sql)

'''Order: to sort ascending or descending'''
# cursor.execute("SELECT * FROM users ORDER BY name DESC;")
# row=cursor.fetchall()
# print(row)

'''CONSTRAINTS:'''
'''Primary Key'''
# CREATE TABLE users (
#     id INT AUTO_INCREMENT PRIMARY KEY, 
#     name VARCHAR(100) NOT NULL,
#     email VARCHAR(100) UNIQUE NOT NULL 
# );

'''UNIQUE:Ensures no duplicate values in a column.'''
# CREATE TABLE employees (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     email VARCHAR(100) UNIQUE  -- No two employees can have the same email
# );

'''Not Null:Prevents null (empty) values in a column.'''
# CREATE TABLE products (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,  -- Must have a value
#     price DECIMAL(10,2) NOT NULL
# );

'''Deafault:Assigns a default value if no value is provided.'''
# CREATE TABLE orders (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     status VARCHAR(20) NOT NULL DEFAULT 'pending'  -- Default status is "pending"
# );

'''Check:Ensures values meet a condition'''
# CREATE TABLE students (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     age INT CHECK (age >= 18)  -- Ensures age is 18 or above
# );

'''Foreign Key:A foreign key links two tables and ensures referential integrity.'''
# CREATE TABLE orders (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     user_id INT,
#     product VARCHAR(100),
#     amount DECIMAL(10,2),
#     FOREIGN KEY (user_id) REFERENCES users(id)  -- Foreign key linking to users(id)
# );

'''Exception Handlig in database:'''
'''Handling Database Connection Errors:'''
# import mysql.connector

# try:
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="wrongpassword",  # Incorrect password
#         database="my_database"
#     )
#     print("Connected successfully!")

# except mysql.connector.Error as err:
#     print(f"Error: {err}")

'''Handling SQL Query Errors'''
# try:
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FORM users")  # Mistyped "FROM"
#     result = cursor.fetchall()
#     print(result)

# except mysql.connector.Error as err:
#     print(f"SQL Error: {err}")

'''COMMIT & ROLLBACK'''
# import mysql.connector

# try:
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="yourpassword",
#         database="my_database"
#     )
#     cursor = conn.cursor()

#     # Start transaction
#     conn.start_transaction()

#     cursor.execute("UPDATE users SET email = 'newemail@example.com' WHERE id = 1")
#     cursor.execute("DELETE FROM orders WHERE user_id = 1")

#     # If everything is successful, commit changes
#     conn.commit()
#     print("Transaction committed successfully!")

# except mysql.connector.Error as err:
#     print(f"Error: {err}")
#     conn.rollback()  # Undo changes if there's an error
#     print("Transaction rolled back!")

# finally:
#     cursor.close()
#     conn.close()


# try:
#     conn.start_transaction()
    
#     cursor.execute("UPDATE users SET email = 'test@example.com' WHERE id = 1")
#     cursor.execute("DELETE FROM orders WHERE user_id = 99")  # Error (User 99 doesn't exist)

#     conn.commit()  # This won't run if there's an error

# except mysql.connector.Error as err:
#     print(f"Error: {err}")
#     conn.rollback()  # Undo previous queries
#     print("Transaction rolled back!")

# finally:
#     cursor.close()
#     conn.close()



# conn.commit()
conn.close()