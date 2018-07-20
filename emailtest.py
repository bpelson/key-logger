import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("193w574257@gmail.com", "930258A26-")

msg = "hello world"
server.sendmail("193w574257@gmail.com", "a6sfh6ec@gmail.com", msg)
server.quit()
