from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return '''<form action="/goto" method="POST">
            <input name="username">
            <input type="submit" value="Go">
        </form>'''

@app.route('/goto', methods=['POST'])
def login_post():
    username = request.form.get('username')
    if username is None or username == '':
        return redirect(url_for('user_page_central'))
    return redirect(url_for('user_page', name = username))

@app.route('/user/')
def user_page_central():
    return 'List of users'

@app.route('/user/<name>')
def user_page(name):
    return render_template_string('Page of {{ name }}', name=name)
