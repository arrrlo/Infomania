

from .source import Source


class DollarKuna(Source):

    def source_name(self):
        return 'dollar-kuna'

    def source_url(self):
        return 'https://www.pbz.hr/'

    def parse(self, content):
        main_block = content.find_all('div', class_='tecajna-lista')[0].find_all('tbody')[0].find_all('td')
        rate = str(main_block[10]).replace('<td>','').replace('</td>','')
        return rate

    def email_message(self, data):
        return data['title']