import selenium
import time
import t2
import t1

from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


print("trying to find links")

interests = t2.get_interests()
interests=interests[:5]


def get_links(element):

    list1=[]
    for x in element:

        list1.append(x.get_attribute("href"))


    return list1

driver = webdriver.Chrome("/Users/chaitanyamalik/Desktop/chromedriver")


def return_links(base_url):
    links=[]



    try:
        driver.get(base_url)
        links_last=driver.find_elements(By.XPATH,"//a")
        links_last = get_links(links_last)
        links+=links_last
    except:
        pass



    try:
        driver.get(base_url)

        links_new = driver.find_elements(By.XPATH, "//a")
        print(len(links_new))
        links_new = get_links(links_new)
        links_list = []

        m = 0
        for i in links_new:
            driver.get(i)
            print(f"iteration : {m}")
            m += 1
            if m==20:
                break
            time.sleep(3)
            list1 = driver.find_elements(By.XPATH, "//a")
            list1 = get_links(list1)
            links_list += list1


        links+=links_list
    except:
        pass

    time.sleep(5)

    driver.quit()

    with open("links1.txt","w") as f:
        f.write(str(links))

    return links,base_url















