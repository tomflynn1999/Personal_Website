from flask import Flask, render_template, request

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


@app.route('/compound', methods=['GET', 'POST'])
def compound():
    result = None
    if request.method == 'POST':
        result = calculate_compound_interest(
            p=int(request.form['principal']),
            i=float(request.form['interest']),
            t=int(request.form['times_per_year']),
            n=int(request.form['years'])
        )
    return render_template('form.html', result=result)


def compound_interest(principal, rate, time, amount):

    """
    Computes Compound Interest
    :param principal:
    :param rate:
    :param time:
    :param amount:
    :return:
    """
    formula = principal*((1.0 + (rate/100)/amount)**(time*amount))  # compound interest formula
    return formula


def calculate_compound_interest(p: int, i: float, t: int, n: int):
    """
    Calculate compound interest.

    :param p: The principal investment amount.
    :param i: The annual interest rate (decimal form).
    :param t: Number of years the money is invested for.
    :param n: Number of times that interest is compounded per year.
    :return: The future value of the investment.
    """
    return p * ((1 + ((i / 100) / t)) ** (n * t))


if __name__ == '__main__':
    app.run(debug=True)
