

import os


DEFAULT_MAIL_SUBJECT = '------- {} -------'

class Source(object):

    def __init__(self):
        self.name = self.source_name()
        self.url = self.source_url()
        self.e_subject = self.email_subject()
        self.events = []

    def source_name(self):
        pass

    def source_url(self):
        pass

    def parse(self, content):
        pass

    def email_subject(self):
        return DEFAULT_MAIL_SUBJECT.format(self.name)

    def email_message(self, data):
        pass