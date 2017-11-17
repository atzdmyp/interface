import requests
from bs4 import BeautifulSoup
import pdfkit
import os


# 将html页面转换成pdf文件
class HTMLTOPDF:
    def __init__(self):
        self.url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
        self.response = None
        self.soup = None
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
        }
        self.file1 = None

    def get_html(self):
        """
        get html page and save to file
        :return:
        """
        self.response = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.response.content, "html.parser")
        mulu = self.soup.find_all(class_="uk-panel")
        #html = self.response.text
        self.file1 = r"F:\test\b.html"
        with open(self.file1, "w", encoding='utf-8') as f:
            f.write(str(mulu))

    def get_url_list(self):
        """
        获取所有URL目录列表
        """
        menu_tag = self.soup.find_all(class_="uk-nav uk-nav-side")[3]
        urls = []
        for li in menu_tag.find_all("li"):
            url = "http://www.liaoxuefeng.com" + li.a.get('href')
            urls.append(url)
        return urls

    def get_htmls(self):
        """

        :return:
        """
        urls = self.get_url_list()
        pages = [self.file1]
        i = 0
        for url in urls:
            self.response = requests.get(url, headers=self.headers)
            self.soup = BeautifulSoup(self.response.content, "html.parser")
            html = self.soup.find_all(class_="x-wiki-content x-main-content")
            str(html).replace(r'src="', r'src="http://www.liaoxuefeng.com')

            post = str(html).find("src=\"")
            if post != -1:
                html = str(html)[:post+len("src=\"")] + "http://www.liaoxuefeng.com" + str(html)[post+len("src=\""):]

            file = "F:\\test\\a%s.html" % i
            with open(file, 'w', encoding='utf-8') as f:
                f.write(str(html))
            i += 1
            pages.append(file)
        return pages

    def save_pdf(self):
        """
        把所有html文件转换成pdf文件
        """
        options = {
            'page-size': 'Letter',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ]
        }
        config = pdfkit.configuration(wkhtmltopdf=r'D:\workprogram\wkhtmltopdf\bin\wkhtmltopdf.exe')
        htmls = self.get_htmls()
        pdfkit.from_file(htmls, r"F:\test\python.pdf", options=options, configuration=config)

    def delete_htmls(self):
        """

        :return:
        """
        htmls = self.get_htmls()
        for i in htmls:
            os.remove(i)


if __name__ == "__main__":
    obj = HTMLTOPDF()
    obj.get_html()
    obj.save_pdf()
