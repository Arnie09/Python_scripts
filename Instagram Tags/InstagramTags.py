from selenium import webdriver
from time import sleep
import sys
import os

path = os.path.join(sys.path[0], 'chromedriver.exe')
choice = int(input("Enter 1 for facebook log in 2 for email login : "))
email = input("Enter the email : ")
password = input("Enter the password : ")
tag = input("Enter the tag you want to search for : ")
number_of_tags = int(input("Enter the number of tags that you want : "))

url1 = "https://www.instagram.com"
driver = webdriver.Chrome(path)
driver.set_page_load_timeout(30)
driver.get(url1)
if (choice == 1):
    # statements for facebook login
    driver.find_element_by_xpath("//section/main/article/div[2]/div[1]/div/form/div[1]/button").click()
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("pass").send_keys(password)
    driver.find_element_by_name("login").click()
elif(choice == 2):
    # statements for email login
    driver.find_element_by_xpath("//section/main/article/div[2]/div[2]/p/a").click()
    sleep(5)
    driver.find_element_by_name("username").send_keys(email)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_xpath("//section/main/div/article/div/div[1]/div/form/div[3]/button").click()   


ListofElements = []
sleep(3)
url = "https://www.instagram.com/explore/tags/"+tag+"/"
print(url)
driver.get(url)
tag = "#"+tag
driver.find_element_by_xpath(
    "//section/nav/div[2]/div/div/div[2]/input").send_keys(tag)
print("Okay")
sleep(2)
print(driver.find_element_by_class_name("Ap253").text)
ListofElements = driver.find_elements_by_class_name("Ap253")
c = 0
for items in ListofElements:
    print(items.text)
    c += 1
    if(c == number_of_tags):
        break
driver.quit()
