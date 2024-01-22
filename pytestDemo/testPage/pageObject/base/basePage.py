import time
from selenium.webdriver import Keys

class BasePage:

    # 构造函数
    def __init__(self, driver):
        self.driver = driver

    # 访问
    def visit(self, url):
        self.driver.get(url)

    # 定位
    def locate(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def input(self, loc, txt):
        self.locate(loc).send_keys(txt)

    # 点击
    def click(self, loc):

        self.locate(loc).click()

          

 