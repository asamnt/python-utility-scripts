import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

api_file = open(r"C:\projects\python\utility_scripts\google-api-key.txt", "r", encoding="utf8")
api_key = api_file.readline()
api_file.close()

# home = input("Enter home address\n")
# work = input("Enter a work address\n")

home = "Assetz 63 Degree East"
work = "Helios Business Park"

# base url
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
# get response
r = requests.get(url + "origins=" + home + "&destinations=" + work + "&key=" + api_key) 
print(r.json())
 
# return time as text and as seconds
time = r.json()["rows"][0]["elements"][0]["duration"]["text"]       
seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]
  
# print the travel time
print("\nThe total travel time from home to work is", time)

mail_content = "Hello, Your total travel time  right now from home " + home + " to work "+ work + " is "+time
#The mail addresses and password
sender_address = 'amitsamant@gmail.com'
sender_pass = 'szaxhmjkucahkcny'
receiver_address = 'amitsamant@gmail.com;joeytayyil@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Travel Time : Home to Work'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP_SSL('smtp.gmail.com', 465) #use gmail with port
# session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')

