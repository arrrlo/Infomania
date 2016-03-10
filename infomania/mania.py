

import os
import smtplib
import requests
from datetime import datetime
from bs4 import BeautifulSoup

from .settings import SMTP_SERVER, SMTP_USERNAME, SMTP_PASSWORD


class Mania(object):

    def __init__(self, email=True):
        self.sources = []
        self.email = email

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

            if self.email:
                os.system('touch {}.txt'.format(source.name))
                db_read = open('{}.txt'.format(source.name), 'r').readline()
                db_write = open('{}.txt'.format(source.name), 'a')

            events = source.parse(parsed_html)
            for event in reversed(events):
                date_title = '{} {}'.format(event['date'], event['title'])
                
                if self.email:
                    if date_title in db_read:
                        continue
                    else:
                        db_write.write(date_title+';')
                
                date_list = map(int, reversed(event['date'].split('.'))) + [0, 0, 0]
                date_obj = datetime(*date_list)

                now = datetime.now()
                now_list = [now.year, now.month, now.day, 0, 0, 0]
                now_obj = datetime(*now_list)

                if date_obj > now_obj:
                    source.events.append(source.email_message(data=event))

        if self.email:
            db_write.close()
            
        return self.output()

    def output(self):
        if self.email:
            email_server = smtplib.SMTP(SMTP_SERVER)
            email_server.ehlo()
            email_server.starttls()
            email_server.login(SMTP_USERNAME, SMTP_PASSWORD)

            for source in self.sources:
                if len(source.events) > 0:

                    if isinstance(source.e_to, str):
                        source.e_to = source.e_to.split(',')

                    for e_to in source.e_to:
                        message_contents = [
                            source.e_from,
                            e_to,
                            source.e_subject,
                            '\n\n'.join(source.events),
                        ]
                        message = """\
From: {}
To: {}
Subject: {}

{}""".format(*message_contents)
                        email_server.sendmail(source.e_from, [e_to], message)
            
            email_server.quit()
        
        return self.sources