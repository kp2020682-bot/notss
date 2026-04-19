from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL connection
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="NewPassword123",   # ⚠ yaha apna password daalo
        database="myapp"
    )

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)",
        (name, email)
    )

    conn.commit()
    conn.close()

    return "Data saved successfully!"

if __name__ == "__main__":
    app.run(debug=True)