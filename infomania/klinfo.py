

from .source import Source


class Klinfo(Source):

    def source_name(self):
        return 'klinfo'

    def source_url(self):
        return 'http://www.klinfo.hr/?post_type=event&event_filter=1&event_category=0&event_location=26&event_date='

    def parse(self, content):
        return_data = []
        events = content.find_all('div', class_='col-sm-6')
        for event in reversed(events):
            
            date_price = event.find('div', class_='event-info')
            
            if date_price:
                date = date_price.find('span', itemprop='startDate').text.encode('utf-8')
                if len(date.split('/')) > 1:
                    date = date.split('/')[0].strip()
                    
                return_data.append({
                    'date': date,
                    'age': date_price.find('span', itemprop='typicalAgeRange').text.encode('utf-8'),
                    'price': date_price.find('span', itemprop='offers').text.encode('utf-8'),
                    'title': event.find('h4', class_='media-heading').text.encode('utf-8'),
                    'location': event.find('span', itemprop='location').text.encode('utf-8'),
                    'link': event.find('a')['href'],
                })
            else:
                continue

        return return_data

    def email_message(self, data):
        return '{date} | {age} | {price}\n{title}\n{location}\n{link}'.format(**data)