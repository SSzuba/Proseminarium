from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys
import re

#zdefiniowanie sterownika znajdującego się w kontenerze z obrazem Selenium w Dockerze
#driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub',options=webdriver.ChromeOptions())

#zdefiniowanie sterownika znajdującego się lokalnie w projekcie 
driver = webdriver.Chrome()

#pobranie adresu url strony z poziomu terminala jako argument
url = str(sys.argv[1])
#przypisanie adresu strony do sterownika
driver.get(url)
#akceptacja regulaminu ciasteczek strony
driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
#pobranie wszystkim elementów strony typu button
buttons = driver.find_elements(By.TAG_NAME, 'button')
#przeszukanie wszystkich przycisków na stronie oraz odnalezienie i wciśnięcie przycisku odpowiedzialnego za wyświetlenie numeru telefonu
for b in buttons:
    if b.text == 'Pokaż':
        b.click()
        time.sleep(2)
        #pobranie wszystkich elementów typu span
        spans = driver.find_elements(By.TAG_NAME, 'span')

#sprawdzenie pobranych elementów span w celu odnalezienia numeru telefonu
for s in spans:
    #000 000 000
    numer_check_1 = re.search(r"[\d]{3} [\d]{3} [\d]{3}", s.text)
    #000-000-000
    numer_check_2 = re.search(r"[\d]{3}-[\d]{3}-[\d]{3}", s.text)
    #000000000
    numer_check_3 = re.search(r"[\d]{3}[\d]{3}[\d]{3}", s.text)
    if numer_check_1 != None:
        if s.text == numer_check_1.string:
            #wyświetlenie numeru telefonu w formacie 000 000 000
            print('Numer tel z ogłoszenia: ', s.text)
    elif numer_check_2 != None:
        if s.text == numer_check_2.string:
            #wyświetlenie numeru telefonu w formacie 000-000-000
            print('Numer tel z ogłoszenia: ', s.text)
    elif numer_check_3 != None:
        if s.text == numer_check_3.string:
            #wyświetlenie numeru telefonu w formacie 000000000
            print('Numer tel z ogłoszenia: ', s.text)
    
        
    
#zamknięcie sterownika
driver.close()
driver.quit()
