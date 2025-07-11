import smtplib
from email.message import EmailMessage
from google import genai
import json,ast,random
import threading
from flaskblog.env_var import api_key,email,password

def mes_con(dct):
  
  
  client = genai.Client(api_key=api_key)
  
  prompt = f""" You are an AI agent. Return only a Python list — no extra text. Format as short OTP email subject + content, warm and clear. Add newlines where needed. Include OTPs in messages.Also don,t include fstring in the output.also dont share otp_admin with user and otp_user with admin.

  Rules:

  role == "user": ["otp for Local-Link registration", "Warmly share otp_user. Ask to enter this OTP on the OTP page."]

  role == "admin": [{{"admin": ["otp for Local-Link registration", "Warmly share otp_admin with admin. Include username and email of user. Ask to share this OTP with user."], "user": ["Welcome message with otp_user. Ask politely to enter this OTP and request admin for admin OTP."]}}]

  If any needed OTP is missing/None: Send error message to admin and user. Ask only user to retry.

  If role == "admin": send otp_admin to admin, otp_user to user.

  If role == "user": send otp_user to user only.


  Input: {json.dumps(dct)} """
                                                                          
  

  response = client.models.generate_content(
      model="gemini-2.0-flash", contents=prompt
  )
  print(response.text)
  output=response.text
  st=output.index("[")
  ed=output.rindex("]")
  response=ast.literal_eval(output[st:ed+1])
  
  
  return response

def set_mail_content(dct):
  
  
  if dct["role"]=="admin":
    content_mail=mes_con(dct)
    t1=threading.Thread(target=send_mail,args=["nautiyaldivyansh98@gmail.com",content_mail[0]["admin"][0],content_mail[0]["admin"][1]])
    t2=threading.Thread(target=send_mail,args=[dct["email"],content_mail[0]["user"][0],content_mail[0]["user"][1]])
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    
  
  
  elif dct["role"]=="user":
    content_mail=mes_con(dct)
    send_mail(dct["email"],content_mail[0],content_mail[1])
   
    
  

  
  
  

def send_mail(remail,subject,content):
  
  server=smtplib.SMTP("smtp.gmail.com",587)
  server.starttls()
  server.login(email,password)
  msg=EmailMessage()
  msg["to"]=remail
  msg["subject"]=subject
  msg.set_content(content)
  server.send_message(msg)
  server.close()
  
  
if __name__=="__main__":
  set_mail_content({"role":"admin","email":"vampire02112006@gmail.com","otp_user":random.randint(1000,9999),"username":"user","otp_admin":random.randint(1000,9999)})
  
