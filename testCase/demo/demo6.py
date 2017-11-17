import os
import requests
from bs4 import BeautifulSoup
import urllib
import urllib.request


class Crawler:
    def __init__(self):
        global crawlerPath, htmlPath, productPath, imagePath
        crawlerPath = os.path.join(r'F:\AppTest', 'Crawler')
        htmlPath = os.path.join(r'F:\AppTest', 'Crawler', 'html.html')
        productPath = os.path.join(r'F:\AppTest', 'Crawler', 'product.txt')
        imagePath = os.path.join(r'F:\AppTest', 'Crawler', 'images')
        if not os.path.exists(crawlerPath):
            os.mkdir(crawlerPath)
        if not os.path.exists(imagePath):
            os.mkdir(imagePath)
        self.url = 'http://www.shein.com/women-dresses-c-1727.html?icn=dresses&ici=www_navbar03'
        self.html = ''
        print(u"爬虫准备就绪！")

    def set_html_page(self):
        """

        :return:
        """
        self.html = requests.get(self.url).text
        f = open(htmlPath, 'w', encoding='UTF-8')
        f.write(self.html)
        f.close()
        print(u"页面已保存在"+htmlPath)

    def new_soup(self):
        """

        :return:
        """
        soup = BeautifulSoup(open(htmlPath, encoding='UTF-8'), "lxml")
        # f = open("F:\AppTest\Crawler\soup.html", 'w', encoding='UTF-8')
        # f.write(soup.prettify())
        # f.close()
        return soup

    def download_img(self):
        """

        :return:
        """
        soup = self.new_soup()
        name = ''
        for m in soup.find_all('img'):
            if m.has_attr('alt') and str(m.get("src")).startswith("http"):
                img_url = m.get('src')
                point = str(img_url).split(".")[-1]
                if point == "jpg":
                    file_name = str(m.get('src')).split('/')[-1]
                    img_path = os.path.join(imagePath, file_name)
                    name = name + m.get("alt") + "\t" + m.get("src") + "\n"
                    # print(u"图片" + file_name + "准备下载")
                    # download image
                    urllib.request.urlretrieve(img_url, filename=img_path)
                    print(u"图片"+file_name+"已下载")
        print(u"所有图片下载完毕!")
        print(u"图片下载路径："+imagePath)
        fb = open(productPath, "w")
        fb.write(name)
        fb.close()
        print(u"图片信息已保存到："+productPath)

    def write_name_to_file(self):
        """

        :return:
        """
        soup = self.new_soup()
        name = ''
        for m in soup.find_all("img"):
            if m.has_attr("alt"):
                name = m.get("alt")+"\t"+m.get("src")+"\n"

        fb = open(productPath, "w")
        fb.write(name)
        fb.close()


if __name__ == "__main__":
    obj = Crawler()
    obj.set_html_page()
    obj.download_img()
