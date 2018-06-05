from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/hello/<string:name>")
def hello(name):
    return render_template(
        'test.html',name=name)

if __name__ == "__main__":
    application.run()
