from flask import Flask

# 1. korak - kreiranje Flask web aplikacije
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Dobro dosli u Flask web demo aplikaciju.</h1>'


@app.route('/about-us')
def about_us():
    return '<h2>About us u Flask web demo aplikaciji.</h2>'


if __name__ == '__main__':
    app.run(debug=True)
