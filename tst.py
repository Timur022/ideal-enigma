from datetime import datetime
from selenium import webdriver
import string

temp = False
date = ''
group = ''
kalendar = ''
load = ''
all_kalendar = ''
mon = ''
right = ''
# while True:
    # if temp == False and datetime.now().strftime('%T') == '16:22:00':
temp = True
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/home/ubuntu/bot1/bo1/jsn/chromedriver',chrome_options=chrome_options)
driver.get('http://uc.osu.ru/asd.php')
date_all = {
    1: 'v1', 2: 'v2', 3: 'v3', 4: 'v4', 5: 'v5', 6: 'v6', 7: 'v7', 8: 'v8', 9: 'v9', 10: 'v10',
    11: 'v11', 12: 'v12', 13: 'v13', 14: 'v14', 15: 'v15', 16: 'v16', 17: 'v17', 18: 'v18', 19: 'v19', 20: 'v20',
    21: 'v21', 22: 'v22', 23: 'v23', 24: 'v24', 25: 'v25', 26: 'v26', 27: 'v27', 28: 'v28', 29: 'v29', 30: 'v30',
    31: 'v31', 32: 'v32', 33: 'v33', 34: 'v34', 35: 'v35', 36: 'v36', 37: 'v37', 38: 'v38', 39: 'v39', 40: 'v40',
    41: 'v41', 42: 'v42'
}
kalendar = driver.find_element_by_xpath("//table[@id='fc']")
load = driver.find_element_by_id("load")
all_kalendar = kalendar.find_element_by_tag_name("td")
mon = kalendar.find_element_by_xpath("//td[@id='mns']")
right = kalendar.find_element_by_xpath("//td[@align='right']")
for i in range(1, 42):
    kd = driver.find_element_by_id(date_all[i])
    if kd.value_of_css_property('cursor') == 'pointer':
        date = kd.text
        kd.click()
        while load.value_of_css_property('display') != 'none':
            load1 = 1
        elem1 = driver.find_element_by_id("error")
        if elem1.value_of_css_property('display') != 'block':
            element = driver.find_element_by_xpath("//select[@id='type_user_id']")
            all_options = element.find_elements_by_tag_name("option")
            for option in all_options:
                if option.get_attribute("value") == "1":
                    option.click()
                    while load.value_of_css_property('display') != 'none':
                        load1 = 1
            element1 = driver.find_element_by_xpath("//select[@id='group_pick']")
            all_options1 = element1.find_elements_by_tag_name("option")
            for b in all_options1:
                b.click()
                while load.value_of_css_property('display') != 'none':
                    load1 = 1
                for element in driver.find_elements_by_id("tabdata"):
                    group = b.text
                    with open('//home//timur//bot1//bo1//Rasp//' + date + '_' + group.replace(' ', '') + '.txt', 'w+') as f:
                        f.write(element.text)
right.click()
for i in range(1, 42):
    kd = driver.find_element_by_id(date_all[i])
    if kd.value_of_css_property('cursor') == 'pointer':
        date = kd.text
        kd.click()
        while load.value_of_css_property('display') != 'none':
            load1 = 1
        elem1 = driver.find_element_by_id("error")
        if elem1.value_of_css_property('display') != 'block':
            element = driver.find_element_by_xpath("//select[@id='type_user_id']")
            all_options = element.find_elements_by_tag_name("option")
            for option in all_options:
                if option.get_attribute("value") == "1":
                    option.click()
                    while load.value_of_css_property('display') != 'none':
                        load1 = 1
            element1 = driver.find_element_by_xpath("//select[@id='group_pick']")
            all_options1 = element1.find_elements_by_tag_name("option")
            for b in all_options1:
                b.click()
                while load.value_of_css_property('display') != 'none':
                    load1 = 1
                for element in driver.find_elements_by_id("tabdata"):
                    group = b.text
                    with open('//home//timur//bot1//bo1//Rasp//' + date + '_' + group.replace(' ', '') + '.txt', 'w+') as f:
                        f.write(element.text)
driver.close()
temp = False
