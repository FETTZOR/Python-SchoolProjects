import requests
import bs4

miniWord = "music"
web_page = requests.get("https://en.wikipedia.org/wiki/" + miniWord)
if web_page is not None:
    html = bs4.BeautifulSoup(web_page.text, 'html.parser')
    text_paragraphs = html.select("p")
    document = '\n'.join([paragraph.text for paragraph in text_paragraphs[:3]])
    print(document)