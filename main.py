from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return "<h2>Please enter your name in the URL</h2>"

@app.route("/<name>")
def guess(name):
    gender_guess_url = f"https://api.genderize.io?name={name}"
    gender = requests.get(gender_guess_url).json()["gender"]
    age_guess_url = f"https://api.agify.io?name={name}"
    age = requests.get(age_guess_url).json()["age"]
    return render_template("index.html", name=name, gender=gender, age=age)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
