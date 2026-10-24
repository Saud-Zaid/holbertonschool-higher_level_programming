#!/usr/bin/python3
"""Module that implements a simple RESTful API using Flask."""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route('/')
def home():
    """Return welcome message at root URL."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Return list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Return status of the API."""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Return the user object for the given username."""
    user = users.get(username)
    if user is not None:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user to the in-memory users dictionary."""
    data = request.get_json(silent=True)
    if data is None or not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
