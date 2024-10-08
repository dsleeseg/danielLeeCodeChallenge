from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "This is a demo!"

@app.route('/healthCheck')
def healthCheck():
    return "App is Running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
