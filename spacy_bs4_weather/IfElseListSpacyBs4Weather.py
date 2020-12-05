import requests
import bs4
import spacy

def SpacyAndBS4():
    nlp = spacy.load("en_core_web_md")
    miniWord = "music"
    web_page = requests.get("https://en.wikipedia.org/wiki/" + miniWord)
    if web_page is not None:
        html = bs4.BeautifulSoup(web_page.text, 'html.parser')
        text_paragraphs = html.select("p")
        document = '\n'.join([paragraph.text for paragraph in text_paragraphs[:3]])
        doc2 = nlp(document)
        for ent in doc2.ents:
            print(ent.text, ent.label_)

def weatherFunc(): #cityInput and countryInput
    city = cityInput
    country = countryInput
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "Enter Your API there",
        'useQueryString': 'true'
    }

    params = {
            'units': 'metric',
            'q': 'London,uk'
        }
    params['q'] = city+","+country[:2]
    r = requests.get(url, headers=headers, params=params)

    if 'json' in r.headers.get('Content-Type'):

        js = r.json()
        main = js['main']
        currentTemp = main['temp']
        print("Current temp: ", currentTemp)

    else:
        print('Response content is not in JSON format.')
        print(r.headers.get('Content-Type'))

cityInput = input("Please select city.. ")
countryInput = input("Country pls ")
weatherFunc()


howAreYouPositiveList = ['good', 'fine', 'very good']
howAreYouNegativeList = ["bad", "nothing much"]
ageAccess = list(range(15, 65))


answer = input("Whats your name? ")
print("Hi", answer)
answer = input("How are you? ")
if answer in howAreYouPositiveList:
    age = int(input("How old r u?  "))
    if age in ageAccess:
        print("ok")
    else:
        print("not ok")
# answer = input("Hello how are you ").lower()
# if answer in howAreYouPositiveList:
#     print("ok")