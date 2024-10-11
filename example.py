from screenShot import getScreenShot

screen = getScreenShot()

print(screen.getScreenWebSite())
# or get your custom url
print(screen.getScreenWebSite(url = "https://vk.ru/"))

screen.quitSession()
