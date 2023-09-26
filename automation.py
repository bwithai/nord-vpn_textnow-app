from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from vpn import nordvpn_disconnect


def perform_automation():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('start-maximized')

    driver = webdriver.Chrome()

    driver.get('https://api.ipify.org')
    ip = driver.find_element(By.TAG_NAME ,"body").text
    print(f"\nWith Selenium after nord connect\nIp:\t{ip}")
    input("press enter to continue: ")

    url = "https://www.textnow.com/login"
    driver.get(url)

    # Wait until the page is fully loaded
    wait = WebDriverWait(driver, 20)  # Wait up to 10 seconds

    username_element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, 'txt-username')))
    username_element.send_keys('knighttigers2211@gmail.com')

    password_element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, 'txt-password')))
    password_element.send_keys('slanty123')

    try:
        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, 'btn-login')))
        login_button.click()

        input("solve the captcha and then press enter: ")

        # driver.get("https://www.textnow.com/messaging")
        # time.sleep(10)

    except Exception as e:
        print(e)

    finally:
        # Disconnect NordVPN after automation is complete
        nordvpn_disconnect()
