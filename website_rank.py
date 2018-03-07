from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from pyvirtualdisplay import Display

class rank_predict:

    def __init__(self):

        self.display = Display(visible=0, size=(1024, 768))
        self.display.start()
        self.driver=webdriver.Chrome()
        self.driver.get(url='https://www.google.com')
        self.timeout = 100



    def search_google(self,search_string):


        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'tsf'))
            WebDriverWait(self.driver, self.timeout).until(element_present)

        except TimeoutException:
            print("Timed out waiting for page to load")

        search_bar = self.driver.find_element_by_xpath('//*[@id="lst-ib"]')      #Locating the search bar on page
        self.driver.execute_script('arguments[0].click();',search_bar)
        send_keys=search_bar.send_keys(search_string + Keys.ENTER)               #Sending Keys to the search bar
    def get_links(self):

        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'mw'))
            WebDriverWait(self.driver, self.timeout).until(element_present)

        except TimeoutException:
            print("Timed out waiting for page to load")

        links_text=[]
        links_as_webelement=self.driver.find_elements_by_css_selector('div.f._Oe._SWb')    #Finding all the links
        for i in range(0,len(links_as_webelement)):
            if (links_as_webelement[i].text)!='':
                links_text.append(links_as_webelement[i].text)
        print(links_text)

class_object=rank_predict()
string_to_search='Enter Search String'                              #Enter the seacr string for which you want to get links
class_object.search_google(string_to_search)
class_object.get_links()


