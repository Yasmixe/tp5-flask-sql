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
    return render_template("exo12.html")


@app.route("/addPerson", methods=["POST"])
def doaddperson():
    nom = request.form["valNom"]
    prenom = request.form["valPrenom"]
    points = request.form["valPoints"]

    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT MAX(id) FROM person")
    max_id = cursor.fetchone()[0]
    new_id = max_id + 1

    cursor.execute(
        "INSERT INTO person (id, nom, prenom, points) VALUES (%s, %s, %s, %s)",
        (new_id, nom, prenom, points),
    )

    conn.commit()
    cursor.close()

    return redirect("formadd")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
