from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

import uuid


class LoginTest(LiveServerTestCase):

    def test_account(self):
        selenium = webdriver.ChromeOptions()
        selenium.add_argument('--no-sandbox')
        selenium.add_argument('--window-size=1920,1080')
        selenium.add_argument('--headless')
        selenium.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=selenium)

        driver.get('http://0.0.0.0:8000/signup/')  # Docker on Github does not accept localhost?
        username = driver.find_element(By.ID, 'id_username')
        email = driver.find_element(By.ID, 'id_email')
        password = driver.find_element(By.ID, 'id_password')
        signup = driver.find_element(By.XPATH, '//button[normalize-space()="Submit"]')

        stamp = str(uuid.uuid4())  # LiveServerTestCase don't tear down db https://github.com/behave/behave/issues/1040
        usr_text = 'test_selenium_user' + stamp
        email_text = 'seleniumtest' + stamp + '@selenium.net'
        pwd_text = 'test_selenium_pwd'

        username.send_keys(usr_text)
        email.send_keys(email_text)
        password.send_keys(pwd_text)
        signup.submit()
        self.assertTrue("Login" in driver.page_source)  # redirected to login

        username = driver.find_element(By.ID, 'id_username')
        password = driver.find_element(By.ID, 'id_password')
        login = driver.find_element(By.XPATH, '//button[normalize-space()="Login"]')
        username.send_keys(usr_text)
        password.send_keys(pwd_text)
        login.submit()

        self.assertTrue("Could not authenticate" in driver.page_source)  # not registered yet

        username = driver.find_element(By.ID, 'id_username')
        password = driver.find_element(By.ID, 'id_password')
        login = driver.find_element(By.XPATH, '//button[normalize-space()="Login"]')
        username.send_keys('test_user')  # KNOWN USER DO NOT DELETE
        password.send_keys('test_pwd')
        login.submit()
        self.assertTrue("Logged in" in driver.page_source)  # known user can log in
