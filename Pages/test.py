actual_links = ['HOME', 'LOCATIONS', 'EXPERIENCES', '', 'GIFT IDEAS', 'TICKETS', 'WEDDING REGISTRY', 'ABOUT',
                'FIND A COUPLE', '', '']
newlist = [item for item in actual_links if item.strip()]
print(newlist)
from datetime import datetime
today_date = datetime.today().date()
formatted_date = datetime.today().strftime('%d')
datenew = datetime.today().strftime('%d-%m-%Y')
print(datenew)