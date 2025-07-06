from flaskblog import app, db
from flask import render_template, url_for, flash, redirect, request, session
from flaskblog.form import RegisterForm, OTP
from flaskblog.database import User
"""--------------------------------------------------------"""
#these functions are used below in the route as decorator

ses = {"role": None}



@app.before_request
def setvar():
    db.create_all()
    


"""--------------------------------------------------------"""


@app.route("/")
def home():
    session["verify"] = False
    return render_template("home.html", title="home-page")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if session.get("verify"):
        print("otp verified-")
        session["verify"] = False
        

        user1 = ses["role"](username=session["data"][0],
                            email=session["data"][1],
                            password=session["data"][2])
        
        db.session.add(user1)
        ses["role"] = None
        db.session.commit()
        return redirect(url_for("home"))

    if form.validate_on_submit():
        role = User
        flash(f"OTP-SENT", "success")
        page = "register"
        ses["role"] = role
        session["role"] = "user"
        session["data"] = [
            form.username.data, form.email.data, form.password.data
        ]
        return redirect(url_for("otp", page=page))
    return render_template("register.html", title="register-page", form=form)


@app.route("/otp/<page>", methods=["GET", "POST"])
def otp(page, *args, **kwarg):
    form = OTP()
    if session.get("role") != "admin" :
        del form.otpa

    print(page)
    if form.validate_on_submit():
        if form.otp.data == "1234":
            print("otp verified")
            flash(f"OTP verified", "success")
            session["verify"] = True
            return redirect(url_for(page))
    return render_template("otp.html", title="otp-page", form=form)


db.session.commit()
