
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import os

# OPTIONS = webdriver.FirefoxOptions()
SERVICE = Service("/home/hoods/Documents/development/geckodriver")
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('subarupython!')
URL = "https://www.instagram.com/accounts/login/"
ACCOUNT_TO_FOLLOW = "linuxmintofficial"

def q_rest():
    time.sleep(3)


def rest(x):
    time.sleep(x)


class InstaFollower:

    def __init__(self):
        self.dr = webdriver.Firefox(service=SERVICE)
        self.follow_buttons = []

    def login(self):
        self.dr.get(URL)
        self.dr.maximize_window()
        q_rest()
        user_entry = self.dr.find_element(By.NAME, "username")
        user_entry.click()
        user_entry.send_keys(USERNAME)
        q_rest()
        pass_entry = self.dr.find_element(By.NAME, "password")
        pass_entry.click()
        pass_entry.send_keys(PASSWORD)
        q_rest()
        login = self.dr.find_element(By.CSS_SELECTOR, "button._acan._acap._acas._aj1-")
        login.click()
        rest(10)

    def find_followers(self):
        search_button = self.dr.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div['
                                                       '1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div/div['
                                                       '2]/div/div')
        search_button.click()
        q_rest()
        search_input = self.dr.find_element(By.CLASS_NAME, "_aauy")
        search_input.send_keys(ACCOUNT_TO_FOLLOW)
        q_rest()
        search_object = self.dr.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div["
                                                       "1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a")
        search_object.click()
        q_rest()
        follower_count = self.dr.find_element(By.PARTIAL_LINK_TEXT, "followers")
        follower_count.click()
        q_rest()
        follower_box = self.dr.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div["
                                                      "2]/div/div/div/div/div[2]/div/div/div[2]")
        follow_buttons = self.dr.find_elements(By.CLASS_NAME, "_acan _acap _acas _aj1-")
        for x in range(10):
            self.dr.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_box)
            q_rest()
            self.follow_buttons.append(self.dr.find_elements(By.XPATH,
                                                             '//button[contains(@class, "_acan") and contains(@class, "_acap") and contains(@class, "_acas") and contains(@class, "_aj1-")]'))

    def follow(self):
        res = sum(self.follow_buttons, [])
        pop_res = {button for button in res}
        for button in pop_res:
            try:
                button.click()
                q_rest()
            except (NoSuchElementException, ElementClickInterceptedException):
                pass
