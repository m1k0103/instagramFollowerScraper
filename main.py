import requests
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

def resolveInstagramID(username):
    url = """https://www.instagram.com/graphql/query?variables={"userID":"40459854417","username":"xanderzero_"}"""
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "x-ig-app-id": "936619743392459"
    }
    r = requests.get(url,headers)
    print(r.status_code)



def scrape(instagramID):
    url = f"https://www.instagram.com/api/v1/friendships/{instagramID}/followers/?count=12&search_surface=follow_list_page"
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "x-ig-app-id": "936619743392459",
    }
    r = requests.get(url=url,headers=headers)
    print(r.status_code)

instaId = resolveInstagramID("compsockent")

scrape(instaId)