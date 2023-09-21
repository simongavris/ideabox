from flask import Flask, request, jsonify, g
from pymongo import MongoClient
import os
import logging

# Initialize Flask app
app = Flask(__name__)

# Logging configuration
logging.basicConfig(filename='app.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

# Load configurations from environment variables
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://username:password@mongo_server:27017/ideabox")
DEBUG = bool(os.environ.get("DEBUG", True))

# Initialize MongoDB client
client = MongoClient(MONGO_URI)
db = client.get_database()

@app.before_request
def before_request():
    g.db = db

@app.teardown_request
def teardown_request(exception):
    pass  # MongoDB handles connection pooling, so no need to close the database connection

@app.route('/submit', methods=['POST'])
def submit_idea():
    try:
        data = request.json
        idea = data.get('idea')
        
        if not idea:
            return jsonify({"status": "error", "message": "Invalid idea"}), 400

        g.db.ideas.insert_one({"idea": idea})
        
        logging.info("Idea successfully submitted.")

        return jsonify({"status": "success"}), 200

    except Exception as e:
        logging.error("An error occurred: %s", e)
        return jsonify({"status": "error", "message": "An error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=DEBUG)
