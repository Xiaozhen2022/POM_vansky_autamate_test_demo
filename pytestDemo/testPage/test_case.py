import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import sys
import os
import allure
from allure_commons.types import AttachmentType
# 获取当前脚本所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
# 将当前目录添加到模块搜索路径中
sys.path.append(current_dir)
from pageObject.loginObject import LoginObject
from config.loadYaml import loadYaml

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    lg=LoginObject(driver)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.parametrize('userData', loadYaml('./data/user.yaml'))    
@allure.severity(allure.severity_level.MINOR)
def test_login(driver, userData):
    print(userData)
    lg=LoginObject(driver)
    lg.open_page()
    driver.implicitly_wait(3)
    # lg.enter_username('8560415@qq.com')
    lg.enter_username(userData['Email'])
    time.sleep(3)
    # lg.enter_pawd('Test@2022')
    lg.enter_pawd(userData['Password']) 
    time.sleep(1)
    lg.login_click()
    driver.implicitly_wait(3)
    if "Incorrect" not in driver.page_source:
        assert True
    else:
        allure.attach(driver.get_screenshot_as_png(),name="testLoginScreen", attachment_type=AttachmentType.PNG)
        assert False
    # assert "Incorrect" not in driver.page_source
  
if __name__ == '__main__':
    # pytest.main(['-s', __file__, '--alluredir', './allureResults'])
    # allure_command = 'allure generate ./allureResults -o ./reports --clean'
    pytest.main(['test_case.py', '--alluredir', './results','--clean-alluredir'])
    os.system('allure generate ./results -o ./reports --clean')
  
   


