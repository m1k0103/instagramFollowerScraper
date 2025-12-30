import requests
from bs4 import BeautifulSoup
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By

def scrape_followers():
    pass

#driver = webdriver.Firefox()
#driver.get("https://instagram.com/{}")
#assert "Python" in driver.title
#elem = driver.find_element(By.NAME, "q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()

def resolveUsernameToID(username):
    r = requests.get(f"https://www.instagram.com/{username}/") # searching for profilepage_ gets the uid so just get source of page and get id
    print(r.text)
    soup = BeautifulSoup(r.text)
    
    pass


def getAllPostIDS(username):
    
    pass


def scrapePostLikes(username):
    userID = resolveUsernameToID(username)
    allPostIds = getAllPostIDS()
    for p in allPostIds:
        url = f"https://www.instagram.com/api/v1/media/{p}/likers/"



instaId = scrapePostLikes("compsockent")
