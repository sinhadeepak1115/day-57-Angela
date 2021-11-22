from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Plzz enter your name at the end of the url."

@app.route("/<name>")
def genz(name):
    requests_age = requests.get(f"https://api.agify.io/?name={name}").json()
    age = (requests_age.get("age"))
    requests_gender = requests.get(f"https://api.genderize.io/?name={name}").json()
    gender = (requests_gender.get("gender"))
    return render_template("index.html",name_1=name, age=age, gender=gender)

if __name__ == "__main__":
    app.run(debug=True)


