#!/usr/bin/env python3
"""app.py module"""
from flask import Flask, request, jsonify, abort, redirect
from auth import Auth
import uuid

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def firstmessage():
    ''' first message '''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
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


@app.route('/sessions', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        abort(400)
    if AUTH.valid_login(email=email, password=password):
        new_session_id = str(uuid.uuid4())
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', new_session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout():
    ''' ind the user with the requested session ID.
    If the user exists destroy the session '''
    current_session = request.cookies.get('session_id', None)
    current_user = AUTH.get_user_from_session_id(current_session)
    if current_user is not None and current_session is not None:
        AUTH.destroy_session(current_user.id)
        return redirect('/')
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
