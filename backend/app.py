from flask import Flask, request, jsonify, g
from contextlib import closing
import sqlite3
import os
import logging

# Initialize Flask app
app = Flask(__name__)

# Logging configuration
logging.basicConfig(filename='app.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

# Load configurations from environment variables
DATABASE = os.environ.get("DATABASE_URL", "ideas.db")
DEBUG = bool(os.environ.get("DEBUG", True))

# Initialize database
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# Database connection
def connect_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/submit', methods=['POST'])
def submit_idea():
    try:
        data = request.json
        idea = data.get('idea')
        
        if not idea:
            return jsonify({"status": "error", "message": "Invalid idea"}), 400

        cursor = g.db.cursor()
        cursor.execute("INSERT INTO ideas (idea) VALUES (?)", (idea,))
        g.db.commit()
        
        logging.info("Idea successfully submitted.")

        return jsonify({"status": "success"}), 200

    except Exception as e:
        logging.error("An error occurred: %s", e)
        return jsonify({"status": "error", "message": "An error occurred"}), 500

if __name__ == '__main__':
    if DEBUG:
        init_db()
    app.run(debug=DEBUG)
