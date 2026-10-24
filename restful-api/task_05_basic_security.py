#!/usr/bin/python3
"""Module that implements basic authentication and JWT security in Flask."""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, get_jwt,
    get_jwt_identity, jwt_required
)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-jwt-key-for-auth-token-generation'
jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify username and password for basic authentication."""
    if username in users and check_password_hash(
        users[username]["password"], password
    ):
        return username
    return None


@auth.error_handler
def basic_auth_error():
    """Handle basic authentication errors returning 401."""
    return jsonify({"error": "Unauthorized"}), 401


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing token errors."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token errors."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired token errors."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked token errors."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle fresh token required errors."""
    return jsonify({"error": "Fresh token required"}), 401


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Return access granted message for basic authentication."""
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """Log in user and return JWT access token."""
    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid credentials"}), 401
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Invalid credentials"}), 401
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]}
    )
    return jsonify({"access_token": access_token}), 200


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """Return access granted message for valid JWT."""
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """Return admin access granted message if user has admin role."""
    current_user = get_jwt_identity()
    user = users.get(current_user)
    claims = get_jwt()
    role = claims.get("role") or (user.get("role") if user else None)
    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
