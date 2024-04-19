from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
import os
from sqlalchemy.sql import text

def login(username, password):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            return True
        else:
            return False

def logout():
    del session["user_id"]


def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = text("INSERT INTO users (username,password) VALUES (:username,:password)")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except Exception as e:
        print("Error during registration:", e)
        return False
    return True

def user_id():
    return session.get("user_id",0)

def get_username(user_id):
    sql = text("SELECT username FROM users WHERE id = :user_id")
    result = db.session.execute(sql, {"user_id": user_id})
    username = result.fetchone()[0]
    return username
