'''from flask import Flask, render_template
app = Flask(__name__)


#__name__ is a special variable


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)'''

from flask import *
import sqlite3

app = Flask(__name__)


@app.route('/')

def home():
    return render_template('register.html')


@app.route('/confirm', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':

        n = request.form['name']
        i = request.form['age']
        p = request.form['mobile']

        with sqlite3.connect('profile.db') as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Emp (name, age, ph_no) VALUES(?,?,?)",(n,i,p))
            con.commit()
            cur.close()
            return render_template('confirm.html',name=n,age=i,mobile=p)




if __name__ == "__main__":
    app.run(debug=True)
