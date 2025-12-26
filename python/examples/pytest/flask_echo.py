from flask import Flask, request, render_template_string
eapp = Flask(__name__)

@eapp.route("/")
def hello():
    return '''
<form action="/echo" method="GET">
<input name="text">
<input type="submit" value="Echo">
</form>
'''

@eapp.route("/echo")
def echo():
    answer = request.args.get('text')
    if answer:
        return render_template_string("You said: {{ answer }}", answer=answer)
    else:
        return "Nothing to say?"


if __name__ == "__main__":
    eapp.run()
