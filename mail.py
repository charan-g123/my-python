#!/usr/bin/python3
import smtplib 
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("charangowda717@gmail.com","")
message ="message_you_need-send"
s.sendmail("charangowda717@gmail.com","charangowda717@gmail.com",message)
s.quit()
