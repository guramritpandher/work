#JOINS: is used to combine rows from two or more tables, based on a related column between them.
import sqlite3

conn=sqlite3.connect("joinsdatabase.db")

cursor=conn.cursor()

# cursor.execute("""
# create table if not exists users(
#             id integer primary key autoincrement,
#             name text not null,
#             email text not null
#                )
# """)
"""Adding new column to existing table"""
# cursor.execute("""
# ALTER TABLE users
# ADD COLUMN email text;
# """)
"""ADDING VALUES"""
# cursor.execute("""INSERT INTO users (name, email) VALUES 
# ('Alice', 'alice@example.com'),
# ('Bob', 'bob@example.com'),
# ('Charlie', 'charlie@example.com')"""
# )
cursor.execute("""INSERT INTO users(name,email) VALUES
('Davin','davin@example.com')
""")

"""DELETING DUPLICATES"""
# cursor.execute("""
# DELETE FROM users
# WHERE rowid NOT IN (
#     SELECT MIN(rowid) 
#     FROM users 
#     GROUP BY name, email
# );
# """)


# cursor.execute("""
# CREATE TABLE orders (
#     order_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     user_id INTEGER,
#     product TEXT NOT NULL,
#     FOREIGN KEY (user_id) REFERENCES users(id)
# );
# """)
# cursor.execute("""
# INSERT INTO orders (user_id, product) VALUES 
# (1, 'Laptop'),
# (1, 'Mouse'),
# (2, 'Keyboard'),
# (3, 'Monitor'),
# (3, 'Headphones');
# """)
# cursor.execute("""
# DELETE FROM orders
# WHERE rowid NOT IN (
#     SELECT MIN(rowid) 
#     FROM orders 
#     GROUP BY user_id, product
# );
# """)

#INNER JOIN:
# cursor.execute("""
# SELECT users.name, orders.product 
# FROM users 
# INNER JOIN orders ON users.id = orders.user_id;
# """)
# for row in cursor.fetchall():
#     print(row[0],":",row[1])

#LEFT JOIN:
# cursor.execute("""
# SELECT users.name, orders.product 
# FROM users 
# LEFT JOIN orders ON users.id = orders.user_id;
# """)
# results = cursor.fetchall()

# for row in results:
#     print(row)

"""FULL JOIN"""
# cursor.execute("""
# SELECT users.name, orders.product 
# FROM users 
# LEFT JOIN orders ON users.id = orders.user_id

# UNION

# SELECT users.name, orders.product 
# FROM users 
# RIGHT JOIN orders ON users.id = orders.user_id;
# """)
# results=cursor.fetchall()
# for row in results:
#     print(row)


'''CROSS JOIN: If we want every user matched with every product (even if they didn’t order), we use CROSS JOIN'''
cursor.execute("""
SELECT users.name, orders.product 
FROM users 
CROSS JOIN orders;
""")
results=cursor.fetchall()
for row in results:
    print(row)


conn.commit()
conn.close()
