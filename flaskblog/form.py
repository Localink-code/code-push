from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional


class RegisterForm(FlaskForm):
  username = StringField("Username",
                         validators=[DataRequired(),
                                     Length(min=2, max=20)])
  email = StringField("Email", validators=[DataRequired(), Email()])
  password = PasswordField("Password", validators=[DataRequired()])
  confirm_password = PasswordField(
      "Confirm Password", validators=[DataRequired(),
                                      EqualTo("password")])
  submit = SubmitField("Sign Up")


class OTP(FlaskForm):
  otp = StringField("Enter Your OTP", validators=[DataRequired()])
  otpa= StringField("Enter Admin OTP", validators=[DataRequired()])
  submit = SubmitField("Submit")
