import sqlite3

#connect database
conn=sqlite3.connect("mydatabase.db")

#cursor object to interact with database
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")

#to fetch all data
# cursor.execute("SELECT * from users") 

#to fetch particular column
cursor.execute("SELECT name FROM users")
users = cursor.fetchall()

#to select multiple columns together
cursor.execute("SELECT name, email FROM users")
data = cursor.fetchall()

for row in data:
    print(f"Name: {row[0]}, Email: {row[1]}")

#to select with a condition:
'''SELECT * FROM users WHERE age > 25;'''

#select a single record:
'''SELECT * FROM users WHERE name = 'Alice';'''

#order vise:
'''SELECT * FROM users ORDER BY age ASC;  -- Sort by age in ascending order
SELECT * FROM users ORDER BY age DESC; -- Sort by age in descending order
'''

#To limit result:
'''SELECT * FROM users LIMIT 3;  -- Get the first 3 users'''

# Count the Number of Users
# SELECT COUNT(*) FROM users;
# Find the Oldest and Youngest User

# SELECT MAX(age) FROM users; -- Oldest
# SELECT MIN(age) FROM users; -- Youngest
# Find the Average Age
# SELECT AVG(age) FROM users;

# Using LIKE for Pattern Matching
# Find Users Whose Names Start with 'A'

# SELECT * FROM users WHERE name LIKE 'A%';
# Find Users Whose Emails Contain 'gmail'

# SELECT * FROM users WHERE email LIKE '%gmail%';
# Using IN, BETWEEN, and EXISTS
# Select Users with Specific Ages

# SELECT * FROM users WHERE age IN (25, 30, 35);
# Select Users Between Two Ages

# SELECT * FROM users WHERE age BETWEEN 20 AND 30;
# Check If a User Exists

# SELECT EXISTS(SELECT 1 FROM users WHERE email = 'alice@example.com');

# Joining Two Tables
# Example: Creating a Second Table

# CREATE TABLE orders (
#     order_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     user_id INTEGER,
#     product TEXT,
#     FOREIGN KEY (user_id) REFERENCES users(id)
# );
# Inner Join to Get User Orders

# SELECT users.name, orders.product 
# FROM users 
# JOIN orders ON users.id = orders.user_id;

# Print the users
# for names in users:
#     print(names[0])

conn.commit()
#close the connection
conn.close() 