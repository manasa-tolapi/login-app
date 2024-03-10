from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/")
def start():
    if session.get('is_loggedin', False):
        name = session.get('username', 'User')
        print(session)
        return render_template('home.html', name=name)
    return render_template('login.html')


# @app.route('/home')
# def home_page():
#     return render_template('home.html')
#     # return 'Welcome ' + email


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        email = request.form.get('email', None)
        password = request.form.get('password', None)
        if email and password:
            # check with database values
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('select id, email, username, password from users where email=? and password=?', (email, password))
            user = cursor.fetchone()
            print(user, '...user')
            if user:
                session['is_loggedin'] = True
                session['id'] = user[0]
                session['username'] = user[2]
                # return render_template('home.html')
                return redirect('/')
                # return redirect(url_for('home_page'))
            else:
                print('Either Email or pasword are wrong')
        else:
            print('Either Email or pasword are None')
    return render_template('login.html')


@app.route('/register', methods=["POST", "GET"])
def register():
    # print(request.form, type(request.form))
    if request.method == 'POST':
        email=request.form.get('email')
        password=request.form.get('password')
        username=request.form.get('username')
        print(email, password, username)

        # save user data to database
        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (username, email, password)
                VALUES (?, ?, ?)
            ''', (username, email, password))
            user_id = cursor.lastrowid
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("SQLite error:", e)

        print('inserted at : ', user_id)

        return redirect('/home')
    return render_template('register.html')


@app.route("/update", methods=["POST", "GET"])
def update():
    user_id = session.get('id', None)
    if user_id:
        if request.method == "POST":
            print(request.form)
            email = request.form.get('email')
            password = request.form.get('password')
            username = request.form.get('username')

            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('update users set username = ?, email = ?, password = ? where id = ?', (
                username, email,password, user_id
            ))

            conn.commit()
            conn.close()

            return redirect("/")

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('select username, email, password from users where id = ?', (str(user_id)))
        user = cursor.fetchone()

        conn.commit()
        conn.close()
        return render_template('update.html', user_data=user)
    return 'User not loggedIn'


@app.route('/logout')
def logout():
    session.clear()
    return redirect("/login")




# if not using `flask run --debug` : run with `python app.py` & uncomment below code
# if __name__ == '__main__':
#     app.run(debug=True)
