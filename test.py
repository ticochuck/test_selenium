# https://www.youtube.com/watch?v=GJjMjB3rkJM

from selenium.webdriver.common.keys import Keys
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.alaskaair.com/')


from_city = browser.find_element_by_id('fromCity1')


from_city.send_keys('SEA')

to_city = browser.find_element_by_id('toCity1')
to_city.send_keys('SJO')

dep_date = browser.find_element_by_id('departureDate1')
dep_date.clear()
dep_date.send_keys('11/30/20')


ret_date = browser.find_element_by_id('returnDate')
ret_date.clear()
ret_date.send_keys('2/15/21')
#dep_date.send_keys(Keys.TAB)


find_go = browser.find_element_by_id('findFlights')
find_go.click()


calendar =  browser.find_element_by_id('AvailType1')

browser.implicitly_wait(15)

calendar.click()