from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("question.html")

@app.route("/question")
def question():
    return render_template("question.html")

@app.route("/choice")
def choice():
    return render_template("choice.html")

@app.route("/hug")
def hug():
    return render_template("hug.html")

@app.route("/gift")
def gift():
    return render_template("gift.html")

@app.route("/letter")
def letter():
    return render_template("letter.html")

if __name__ == "__main__":
    app.run(debug=True)
