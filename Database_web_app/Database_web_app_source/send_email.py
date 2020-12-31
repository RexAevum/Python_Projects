from email.mime.text import MIMEText # to read a sting as html
import smtplib

def send_email(email, height, age, avgHeight, avgAge, participants):
    from_email = 'rexaevum.dev@gmail.com'
    from_password = 'admin2020'
    to_email = email
    
    # convert to inches as well
    inches = round(float(height)/2.54, 1)
    avgInches = round(float(avgHeight)/2.54, 1) 

    subject = 'Data'
    message = "Your height is <strong>{} cm ({} in)</strong> and age is <strong>{}</strong>. ".format(height, inches, age)
    message = message + "From the <strong>{}</strong> survey participants, the current average height is ".format(participants)
    message = message +  "<strong>{} cm ({} in)</strong> and the average age is <strong>{}</strong>".format(avgHeight, avgInches, avgAge)

    # Covnert to a html
    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    # Connect to from_email
    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)