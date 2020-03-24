from flask import Flask, session, redirect, url_for, request
from markupsafe import escape
from game import Game

app = Flask(__name__)

# secret key is required to handle session. Create your own 'secrets' file at root of project and read from it.
sec_key = open('secrets', 'rb').read()
app.secret_key = sec_key

game = Game()


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'


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
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
