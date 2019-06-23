import time
from selenium import webdriver

driver = webdriver.Chrome()

def unfollow():
    driver.find_element_by_xpath("//button[text()='Following']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//button[text()='Unfollow']").click()
    time.sleep(1)

def search_and_unfollow(followers):
    for follower in followers:
        driver.find_element_by_xpath("//input[@type='text']").send_keys(follower)
        time.sleep(1)
        driver.find_element_by_xpath(f"//span[text()='{follower}']").click()
        time.sleep(3)
        unfollow()

def read_followers():
    file = open('Following_List.txt', 'r')
    return file.read().splitlines()

def site_login():
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    time.sleep(2)
    driver.find_element_by_name("username").send_keys("username")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//button[text()='Not Now']").click()

site_login()
followers = read_followers()
search_and_unfollow(followers)