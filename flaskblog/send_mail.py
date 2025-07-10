import smtplib
from email.message import EmailMessage
from google import genai
import json,ast,random
import threading
try:
  from secret import api_key
except:
  from flaskblog.secret import api_key
def mes_con(dct):
  
  
  client = genai.Client(api_key=api_key)
  
  prompt = f""" You are an AI agent. Return only a Python list — no extra text. Format as short OTP email subject + content, warm and clear. Add newlines where needed. Include OTPs in messages.Also don,t include fstring in the output.

  Rules:

  role == "user": ["otp for Local-Link registration", "Warmly share otp_user. Ask to enter this OTP on the OTP page."]

  role == "admin": [{{"admin": ["otp for Local-Link registration", "Warmly share otp_admin with admin. Include username and email of user. Ask to share this OTP with user."], "user": ["Welcome message with otp_user. Ask politely to enter this OTP and request admin for admin OTP."]}}]

  If any needed OTP is missing/None: Send error message to admin and user. Ask only user to retry.

  If role == "admin": send otp_admin to admin, otp_user to user.

  If role == "user": send otp_user to user only.


  Input: {json.dumps(dct)} """
                                                                          
  

  response = client.models.generate_content(
      model="gemini-2.0-flash-lite", contents=prompt
  )
  response=ast.literal_eval(response.text[10:-3])
  
  
  print(response)

def set_mail_content(dct):
  
  
  if dct["role"]=="admin":
    content_mail=mes_con(dct)
    # t1=threading.Thread(target=send_mail,args=("admin@gmail.com",content_mail[0]["admin"][0],content_mail[0]["admin"][1]))
    # t2=threading.Thread(target=send_mail,args=(dct["email"],content_mail[0]["user"][0],content_mail[0]["user"][1]))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    
  
  
  elif dct["role"]=="user":
    content_mail=mes_con(dct)
    # send_mail(dct["email"],content_mail[0],content_mail[1])
   
    
  

  
  
  

def send_mail(remail,subject,content):
  server=smtplib.SMTP("smtp.gmail.com",587)
  server.starttls()
  server.login("localink2024@gmail.com","Localink@2024")
  msg=EmailMessage()
  msg["receiver"]=remail
  msg["subject"]=subject
  msg.set_content(content)
  server.send_message(msg)
  server.close()
  
if __name__=="__main__":
  set_mail_content({"role":"user","email":"user@gmail.com","otp_user":random.randint(1000,9999),"username":"user","otp_admin":random.randint(1000,9999)})
  
