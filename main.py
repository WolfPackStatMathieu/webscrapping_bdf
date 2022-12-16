from selenium import webdriver #import
from selenium.webdriver.support.ui import Select #pour gére rles dropdowns
import pandas as pd
import time

website = 'https://www.adamchoi.co.uk/overs/detailed' #define website
#après téléchargement, mettre le lien  ver l'exécutable de chromedriver sans le .exe
#define a path where the chromedriver is
path = 'C:/Users/mathi/Downloads/chromedriver_win32/chromedriver'
driver = webdriver.Chrome(path) # create a driver to scrape the website
driver.get(website) #open a chromedriver window

#on veut le bouton "fin all"
all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]') #attention à utiliser les doubles quotes/single quotes
all_matches_button.click()


dropdown = Select(driver.find_element_by_id('country'))
dropdown.select_by_visible_text('Spain')
#loading page, takes a couple of seconds
time.sleep(3) #laisse 3 secondes avant d'exécuter la ligne de code suivante





#'tr' est le nom de l'élément pour chaque ligne du tableau
matches = driver.find_elements_by_tag_name('tr') #avec un s pour en trouver plusieurs

# préparation des variables individuelles
date = [] #empty list
home_team = []
score = []
away_team = []

for match in matches:
    # pour indiquer le current context
    date.append(match.find_element_by_xpath('./td[1]').text)
    home = match.find_element_by_xpath('./td[2]').text
    home_team.append(home)
    print(home)
    score.append(match.find_element_by_xpath('./td[3]').text)
    away_team.append(match.find_element_by_xpath('./td[4]').text)


driver.quit() #ferme le navigateur ouvert par selenium

df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, "away_team": away_team})
df.to_csv('footbal_data.csv', index=False )
print(df)