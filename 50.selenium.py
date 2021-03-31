from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup

def dummy_wait(driver):

    wait_sec = 3

    try:
        wait = WebDriverWait(driver, wait_sec)
        wait.until(EC.title_contains("Dummy"))
    except:
        pass


def main():

    url = "https://www.google.co.jp"

    driver = webdriver.Firefox()
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    xpath = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
    wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    elem = driver.find_element_by_xpath(xpath)
    elem.send_keys("Udemy")
    elem.send_keys(Keys.ENTER)

    dummy_wait(driver)

    class_ = "LC20lb"
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, class_)))
    elem = driver.find_element_by_class_name(class_)
    elem.click()

    dummy_wait(driver)

    soup = BeautifulSoup(driver.page_source)
    print(soup.prettify())

    dummy_wait(driver)

    driver.quit()

    return


if __name__ == "__main__":

    main()

