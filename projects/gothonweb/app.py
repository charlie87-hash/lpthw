
from flask import Flask

from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    greeting = "Hello word"
    return render_template("index.html", greeting=greeting) # with html
    #return f'Hello, {greeting}!' without html

if __name__ == "__main__":
    app.run()