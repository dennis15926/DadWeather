#coding: utf-8
import urllib.request

def url_to_text(URL):
    try:
        response = urllib.request.urlopen(URL)
        for line in response:
            content = line.decode('UTF-8')
            if content.find('桐林') is not -1:
                return content
    except:
        print('Inacessible URL')
    return ""

def split_text(text):
    tokens=text.split('</font>')
    try:
        line=tokens[24]
        line = line.split('>')[-1]
    except:
        return ""
    return line

def test(URL='http://www.cwb.gov.tw/V7/observe/rainfall/Rain_Hr/7.htm'):
    split_text(url_to_text(URL))
    return

def send_email(recipient, subject, body):
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header

    ntu_user = "b00611035"
    ntu_pwd = "n1t5u926chen"
    FROM = ntu_user+"@ntu.edu.tw"
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = MIMEText(TEXT,_subtype='plain',_charset='UTF-8')
    message['Subject'] = Header(SUBJECT, charset='UTF-8')
    message['From']=FROM
    message['To']=", ".join(TO)
    try:
        server_ssl = smtplib.SMTP_SSL("smtps.ntu.edu.tw", 465)
        server_ssl.ehlo() # optional, called by login()
        server_ssl.login(ntu_user, ntu_pwd)  
        server_ssl.sendmail(FROM, TO, message.as_string())
        #server_ssl.quit()
        server_ssl.close()
        print ('successfully sent the mail')
    except:
        print ("failed to send mail")
