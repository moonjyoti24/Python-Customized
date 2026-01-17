from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_user",
        password="your_password",
        database="your_database"
    )

# INSERT
@app.route("/insert", methods=["POST"])
def insert_row():
    data = request.json
    name = data.get("name")
    role = data.get("role")

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, role) VALUES (%s, %s)", (name, role))
    conn.commit()

    return jsonify({"message": "Row inserted", "id": cursor.lastrowid})

# UPDATE
@app.route("/update/<int:emp_id>", methods=["PUT"])
def update_row(emp_id):
    data = request.json
    name = data.get("name")
    role = data.get("role")

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE employees SET name=%s, role=%s WHERE id=%s",
        (name, role, emp_id)
    )
    conn.commit()

    return jsonify({"message": "Row updated"})

# DELETE
@app.route("/delete/<int:emp_id>", methods=["DELETE"])
def delete_row(emp_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id=%s", (emp_id,))
    conn.commit()

    return jsonify({"message": "Row deleted"})

# OPTIONAL: fetch all rows
@app.route("/employees", methods=["GET"])
def get_all():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True)
