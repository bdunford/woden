import smtplib
from email.message import Message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import dns.resolver
import json


class Mailer(object):

    def __init__(self, sender, recipients, subject, content, is_html=False, attachment=False, relay=False, timeout=5):
        self.sender = sender
        self.recipients = recipients
        self.subject = subject
        self.content = content
        self.is_html = is_html
        self.attachment = attachment 
        self.relay = relay
        self.timeout = timeout

    def _get_mail_servers(self, domain):
        servers = list(map(lambda x: {"sort": int(x.preference), "name": x.exchange.to_text().rstrip('.')}, dns.resolver.query(domain, 'MX')))
        return list(map(lambda f: f["name"],sorted(servers,key=lambda x: x["sort"])))

    def _build_mailing_list(self):
        mail_list = {}
        for r in self.recipients:
            d = r.split("@")[1]
            if d not in mail_list:
                mail_list[d] = {
                    "recipients": [r],
                    "servers": self._get_mail_servers(d)
                }
            else:
                mail_list[d]["recipients"].append(r)
        return mail_list

    def _send_message(self, mail_server, recipients, msg):
        try:
            s = smtplib.SMTP('{0}:25'.format(mail_server),timeout=self.timeout)
            s.ehlo()
            s.sendmail(msg['From'], recipients, msg.as_string())
            s.quit()
            return True
        except Exception as e:
            self.error = str(e)
            return False

    def _relay_message(self, msg):
        try:
            s = smtplib.SMTP_SSL(self.relay["host"], self.relay["port"],timeout=self.timeout) if self.relay["ssl"] else smtplib.SMTP(self.relay["host"], self.relay["port"],timeout=3)   
            s.ehlo()
            if "username" in self.relay:
                s.login(self.relay["username"],self.relay["password"])
            s.sendmail(msg['From'], self.recipients, msg.as_string())
            s.quit()
            return True
        except Exception as e:
            self.error = str(e)
            return False

    def _create_message(self):
        msg = MIMEMultipart() if self.attachment else Message()
        msg['To'] = ",".join(self.recipients)
        msg["From"] = self.sender
        msg["Subject"] = self.subject
    
        if self.attachment:
            msg.attach(MIMEText(self.content, 'html' if self.is_html else 'plain' ))
            part = MIMEBase('application', 'octet-stream')

            with open(self.attachment) as f:
                part.set_payload(f.read())

            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= {0}".format(os.path.split(self.attachment)[1]))
            msg.attach(part)
        else:
            if is_html:
                msg.add_header('Content-Type', 'text/html')
            msg.set_payload(self.content)

        return msg

    @staticmethod    
    def Send(sender, recipients, subject, content, is_html=False, attachment=False, relay=False, timeout=5):
        instance = Mailer(sender, recipients, subject, content, is_html, attachment, relay,timeout)
        msg = instance._create_message()
        if instance.relay:
            if not instance._relay_message(msg):
                return instance.error

        else: 
            errors = []
            for k,v in instance._build_mailing_list().items():
                if not instance._send_message(v["servers"][0],v["recipients"],msg):
                    errors.append(instance.error)

            if len(errors) > 0:
                return errors

                    
                

