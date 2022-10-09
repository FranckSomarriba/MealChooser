from flask import Flask, render_template, url_for
import randomizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mylink/')
def mylink():
    return randomizer.food

if __name__ == "__main__":
    app.run(debug=True)

    