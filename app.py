from flask import Flask, session, redirect, url_for, request
from game import Game
from player import Player
import hashlib
import templates as t
# from markupsafe import escape

app = Flask(__name__)

# secret key is required to handle sessions.
# Create your own 'secrets' file at root of project and read from it.
sec_key = open('secrets', 'rb').read()
app.secret_key = sec_key

print(t.UNIVERSE_TITLE)

game = Game()
user_table = {}


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        if 'signup' in request.form:
            return redirect(url_for('signup'))
        elif 'login' in request.form:
            return redirect(url_for('login'))

    else:
        if session.get('username'):
            r_string = t.UNIVERSE_TITLE
            r_string += f"{session['username']} logged in."
            r_string += t.LOGOUT_LINK

            return r_string
        else:
            return f'''
            <h1>{t.UNIVERSE_TITLE}</h1>
            <div>
                <form method='post'>
                    {t.LOGIN_BUTTON}
                    {t.SIGNUP_BUTTON}
                </form>
            </div>
            '''


@app.route('/update')
def update():
    game.update()
    return 'Done!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        m = hashlib.sha3_256()
        m.update(username.encode('utf-8'))
        m.update(password.encode('utf-8'))

        if username in user_table:
            if user_table[username] == m.hexdigest():
                session['username'] = request.form['username']
                return redirect(url_for('index'))
        else:
            return 'FAILED LOGGING IN!'
    else:
        return '''
            <form method="post">
                <p><input type=text name=username>
                <p><input type="password" name="password"</p>
                <p><input type=submit value=Login>
            </form>
        '''


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return '''
        <form method="post">
            <p><input type="text" name="username"></p>
            <p><input type="password" name="password"</p>
            <p><input type="submit" value="Submit"></p>
        </form>
        '''
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        m = hashlib.sha3_256()
        m.update(username.encode('utf-8'))
        m.update(password.encode('utf-8'))
        user_table[username] = m.hexdigest()

        session["username"] = username
        p = Player(username=username)
        game.add_player(p)

        return f'''{request.form['username']}Done! <a href='/'>home!</a>'''


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
