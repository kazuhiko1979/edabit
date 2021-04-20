from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def dummy_sleep(sec, browser):

    wait = WebDriverWait(browser, 1)

    for i in range(sec):
        try:
            xpath = 'dummmy'
            wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        except:
            pass


def main():

    browser = webdriver.Chrome(executable_path='./chromedriver')

    browser.get('https://www.yahoo.com')

    xpath = '//*[@id="ybar-sbq"]'
    elem = browser.find_element_by_xpath(xpath)
    elem.send_keys('seleniumhq' + Keys.RETURN)

    dummy_sleep(5, browser)

    browser.close()
    browser.quit()


if __name__ == '__main__':
    main()