from flask import Flask

app=Flask(__name__)


@app.route('/')
def index():
    return 'Prueba'




if __name__ == '__main__':
    app = app.run(debug=True)