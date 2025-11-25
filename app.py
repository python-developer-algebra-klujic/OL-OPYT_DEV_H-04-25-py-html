from flask import Flask

# 1. korak - kreiranje Flask web aplikacije
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Dobro dosli u Flask web demo aplikaciju.</h1>'


if __name__ == '__main__':
    app.run(debug=True)
