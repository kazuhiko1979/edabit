from bottle import jinja2_template as template
from bottle import TEMPLATE_PATH, Bottle, route, run
from bottle import static_file

app = Bottle()
TEMPLATE_PATH.append("./template")


@app.route('/static/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='static/css')


@app.route("/")
@app.route("/<name>")
def register(name=""):

    return template('register.html', name=name)

def main():

    run(app=app,
        host="localhost",
        port=5000,
        debug=True,
        reloader=True)



    return


if __name__ == "__main__":
    main()