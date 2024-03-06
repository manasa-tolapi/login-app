from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Database connection details
db_file = 'your_database.db'

# Route to fetch all users
@app.route('/get_users', methods=['GET'])
def get_users():
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        # Execute SQL query to select all columns from the users table
        cursor.execute("SELECT * FROM users")

        # Fetch all rows
        users = cursor.fetchall()

        # Close the database connection
        cursor.close()
        connection.close()

        # Return data in JSON format
        return jsonify(users)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        # Get user data from the request JSON
        # user_data = request.get_json()
        username = request.form.get('username')
        email = request.form.get('email')

        # Insert user data into the users table
        cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))

        # Commit changes and close the connection
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"message": "User added successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to delete an existing user
@app.route('/delete_user/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        # Delete user from the users table
        cursor.execute("DELETE FROM users WHERE id=?", (user_id,))

        # Commit changes and close the connection
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"message": f"User with ID {user_id} deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to update an existing user
# @app.route('/update_user/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     try:
#         # Connect to the SQLite database
#         connection = sqlite3.connect(db_file)
#         cursor = connection.cursor()

#         # Get user data from the request JSON
#         user_data = request.get_json()
#         new_username = user_data.get('username')
#         new_email = user_data.get('email')

#         # Update user data in the users table
#         cursor.execute("UPDATE users SET username=?, email=? WHERE id=?", (new_username, new_email, user_id))

#         # Commit changes and close the connection
#         connection.commit()
#         cursor.close()
#         connection.close()

#         return jsonify({"message": f"User with ID {user_id} updated successfully"}), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

