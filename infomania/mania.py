

import os
import smtplib
import requests
from datetime import datetime
from bs4 import BeautifulSoup


class Mania(object):

    def __init__(self, send_email=None, from_=None, to=None, host=None, username=None, password=None):
        self.sources = []

        self.email_to = os.environ.get('INFOMANIA_MAIL_TO', to)
        if type(self.email_to) is str:
            self.email_to = [self.email_to]

        self.send_email = send_email
        self.email_from = os.environ.get('INFOMANIA_MAIL_FROM', from_)
        self.email_host = os.environ.get('INFOMANIA_SMTP_SERVER', host)
        self.email_usernam = os.environ.get('INFOMANIA_SMTP_USERNAME', username)
        self.email_password = os.environ.get('INFOMANIA_SMTP_PASSWORD', password)

    def set_source(self, source):
        self.sources.append(source)

    def run(self):
        source_data = []
        for source in self.sources:
            events_data = []
            source_data.append({
                'source': source,
                'events': events_data
            })

            source_code = requests.get(source.url).content
            parsed_html = BeautifulSoup(source_code, 'html.parser')

            if self.send_email:
                os.system('touch {}.txt'.format(source.name))
                db_read = open('{}.txt'.format(source.name), 'r').readline()
                db_write = open('{}.txt'.format(source.name), 'a')

            try:
                events = source.parse(parsed_html)
            except:
                raise Exception('Error parsing ' + source.name + '\' HTML')

            if type(events) is not list:
                events = [events,]

            for event in reversed(events):

                if type(event) is not dict:
                    event = {'title': event}

                if 'date' not in event:
                    event['date'] = datetime.now().strftime('%d.%m.%Y')

                date_title = '{} {}'.format(event['date'], event['title'])
                
                if self.send_email:
                    if date_title in db_read:
                        continue
                    else:
                        db_write.write(date_title+';')

                try:
                    date_list = map(int, reversed(event['date'].split('.')[:3])) + [0, 0, 0]
                except:
                    continue

                date_obj = datetime(*date_list)

                now = datetime.now()
                now_list = [now.year, now.month, now.day, 0, 0, 0]
                now_obj = datetime(*now_list)

                if date_obj >= now_obj:
                    source.events.append(source.email_message(data=event))

        if self.send_email:
            db_write.close()
            
        return self.output()

    def output(self):
        if self.send_email:
            email_server = smtplib.SMTP(self.email_host)
            email_server.ehlo()
            email_server.starttls()
            email_server.login(self.email_usernam, self.email_password)

            for source in self.sources:
                if len(source.events) > 0:
                    for e_to in self.email_to:
                        message_contents = [
                            self.email_from,
                            e_to,
                            source.e_subject,
                            '\n\n'.join(source.events),
                        ]
                        message = """\
From: {}
To: {}
Subject: {}

{}""".format(*message_contents)
                        email_server.sendmail(self.email_from, [e_to], message)
            
            email_server.quit()
        
        return self.sources