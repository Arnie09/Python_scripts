from selenium import webdriver
from time import sleep
import sys
import os

path = os.path.join(sys.path[0], 'chromedriver.exe')
state = False
'''taking the requisite inputs from the user'''
song = input("Enter the song you want to play or paste the url of the youtube video : ")
# print(song)
times = int (input("Enter the number of time you want to play the song in minutes: "))
sub = song[0:5]
#print(sub)

'''checking if the user has given name of song or youtube link'''
if(sub == "https"):
    #print("HI")
    url = song
    state = True
else:
    '''we will first search the song on google'''
    url = "https:\\www.google.com"



'''starting webdriver'''
driver = webdriver.Chrome(path)
driver.set_page_load_timeout(30)

if(state == False):
    
    driver.get(url)
    sleep(2)
    driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input').send_keys(song+" Youtube")
    driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[3]/center/input[1]').click()
    sleep(2)
    '''getting the link of the song'''
    link = driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[1]/div/div/div[1]/a').get_attribute("href")
    '''loop for the number of times the user wants'''
    while(times>0):
        driver.get(link)
        sleep(1)
        length_str = driver.find_element_by_class_name("ytp-time-duration").text
        min,sec = map(int,length_str.split(":"))
        time = min*60+sec
        #print(time)
        sleep(time)
        '''if time <100  then it has to be an add'''
        if(time>100):
            times -=time
else:
    while(times>0):
        driver.get(url)
        sleep(1)
        length_str = driver.find_element_by_class_name("ytp-time-duration").text
        min,sec = map(int,length_str.split(":"))
        time = min*60+sec
        #print(time)
        sleep(time)
        '''if time <100  then it has to be an add'''
        if(time>100):
            times -=time

driver.quit()