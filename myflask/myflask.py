from flask import Flask, render_template
from urllib.request import method

app = Flask(__name__)

@app.route("/")
def hello():
    return "歡迎光臨，您好！"

@app.route("/about")
def about():
    return "這是一個使用Flask建立的測試網站！"

@app.route("/login", methods = ['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        username = reuqest.form['username']
        password = request.form['password']
    return render_template('login.html',error = error )

@app.route("/user/")
@app.route("/user/<username>")
def show_user(username = None):
    return render_template('show_user.html',name = username)
    # return "User name is: {}".format(username)

if __name__ == '__main__':
    app.run()
