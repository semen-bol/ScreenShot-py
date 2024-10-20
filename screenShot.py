import string, random

from selenium import webdriver

def genNaming(length):
        characters = string.ascii_letters + string.digits
        name = ''.join(random.choice(characters) for _ in range(length))
        return name

class getScreenShot():
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
    
    def getScreenWebSite(self, url = "https://google.com/"):
        str = f"{genNaming(30)}.png"

        self.driver.get(url)
        self.driver.save_screenshot(str)

        return str

    def quitSession(self):
        self.driver.quit()
