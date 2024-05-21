#!/usr/bin/env python3
"""app.py module"""
from flask import Flask, request, jsonify, abort, redirect
from auth import Auth
from db import DB

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    ''' first message '''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    ''' checks if the user exists and returns based on existance '''
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email=email, password=password)
        return jsonify({"email": email,
                        "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        abort(400)
    if AUTH.valid_login(email=email, password=password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    ''' ind the user with the requested session ID.
    If the user exists destroy the session '''
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if session_id is None or user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=["GET"], strict_slashes=False)
def profile():
    ''' return the profile based on the user '''
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if session_id is None or user is None:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    ''' Get reset password token '''
    email = request.form.get('email')
    token = AUTH.get_reset_password_token(email)
    if DB.find_user_by(email):
        return jsonify({{"email": email, "reset_token": token}}), 200
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
