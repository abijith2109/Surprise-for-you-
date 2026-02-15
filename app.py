from flask import Flask, render_template

app = Flask(__name__)

@app.route("/question")
def question():
    return render_template("question.html")

@app.route("/letter")
def letter():
    return render_template("letter.html")

@app.route("/gift")
def gift():
    return render_template("gift.html")

@app.route("/choice")
def choice():
    return render_template("choice.html")

@app.route("/hug")
def hug():
    return render_template("hug.html")

@app.route("/kiss")
def kiss():
    return render_template("kiss.html")

@app.route("/final")
def final():
    return render_template("final.html")

if __name__ == "__main__":
    app.run(debug=True)
