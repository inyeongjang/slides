from flask import Flask, request, render_template_string
app = Flask(__name__)

VERSION = "1.00"

@app.route("/")
def main():
    return f'''
     VERSION {VERSION}<br>
     <form action="/echo" method="GET">
         <input name="text">
         <input type="submit" value="Echo">
     </form>
     '''

@app.route("/echo")
def echo():
    user_input = request.args.get('text', '')
    return render_template_string("You said: {{ user_input }}", user_input=user_input)
