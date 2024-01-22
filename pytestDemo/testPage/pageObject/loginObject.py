import time
# import sys
# import os
# # 获取当前脚本所在目录的绝对路径
# current_dir = os.path.dirname(os.path.abspath(__file__))
# # 将当前目录添加到模块搜索路径中
# sys.path.append(current_dir)
# from base.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginObject:
      def __init__(self,driver):
          self.driver = driver
          self.Email = (By.ID,"email")
          self.Pawd =  (By.ID,"password")
          self.Login =  (By.ID,"submit")
 
      def open_page(self):
          self.driver.get('https://www.vansky.com/user/login')
      def enter_username(self, username):
          self.driver.find_element(*self.Email).clear()
          time.sleep(2)
          self.driver.find_element(*self.Email).send_keys(username)
      def enter_pawd(self, password):
          self.driver.find_element(*self.Pawd).send_keys(password)
      def login_click(self):
          self.driver.find_element(*self.Login).click()
       



