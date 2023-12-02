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


@app.route("/")
def form():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM person")
    data = cursor.fetchall()
    cursor.close()

    return render_template("exo17.html", data=data)


@app.route("/addPerson", methods=["POST"])
def index():
    nom = request.form["name"]
    prenom = request.form["secondname"]
    rangee = request.form["range"]
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO person ( nom, prenom, points) VALUES ( %s, %s, %s)",
        (nom, prenom, rangee),
    )
    data = cursor.fetchall()
    conn.commit()
    cursor.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
