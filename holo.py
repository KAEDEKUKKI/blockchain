import requests
from bs4 import BeautifulSoup

class Hololive(object):

    def __init__(self, name):
        self.name = name

    def find(self):
        import requests
        from bs4 import BeautifulSoup
        site= "https://www.hololive.tv/portfolio/items/"+self.name
        hdr = {'User-Agent': 'Googlebot/2.1 (+http://www.google.com/bot.html)'}
        req = requests.get(site, headers=hdr)
        soup = BeautifulSoup(req.text,"html.parser")
        name = soup.find(class_="s-ecommerce-row-view-product-name")
        index = soup.find(class_="s-component-content s-font-body").select("p")
        data = {
            "名前":name.text,
        }
        for i in index:
            tag = i.text.split("：")[0]
            if tag!=i.text :
                data[tag]=i.text.split("：")[1]
        return data
