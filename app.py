from flask import Flask

app = Flask(__name__)


@app.route('/compound_interest')
def compound():
    ...


if __name__ == '__main__':
    app.run(debug=True)
