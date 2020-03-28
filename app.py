from flask import Flask, session, redirect, url_for, request
from game import Game
import hashlib
# from markupsafe import escape

app = Flask(__name__)

# secret key is required to handle sessions.
# Create your own 'secrets' file at root of project and read from it.
sec_key = open('secrets', 'rb').read()
app.secret_key = sec_key

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
        return '''
        <div>
            <form method='post'>
                <input type='submit' name='signup' value='Sign me up! '>
                <input type='submit' name='login' value='Log me in! '>
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
        session['username'] = request.form['username']
        return redirect(url_for('index'))
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

        return f'''{request.form['username']}Done!'''


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
