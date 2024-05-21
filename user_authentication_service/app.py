#!/usr/bin/env python3
"""app.py module"""
from flask import Flask, request, jsonify
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
        return jsonify({"email": "<registered email>",
                        "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
