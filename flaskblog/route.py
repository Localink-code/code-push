# Import necessary modules from Flask and the application
from flaskblog import app, db
from flask import render_template, url_for, flash, redirect, request, session
from flaskblog.form import RegisterForm, OTP
from flaskblog.database import User

"""--------------------------------------------------------"""
# Global session dictionary to store temporary role information during registration
ses = {"role": None}


# Before request hook to ensure database tables are created
@app.before_request
def setvar():
    # Create all database tables if they don't exist
    db.create_all()
    

"""--------------------------------------------------------"""

# Home page route - resets verification status
@app.route("/")
def home():
    # Reset OTP verification status when visiting home page
    session["verify"] = False
    return render_template("home.html", title="home-page")


# User registration route - handles both form display and submission
@app.route("/register", methods=["GET", "POST"])
def register():
    # Create registration form instance
    form = RegisterForm()
    
    # Check if user has completed OTP verification
    if session.get("verify"):
        print("otp verified-")
        session["verify"] = False
        
        # Create new user with stored registration data
        user1 = ses["role"](username=session["data"][0],
                            email=session["data"][1],
                            password=session["data"][2])
        
        # Add user to database and commit
        db.session.add(user1)
        ses["role"] = None
        db.session.commit()
        return redirect(url_for("home"))

    # Process form submission if validation passes
    if form.validate_on_submit():
        # Set user role and prepare for OTP verification
        role = User
        flash(f"OTP-SENT", "success")
        page = "register"
        ses["role"] = role
        session["role"] = "user"
        
        # Store form data in session for later use after OTP verification
        session["data"] = [
            form.username.data, form.email.data, form.password.data
        ]
        return redirect(url_for("otp", page=page))
    
    # Render registration form template
    return render_template("register.html", title="register-page", form=form)


# OTP verification route - handles two-factor authentication
@app.route("/otp/<page>", methods=["GET", "POST"])
def otp(page, *args, **kwarg):
    # Create OTP form instance
    form = OTP()
    
    # Remove admin OTP field if user is not admin
    if session.get("role") != "admin" :
        del form.otpa

    print(page)  # Debug print to show which page redirected here
    
    # Process OTP form submission
    if form.validate_on_submit():
        # Simple OTP validation (hardcoded for demo purposes)
        if form.otp.data == "1234":
            print("otp verified")
            flash(f"OTP verified", "success")
            session["verify"] = True
            # Redirect back to the page that initiated OTP verification
            return redirect(url_for(page))
    
    # Render OTP verification template
    return render_template("otp.html", title="otp-page", form=form)


# Commit any pending database transactions
db.session.commit()
