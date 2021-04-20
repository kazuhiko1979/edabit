from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def registration(name=""):

    html = render_template('register.html', name=name)
    return html


def main():

    app.debug = True
    app.run()
    return


if __name__ == '__main__':
    main()
