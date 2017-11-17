from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TaoBaoLianMeng:

    def __init__(self):
        self.url = "http://pub.alimama.com/"
        self.elements =[]
        self.result_url = []
        # self.driver = webdriver.Remote(command_executor='http://127.0.0.1:5555/wd/hub',
        #                                desired_capabilities=DesiredCapabilities.HTMLUNIT)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)

    def testTaoBao(self):

        self.driver.get(self.url)
        self.driver.find_element_by_class_name("search-inp input").send_keys("dress")
        time.sleep(1)
        self.driver.find_element_by_class_name("btn btn-brand search-btn").click()
        time.sleep(1)
        self.elements = self.driver.find_element_by_class_name("color-m")
        time.sleep(1)
        for element in self.elements:
            rel_url = element.get_attribute('href')
            self.result_url.append(rel_url)
        print(self.result_url)
        time.sleep(1)
        self.driver.quit()

    def getCountPages(self):
        count = (self.driver.find_element_by_class_name("btn btn-xlarge btn-white")[-2]).get_attribute("text")
        print(count)
        for i in range(int(count)):
            pass


if __name__ == "__main__":
    obj = TaoBaoLianMeng()
    obj.testTaoBao()
