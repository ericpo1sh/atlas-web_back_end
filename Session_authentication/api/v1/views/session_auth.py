#!/usr/bin/env python3
""" Module of session auth views
"""
from flask import jsonify, request, abort, make_response
from models.user import User
import os
from api.v1.views import app_views


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    ''' New view for Session Authentication login '''
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    search_user = User.search({"email": email})
    if not search_user:
        return jsonify({"error": "no user found for this email"}), 404

    user = search_user[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth

    session_id = auth.create_session(user.id)
    to_json_user = user.to_json()
    response = make_response(to_json_user)
    session = os.getenv('SESSION_NAME')
    response.set_cookie(session, session_id)

    return response
