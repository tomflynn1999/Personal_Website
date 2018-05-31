from flask import Flask, render_template

app = Flask(__name__)


@app.route('/personal_website')
def personal_website():
    return render_template('base.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
