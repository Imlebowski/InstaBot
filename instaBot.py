import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

def save_name():
        file = open("Following_List.txt", "a+")
        file.write((driver.find_element_by_xpath("//article/header//h2/a").text) + '\n')
        file.close()

def follow():
    for i in range(1, 4):
        for j in range(1, 4):
                driver.find_element_by_xpath(f"//div[contains(@style, 'flex-direction')]//div[{i}]//div[{j}]//a").click()
                time.sleep(2)
                save_name()
                driver.find_element_by_xpath("//article/header//h2/a").click()
                time.sleep(4)
                driver.find_element_by_xpath("//button[text()='Follow']").click()
                driver.back()
                time.sleep(1)
                driver.back()
                # button = driver.find_element_by_xpath("//button[text()='Follow']/..")
                # driver.execute_script("return arguments[0].click()", button)
                # driver.find_element_by_tag_name("html").send_keys(Keys.ESCAPE)
                time.sleep(1)

def search_and_follow(tags):
    for tag in tags:
        driver.find_element_by_xpath("//input[@type='text']").send_keys(tag)
        time.sleep(2)
        driver.find_element_by_xpath(f"//span[text()='{tag}']").click()
        time.sleep(3)
        follow()

def read_tags():
    file = open('hashtags.txt', 'r')
    return file.read().splitlines()

def site_login():
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    time.sleep(1)
    driver.find_element_by_name("username").send_keys("username")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//button[text()='Not Now']").click()

site_login()
tags = read_tags()
search_and_follow(tags)
