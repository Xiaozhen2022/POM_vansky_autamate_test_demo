<!-- https://gitee.com/wesion01/automated-test-pom-pytest/tree/master -->
Frame: selenium+pytest+allure
google search allure frame download in windows:https://allurereport.org/docs/gettingstarted-installation/
install allure:
C:\Users\myf\Downloads\allure-2.26.0\allure-2.26.0\bin
pc--properties--advanced system setting--environment var--path--
install java: 
C:\Program Files\Java\jdk-21\bin

visit https://www.vansky.com/user/login
test login function
pytest --alluredir=./results  
In windows command line will generate report: allure serve D:\MyLab\seleniumProject\POM_vansky_demo\pytestDemo\testPage\results
The reports will generate in temp folder: C:\Users\myf\AppData\Local\Temp\3025264090457655168\allure-report

How to share the report?
https://www.netlify.com/ 
sign in
pull the temp folder to the manual site and generate a sharing url:https://snazzy-squirrel-6fc2f2.netlify.app
