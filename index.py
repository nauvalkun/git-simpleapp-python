from flask import Flask
app = Flask(__name__)
@app.route("/")
def helloworld():
    return "We Need Love"
if __name__ == "__main__":
    app.run()
