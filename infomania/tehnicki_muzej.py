

from .source import Source


class TehnickiMuzej(Source):

    def source_name(self):
        return 'tehnicki-muzej'

    def source_url(self):
        return 'http://tehnicki-muzej.hr/hr/kalendar/'

    def parse(self, content):
        return_data = []
        events = content.find('div', id='center').find_all('div', class_='d')

        for event in reversed(events):
            date_title = event.find('b').text.encode('utf-8')
            date, title = (str_.strip() for str_ in date_title.split('|'))

            if len(date.split('-')) > 1:
                date = date.split('-')[-1].strip()
            
            if date_title:
                return_data.append({
                    'date': date,
                    'title': title,
                    'link': 'http://tehnicki-muzej.hr' + event.find('a')['href'],
                })
            else:
                continue

        return return_data

    def email_message(self, data):
        return '{date}\n{title}\n{link}'.format(**data)