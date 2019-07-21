from selenium import webdriver
import time
#运行浏览器
driver = webdriver.Chrome()
driver.maximize_window()
#设置全局操作超时时间
driver.implicitly_wait(10)
#打开网址
driver.get('https://www.12306.cn/index/')
time.sleep(5)
driver.find_element_by_link_text("登录").click()
driver.find_element_by_link_text("账号登录").click()
driver.find_element_by_id("J-userName").send_keys("386817263@qq.com")
#driver.find_element_by_id("J-password").send_keys("*******")
print("continue")
time.sleep(20)
driver.find_element_by_link_text("首页").click()
time.sleep(3)
#出发地选择
driver.find_element_by_id("fromStationText").click()
driver.find_element_by_css_selector("#ul_list1 > li:nth-child(9)").click()
time.sleep(5)
#目的地选择
driver.find_element_by_id("toStationText").click()
driver.find_element_by_css_selector("#ul_list1 > li:nth-child(2)").click()
time.sleep(5)
#日期选择
driver.find_element_by_id("train_date").click()
driver.find_element_by_css_selector("body > div.cal-wrap > div:nth-child(1) > div.cal-cm > div:nth-child(26) > div").click()
time.sleep(5)
#选择动车
driver.find_element_by_id("isHighDan").click()
#查询
driver.find_element_by_id("search_one").click()
time.sleep(5)
driver.close()