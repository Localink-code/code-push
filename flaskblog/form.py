# Import Flask-WTF and WTForms modules for form handling
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional


# User registration form with validation
class RegisterForm(FlaskForm):
  # Username field with length validation (2-20 characters)
  username = StringField("Username",
                         validators=[DataRequired(),
                                     Length(min=2, max=20)])
  
  # Email field with email format validation
  email = StringField("Email", validators=[DataRequired(), Email()])
  
  # Password field (required)
  password = PasswordField("Password", validators=[DataRequired()])
  
  # Password confirmation field that must match the password field
  confirm_password = PasswordField(
      "Confirm Password", validators=[DataRequired(),
                                      EqualTo("password")])
  
  # Submit button for the registration form
  submit = SubmitField("Sign Up")


# OTP verification form for two-factor authentication
class OTP(FlaskForm):
  # Regular user OTP field (required)
  otp = StringField("Enter Your OTP", validators=[DataRequired()])
  
  # Admin OTP field (required for admin users)
  otpa= StringField("Enter Admin OTP", validators=[DataRequired()])
  
  # Submit button for OTP verification
  submit = SubmitField("Submit")
