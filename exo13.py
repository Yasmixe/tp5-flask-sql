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
    return render_template("exo13.html")


@app.route("/updateperson", methods=["POST"])
def doaddperson():
    id = request.form["valid"]
    nom = request.form["valNom"]
    prenom = request.form["valPrenom"]
    points = request.form["valPoints"]

    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE person SET "
        'nom="' + nom + '", '
        'prenom="' + prenom + '", '
        "points=" + points + " WHERE id=" + id
    )

    conn.commit()
    cursor.close()

    return redirect("/formupdate")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
