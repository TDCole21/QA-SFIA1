from flask import Flask, render_template
from templates import dummydata

app = Flask(__name__) #__name__ is for best practice

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template("index.html", name="Home", page="active", posts=dummydata.dummyData)
@app.route('/about')
def about():
    return render_template("about.html", name="About", page="active", posts=dummydata.dummyData)
@app.route('/account')
def account():
    return render_template("account.html", name="Account", page="active", posts=dummydata.dummyData)


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)