from db import db
import users
from sqlalchemy.sql import text


def get_list():
    sql = text("SELECT M.content, U.username, M.sent_at FROM messages M, users U WHERE M.user_id=U.id ORDER BY M.id")
    result = db.session.execute(sql)
    return result.fetchall()

def send(content):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("INSERT INTO messages (content, user_id, sent_at) VALUES (:content, :user_id, NOW())")
    db.session.execute(sql, {"content":content, "user_id":user_id})
    db.session.commit()
    return True

def get_ketju_messages(ketju_name):
    sql = text("SELECT content, username FROM messages WHERE ketju = :ketju_name")
    result = db.session.execute(sql, {"ketju_name": ketju_name})
    messages = result.fetchall()
    return messages

def send_message(content, username, ketju_name):
    sql= text("INSERT INTO messages (content, username, ketju) VALUES (: content, :username, :ketju_name)")
    db.session.execute(sql, {"content": content, "username": username, "ketju_name": ketju_name})
    db.session.commit()
