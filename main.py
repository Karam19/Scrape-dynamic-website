import time

from selenium import webdriver
import chromedriver_binary
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


def fill_rich(rich):
    money = ""
    use = ""
    interest = ""
    fund = ""
    you = ""
    ps = []
    uls = []
    for r in rich.findAll('p'):
        if len(r.text) > 0:
            ps.append(r.text)
    for r in rich.findAll('ul'):
        uls.append(r.text)
    print(ps)
    print(uls)

driver = webdriver.Chrome()
driver.get("https://innovation.ised-isde.canada.ca/s/list-liste?language=en_CA&token=a0B5W000000WsFSUA0")
time.sleep(2)

# all_buttons = driver.find_elements(By.XPATH, '//*[@class="advanced-results brdr-tp lv-toggle--collapsed"]/div[1]/button[1]')
# for button in all_buttons:
#     button.click()
#     time.sleep(1)
driver.find_element(By.XPATH, '//*[@class="advanced-results brdr-tp lv-toggle--collapsed"]/div[1]/button[1]').click()
time.sleep(1)

h = driver.execute_script("return document.body.innerHTML;")
soup = BeautifulSoup(h, 'html.parser')
i = 0
print(soup.prettify())
for element in soup.findAll('div', {'class': ['advanced-results brdr-tp lv-toggle--collapsed']}):
    name = element.find('div', {'class': 'col-xs-11 list-sub-title'}).text
    short_des = element.find('div', {'class': 'h4 mrgn-tp-0'}).text
    long_des = element.find('p', {'class': 'program-dov-description'}).text
    status = element.find('div', {'class': 'mrgn-lft-xl'})
    status_text = ""
    for p in status.findAll('p'):
        status_text = status_text + '\n' + p.text
    rich_text = element.find('p', {'class': 'rich_text'})
    print(i)
    print(name)
    print(short_des)
    print(long_des)
    print('*************')
    print(status_text)
    # print(rich_text)
    fill_rich(rich_text)
    i = i + 1
