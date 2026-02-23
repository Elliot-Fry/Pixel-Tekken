import csv
import requests
from lxml import html

# Scraping guide: https://docs.python-guide.org/scenarios/scrape/

def get_bracket_link(eventName):
    # FUNCTION get_bracket_link
    # Extracts the link to an tournament's bracket from the event page
    
    prefix = 'https://www.start.gg/tournament/'
    suffix = '/events/singles/brackets'
    url = prefix + eventName + suffix
    
    print('Accessing URL: ', url)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    anchor = tree.xpath('//div[@class="phaseRows-sggOQ3xu"]')
     
    href = tree.xpath('//div[@class="phaseRows-sggOQ3xu"]/@href')

    print(anchor)
    print(href)
    print('\n\n___PAGE HTML: ___\n', page.content[:2000])
    



with open('Event-Scraping\event_links.csv',newline='') as csvf:
    reader = csv.reader(csvf)
    header = next(reader,None)
    for row in reader:
        bracketLink = get_bracket_link(row[0])
        break
        