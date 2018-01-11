import requests
import bs4

def getHtmlText(url):
    try:
        r= requests.get(url)
        r.raise_for_status()
        r.encoding =  r.apparent_encoding
        return r.text
    except:
        print("failtogetHTML")
        

def doi(tlist, htmltext):
    soup = bs4.BeautifulSoup(htmltext, "html.parser")
    for tr in soup.tbody.children:
        if isinstance (tr, bs4.element.Tag):
            tds = tr('td')
            tlist.append([tds[0].string, tds[1].string, tds[3].string])

def show(tlist, num):
    print("{:<10}\t{:<20}\t{:<20}".format("range","school","grade"))
    for i in range(num):
        u=tlist[i]
        print("{:<10}\t{:<20}\t{:<20}".format(u[0],u[1],u[2]))


def main():
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    tlist = []
    htmltext = getHtmlText(url)
    doi(tlist, htmltext)
    show(tlist, 20)

main()



