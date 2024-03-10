# import sqlite3

# conn = sqlite3.connect('database.db')
# cursor = conn.cursor()

# # Create users table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT NOT NULL,
#         email TEXT NOT NULL,
#         password TEXT NOT NULL
#     )
# ''')
# conn.commit()

# # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# # existing_tables = cursor.fetchall()
# # conn.commit()
# # print(existing_tables)

# query = 'SELECT id, email, username, password FROM users'
# cursor.execute(query)
# users = cursor.fetchone()
# print(users)
# print(users[1])

# # Create users table
# # cursor.execute('''
# #     CREATE TABLE IF NOT EXISTS orders (
# #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         username TEXT NOT NULL,
# #         email TEXT NOT NULL,
# #         password TEXT NOT NULL
# #     )
# # ''')
# # conn.commit()

# conn.close()


wife = "Manasa"

husband = "Siva Prasad"

wife_extra = "Tolapi"

# wife = wife + " " + wife_extra

# wife = "MRs {} {}".format(wife, wife_extra)

# wife = "I am {0}, and {0} is good girl.".format(wife)

wife = f"Mrs {wife} {wife_extra}"

print(husband, wife)

