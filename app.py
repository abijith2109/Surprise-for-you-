from flask import Flask, render_template

app = Flask(__name__)

# Step 1: Question page
@app.route("/")
def question():
    return render_template("question.html")

# Step 2: Love letter page
@app.route("/letter")
def letter():
    return render_template("letter.html")

# Step 3: Gift page
@app.route("/gift")
def gift():
    return render_template("gift.html")

# Step 4: Hug or Kiss choice page
@app.route("/choice")
def choice():
    return render_template("choice.html")

# Step 5A: Hug page
@app.route("/hug")
def hug():
    return render_template("hug.html")

# Step 5B: Kiss page
@app.route("/kiss")
def kiss():
    return render_template("kiss.html")

# Step 6: Final page (you can put the music here)
@app.route("/final")
def final():
    return render_template("final.html")


if __name__ == "__main__":
    app.run(debug=True)
