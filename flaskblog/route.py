# Import necessary modules from Flask and the application
from flaskblog import app, db, login_manager
from flask import render_template, url_for, flash, redirect, request, session
from flaskblog.form import RegisterForm, OTP
from flaskblog.database import User,Admin
import random
from flaskblog.send_mail import set_mail_content
from flask_login import   login_user, login_required, logout_user
"""--------------------------------------------------------"""


# Before request hook to ensure database tables are created
# Global session dictionary to store temporary role information during registration
ses = {}
@app.before_request
def setvar():
    # Create all database tables if they don't exist
    db.create_all()
@login_manager.user_loader
def load_user(user_id):

    # Load user from database based on user ID
    return User.query.get(int(user_id))

"""--------------------------------------------------------"""
# Home page route - resets verification status
@app.route("/")
@login_required
def home():
    # Reset OTP verification status when visiting home page
    session["verify"] = False
    return render_template("home.html", title="home-page")
#################################################################
@app.route("/login", methods=["GET", "POST"])
def login():
    # Create login form instance
    return "this is login page."


####################################################################

# User registration route - handles both form display and submission
@app.route("/register", methods=["GET", "POST"])
def register():
    # Create registration form instance
    form = RegisterForm()
    
    # Check if user has completed OTP verification
    if session.get("verify"):
        session["otp_page"]=False
        print("otp verified-")
        session["verify"] = False
        
        # Create new user with stored registration data
        user1 = ses["role"](username=session["data"][0],
                            email=session["data"][1],
                            password=session["data"][2])
        
        # Add user to database and commit
        db.session.add(user1)
        ses["role"] = None
        # db.session.commit()
        return redirect(url_for("login"))

    # Process form submission if validation passes
    if form.validate_on_submit():
        # Set user role and prepare for OTP verification
        if form.role.data == "user":
            print("user")
            
            flash(f"OTP-SENT", "success")
            ses["role"] = User
            session["email_data"]={"role":"user","email":form.email.data,"otp_user":random.randint(1000,9999),"username":form.username.data}
            set_mail_content(session["email_data"])
        
        
        
        elif form.role.data == "admin":
            print("admin")

            flash(f"OTP-SENT", "success")
            ses["role"] = Admin
            session["email_data"]={"role":"admin","email":form.email.data,"otp_user":random.randint(1000,9999),"username":form.username.data,"otp_admin":random.randint(1000,9999)}
            set_mail_content(session["email_data"])
        
        page = "register"
        
        session["next_page"]=page
        session["otp_page"]= True
            
        
        # Store form data in session for later use after OTP verification
        session["data"] = [
            form.username.data, form.email.data, form.password.data
        ]
        return redirect(url_for("otp",page=page))
    
    # Render registration form template
    return render_template("register.html", title="register-page", form=form)


######################################################################


# OTP verification route - handles two-factor authentication
@app.route("/otp/<page>", methods=["GET", "POST"])
def otp(page,*args, **kwarg):
    # Create OTP form instance
    form = OTP()
    
    # Remove admin OTP field if user is not admin
    if session["email_data"]["role"] != "admin" :
        del form.otpa

    if session["otp_page"]:
        print("this time otp_page is true")
        print("ye esse aage kyu nhi ja rha ")

       
    # Process OTP form submission
        if form.validate_on_submit():
            print("otp form validated")
            
            # Simple OTP validation (hardcoded for demo purposes)
            if str(form.otp.data) == "1234":
                
                print("otp verified")
                flash(f"OTP verified", "success")
                session["verify"] = True
                # Redirect back to the page that initiated OTP verification
                return redirect(url_for(page))
    else:
        
        print("this time otp_page is false")
        return redirect(url_for(session["next_page"]))
        
    
    # Render OTP verification template
    return render_template("otp.html", title="otp-page", form=form)

###################################################################

@app.errorhandler(404)
def page_not_found(error):
    # Return a custom error message and status code for 404 errors ie if user tries to access a page that doesn't exist
    return "hello gays", 404

# Commit any pending database transactions
#db.session.commit()