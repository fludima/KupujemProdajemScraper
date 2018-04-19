import re
import requests
from bs4 import BeautifulSoup, SoupStrainer
import time


class Korisnik:

    def __init__(self, link):
        self.regex1 = re.compile(r'''(www.kupujemprodajem.com)\/(\d+)-''')
        self.link = link
        self.regexbase = re.search(self.regex1, self.link)
        self.base = self.regexbase.group(1)
        self.id = self.regexbase.group(2)
        self.htmlsoup = self.glavnastr()
        self.ocena = self.ocene()
        self.pozitivne = self.ocena[0]
        self.negativne = self.ocena[1]
        self.data = []

    def ocene(self):
        finder = self.htmlsoup.find_all(
            'span', class_='reviews-thumbs__thumb-number')
        likes = finder[0].text
        downlikes = finder[1].text
        return (likes, downlikes)

    def glavnastr(self):
        url = 'https://{0}/{1}-tall-ocene.htm'.format(self.base, self.id)
        stainer = SoupStrainer(id='reviewsPage')
        myrequest = self.data_request(url)
        mksoup = BeautifulSoup(myrequest, 'lxml', parse_only=stainer)
        return mksoup

    def bs4parse(self, url):
        myreq = requests.get(url).text
        return BeautifulSoup(myreq, 'lxml')

    def data_request(self, url):
        return requests.get(url).text

    def oglasi(self):
        url = 'https://{0}/{1}-1-svi-oglasi.htm'.format(self.base, self.id)
        makereq = self.bs4parse(url)
        if makereq.find('span', class_='error'):
            print('Error nema oglasa')
            return False
        return self.nadjioglase(makereq)

    def nadjioglase(self, data):
        '''Funkcija vraca SVE oglase

        Pozivanjem funkcije dace nam sve oglase odnosno
        sve detalje oglasa. Vazno je napomenuti da nece request-ovati
        svaki oglas pojedinacno, vec detalje oglasa uzima sa osnovne 
        (npr str. 1.) i na kraju dobijate listu. 

        Arguments:
            stranica -- prvobitna stranica za skrejpovanje

        Returns:
            listu -- slika, link, title, cena, pregled, lokacija
        '''
        c = lambda x: x.replace('\n', '').replace('\t', '').strip()
        # cuz i can

        mylist = []
        lista_proizvoda = data.find('div', id='adListContainer')
        proizvodi = lista_proizvoda.find_all(
            'div', class_='clearfix', recursive=False)
        sledeci = data.find('a', string='SledeÄa âº')
        # ako ima sledeca strana onda nastavlja sa skrejpovanjem
        # utf-8 ni unicode ne rade. Mora custom mapping ili ovako.

        for i in proizvodi[1:]:

            slika = i.div.section.div.div.a.div.img['src'].strip('//')
            link = i.div.find('section', class_='nameSec').div.a
            title = link.text
            link = '{}/{}'.format(self.base, link['href'].strip())
            cena = i.div.find(
                'section', class_='priceSec').span.text.replace('\xa0', '')
            pregled = i.div.find('section', class_='viewsSec').div.text
            lokacija = i.div.find('section', class_='locationSec').text

            templist = list(
                map(c, [slika, link, title, cena, pregled, lokacija]))
            mylist.append(templist)

        self.data.append(mylist)
        if sledeci:
            newreq = self.bs4parse(
                'https://{}/{}'.format(self.base.strip(), sledeci['href']))
            return self.nadjioglase(newreq)
        return self.data

    def ime(self):
        '''Vraca IME prodavca 

        Funkcija koja daje 
        Ime prodavca kojeg skrejpamo, lepo formatiran.

        Returns:
            Ime -- Ime KupujemProdajem Korisnika
        '''
        ime = self.htmlsoup.find(
            'h1', class_='reviews-header__title').text.strip()
        ime = ime.split('\t')
        # uzimamo samo ime zato split na \t i uklanjamo zadnje \n
        return ime[0][:-1]
