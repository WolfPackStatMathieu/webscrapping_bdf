from selenium import webdriver #import

website = 'https://www.adamchoi.co.uk/' #define website
#après téléchargement, mettre le lien  ver l'exécutable de chromedriver sans le .exe
#define a path where the chromedriver is
path = 'C:/Users/mathi/Downloads/chromedriver_win32/chromedriver'
driver = webdriver.Chrome(path) # create a driver to scrape the website
driver.get(website) #open a chromedriver window

driver.quit() #ferme le navigateur ouvert par selenium