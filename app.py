from flask import Flask
app = Flask(__name__)

app.config["SECRET_KEY"] = "kasjhdfklsdajhfksla"

@app.route('/')
def hello_world():
    return 'Hello, World test!'

if __name__ == '__main__':
    app.run(debug=True)

