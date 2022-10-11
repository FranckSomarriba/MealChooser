from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import randomizer

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@app.route('/home')
def home():
    return render_template('index.html', food=randomizer.food(), foodlist=randomizer.fastFoodDict, )


@app.route('/home')
def contact():
    if request.method == 'POST':
        if request.form['submit_button'] == 'What you want?':
            return "hello world"
        elif request.form['submit_button'] == 'Do Something Else':
            pass  # do something else
        else:
            pass  # unknown
    elif request.method == 'GET':
        return render_template('index.html', food=randomizer.food(), foodlist=randomizer.fastFoodDict)


@app.route('/about')
def about():
    return "This is the about page"


if __name__ == "__main__":
    app.run(debug=True)


    