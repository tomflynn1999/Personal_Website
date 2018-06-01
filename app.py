from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def personal_website():
    return render_template({{url_for('base.html')}})


if __name__ == '__main__':
    app.run(debug=True)
