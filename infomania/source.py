

from .settings import DEFAULT_MAIL_FROM, DEFAULT_MAIL_TO, DEFAULT_MAIL_SUBJECT


class Source(object):

    def __init__(self):
        self.name = self.source_name()
        self.url = self.source_url()
        self.e_subject = self.email_subject()
        self.e_from = self.email_from()
        self.e_to = self.email_to()
        self.events = []

    def source_name(self):
        pass

    def source_url(self):
        pass

    def parse(self, content):
        pass

    def email_subject(self):
        return DEFAULT_MAIL_SUBJECT.format(self.name)

    def email_from(self):
        return DEFAULT_MAIL_FROM

    def email_to(self):
        return DEFAULT_MAIL_TO

    def email_message(self, data):
        pass