from flask import Flask, jsonify, request, send_from_directory
import sqlite3
import os

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("words.db")
    conn.row_factory = sqlite3.Row
    return conn

# Serve words.html from the root folder
@app.route("/")
def serve_words_page():
    return send_from_directory(os.getcwd(), "words.html")

# READ all words
@app.route('/words', methods=['GET'])
def get_words():
    conn = get_db()
    rows = conn.execute("SELECT * FROM words").fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])

# CREATE a word
@app.route('/words', methods=['POST'])
def add_word():
    data = request.json
    irish = data.get("irish")
    english = data.get("english")

    conn = get_db()
    conn.execute(
        "INSERT INTO words (irish, english) VALUES (?, ?)",
        (irish, english)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Word added"}), 201

# UPDATE a word
@app.route('/words/<int:id>', methods=['PUT'])
def update_word(id):
    data = request.json
    irish = data.get("irish")
    english = data.get("english")

    conn = get_db()
    conn.execute(
        "UPDATE words SET irish = ?, english = ? WHERE id = ?",
        (irish, english, id)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Word updated"})

# DELETE a word
@app.route('/words/<int:id>', methods=['DELETE'])
def delete_word(id):
    conn = get_db()
    conn.execute("DELETE FROM words WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Word deleted"})

if __name__ == "__main__":
    app.run(debug=True)
