from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    context = {'title': 'main',
               }
    return render_template('base.html', **context)


@app.route('/clothes/')
def clothes():
    context = {'title': 'clothes',
               }
    return render_template('clothes.html', **context)


@app.route('/card/')
def card():
    context = {'title': 'card',
               }
    return render_template('card.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'title': 'shoes',
               }
    return render_template('shoes.html', **context)


@app.route('/accessories/')
def accessories():
    context = {'title': 'accessories',
               }
    return render_template('accessories.html', **context)


if __name__ == '__main__':
    app.run()
