from db import db
from app import app
from flask import render_template, request, redirect, session
import messages, users

@app.route("/")
def etusivu():
    print("ETUSIVULLA OLLAAN")
    print("user_id" in session)
    if "user_id" in session:
        username = users.get_username(session["user_id"])
        return render_template("etusivu.html", username=username)
    else:
        return redirect("/kirjaudu")

@app.route("/kirjaudu", methods=["GET", "POST"])
def kirjaudu():
    if request.method == "GET":
       return render_template("kirjaudu.html")
    if request.method == "POST":
       username = request.form["username"]
       password = request.form["password"]
       if users.login(username, password):
            print("kirjautuminen onnistui")
            return redirect("/")
       else:
            return render_template("error.html", message="Annoit väärän tunnuksen tai salasanan")  
               
@app.route("/logout")
def logout(): 
    users.logout()
    return redirect("/")
    #del session["user_id"]
    #return redirect("/")


@app.route("/sisään", methods=["GET", "POST"])
def sisaan():
    if request.method == "GET":
        return render_template("sisään.html")
    if request.method == "POST":
       username = request.form["username"]
       password1 = request.form["password_1"]
       password2 = request.form["password_2"]
       if password1 != password2:
          return render_template("error.html", message="Annoit kaksi eri salasanaa")
       if users.register(username, password1):
          return redirect("/")
       else:
          return render_template("error.html", message="Rekistöröinti ei onnistunut")
          
@app.route("/ketju1")
def ketju1():
    if "user_id" in session: 
        username = users.get_username(session["user_id"])
        messages = messages.get_ketju_messages("ketju1.html")
        count_messages = len(messages)
        return render_template("ketju1.html", username=username, messages=messages, count=count_messages)
    else:
       return redirect("/kirjaudu")

@app.route("/ketju2")
def ketju2():
    if "user_id" in session: 
        username = users.get_username(session["user_id"])
        messages = messages.get_ketju_messages("ketju2.html")
        count_messages = len(messages)
        return render_template("ketju2.html", username=username, messages=messages, count=count_messages)
    else:
       return redirect("/kirjaudu")

@app.route("/ketju3")
def ketju3():
    if "user_id" in session: 
        username = users.get_username(session["user_id"])
        messages = messages.get_ketju_messages("ketju3.html")
        count_messages = len(messages)
        return render_template("ketju3.html", username=username, messages=messages, count=count_messages)
    else:
       return redirect("/kirjaudu")

@app.route("/uusi", methods=["GET", "POST"])
def uusi():
    if "user_id" in session:
       if request.method == "GET":
            username = users.get_username(session["user_id"])
            return render_template("uusi.html", username=username)
       elif request.method == "POST":
            return redirect("/")
    else:
       return redirect("/kirjaudu")         
