from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def personal_website():
    return render_template('base3.html')


@app.route('/about')
def about():
    return render_template('About_Me.html')


@app.route('/interests')
def interests():
    return render_template('Interests.html')


if __name__ == '__main__':
    app.run(debug=True)
