from selenium import webdriver
from time import sleep
import sys
import os

path = os.path.join(sys.path[0], 'chromedriver.exe')
driver = webdriver.Chrome(path)
choice = int(input("Enter 1 for facebook log in 2 for email login : "))
email = input("Enter the email : ")
password = input("Enter the password : ")
tag = input("Enter the tag you want to search for : ")
limit = int(input("Enter how many pictures you want to like?"))
time = (limit * 5) + 4
print("It will take approximately ",time,"seconds to run!")

url1 = "https://www.instagram.com"
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
    driver.find_element_by_name("username").send_keys(email)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_xpath("//section/main/div/article/div/div[1]/div/form/div[3]/button").click()   


ListofElements = []
sleep(3)

url = "https://www.instagram.com/explore/tags/"+tag+"/"

driver.get(url)
#write code for the like part here!
driver.find_element_by_xpath("//section/main/article/div[1]/div/div/div[1]/div[1]").click()
sleep(1)
#clicking the first like 
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/article/div[2]/section[1]/span[1]").click()
sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/a").click()
sleep(2)
for i in range(limit-1):
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/article/div[2]/section[1]/span[1]/button/span").click()
    sleep(3)
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/a[2]").click()
    sleep(2)
driver.quit()
