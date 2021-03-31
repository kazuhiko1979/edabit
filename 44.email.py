import smtplib
import mimetypes
import os

from email import encoders, utils
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def attachment(filename):

    with open(filename, "rb") as f:
        mimetype, mimeencoding = \
            mimetypes.guess_type(filename)

        if mimeencoding or (mimetype is None):
            mimetype = "application/octet-stream"

        maintype, subtype = mimetype.split('/')

        if maintype == "text":
            attachment = MIMEText(f.read(), _subtype=subtype)
        else:
            attachment = MIMEBase(maintype, subtype)
            attachment.set_payload(f.read())
            encoders.encode_base64(attachment)

        attachment.\
        add_header(
            'Content-Disposition',
            'attachemnt',
            filename=os.path.basename(filename)
        )

    return attachment


def create_message(src_address, dst_address,
                   bcc, subject, body, files):

    msg = MIMEMultipart()
    # msg["Subject"] = subject
    msg.add_header('Subject', subject)
    msg["Form"] = src_address
    msg["To"] = dst_address
    msg["Bcc"] = bcc
    msg["Message-ID"] = utils.make_msgid()
    msg["Date"] = utils.formatdate(localtime=True)

    body = MIMEText(body, _subtype="plain")
    msg.attach(body)

    for filename in files:
        msg.attach(attachment(filename))

    return msg.as_string()


def send(src_address, dst_address, msg, password):

    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(src_address, password)
    smtp.sendmail(src_address, dst_address, msg.as_string())
    smtp.close

#
#



def main():

    subject = "This is Email Send Test"
    body = "Python Programming is so FUN!"

    src_address = "****@gmail.com"
    password = ""
    dst_address = "****@gmail.com"
    bcc = ""

    files = [
        r"C:\Users\kazuh\PycharmProjects\edabit\C\Some.csv",
        r"C:\Users\kazuh\PycharmProjects\edabit\C\some.txt"
    ]

    msg = create_message(src_address, dst_address,
                             bcc, subject, body, files)

    send(src_address, dst_address, msg, password)

    return


if __name__ == '__main__':
    main()