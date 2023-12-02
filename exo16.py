from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

app.config["MYSQL_DATABASE_HOST"] = "localhost"
app.config["MYSQL_DATABASE_PORT"] = 3306
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "pass_root"
app.config["MYSQL_DATABASE_DB"] = "db_persons"

mysql.init_app(app)


@app.route("/form")
def form():
    return render_template("exo14.html")


@app.route("/")
def index():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM person")
    data = cursor.fetchall()
    cursor.close()

    return render_template("index.html", data=data)


@app.route("/deleteperson", methods=["POST"])
def doaddperson():
    id = request.form["valid"]

    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM person where id=" + id)

    conn.commit()
    cursor.close()

    return redirect("/formDelete")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
