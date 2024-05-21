#!/usr/bin/env python3
"""app.py module"""
from flask import Flask, request, jsonify, abort
import response
from auth import Auth

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
        new_session_id = AUTH._generate_uuid()
        request.set_cookie('session_id', new_session_id)
        return jsonify({"email": email, "message": "logged in"})
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
