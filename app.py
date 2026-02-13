from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def question():
    return render_template("question.html")

@app.route("/yes")
def letter():
    return render_template("letter.html")

@app.route("/gift")
def gift():
    return render_template("gift.html")

@app.route("/music")
def music():
    return render_template("music.html")

@app.route("/final")
def final():
    return render_template("final.html")

if __name__ == "__main__":
    app.run(debug=True)
