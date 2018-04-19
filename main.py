from person import Korisnik
from speedup import Link
from data import data
from data import returnth



def main():
    l1 = 'https://www.kupujemprodajem.com/143524-1-tall-ocene.htm'
    l2 = 'https://www.kupujemprodajem.com/1590376-1-computer-dream-svi-oglasi.htm'
    links = [l1, l2]

    objectlist = [Korisnik(link) for link in links]

    ocenelinkova = [returnth.ThreadReturn(target=x.ocene) for x in objectlist]
    oglasi = [returnth.ThreadReturn(target=x.ime) for x in objectlist]


    myobj = Link(oglasi)
    myobj.getvalues()

if __name__ == '__main__':
    main()
