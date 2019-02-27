from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/me")
def me():
    return render_template("next.html")
@app.route("/contact")
def contact():
    return render_template("my.html")
@app.route("/about")
def about():
    return "my address is"
if(__name__=="__main__"):
    app.run(debug=True)