from selenium import webdriver
import time


class ScreenShot:

    def screenShot(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(6)
        driver.get("http://pub.alimama.com/")
        time.sleep(5)

        driver.get_screenshot_as_file("F:\screenShot1.png")
        driver.get_screenshot_as_png()
        driver.get_screenshot_as_base64()
        driver.quit()


if __name__ == "__main__":
    obj = ScreenShot()
    obj.screenShot()
