from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from pyvirtualdisplay import Display       # Comment this if using windows
class rank_predict:

    def __init__(self):

        self.display = Display(visible=0, size=(1024, 768))        # Comment this if using windows
        self.display.start()                                        # Comment this if using windows
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

        self.links_text=[]
        self.links_as_webelement=self.driver.find_elements_by_css_selector('div.f._Oe._SWb')    #Finding all the links
        for i in range(0,len(self.links_as_webelement)):
            if (self.links_as_webelement[i].text)!='':
                self.links_text.append(self.links_as_webelement[i].text)

    def search(self,search,stringtosearch):
        sum=0
        self.page=1

        while self.page<10:
            self.get_links()
            count=0
            counter=0
            for i in range(0,len(self.links_text)):
                if search in self.links_text[i]:
                    counter+=1
                    if self.page==1:
                        print('Rank of  '+ str(search) +' for the search  '+str(stringtosearch)+ ' is :' +str(i+1))
                        print('\n')
                        print('Searched website found on page ' + str(self.page))
                    else:
                        print('Rank of  ' + str(search) + ' for the search  ' + str(stringtosearch) + ' is :' + str(sum+(i + 1)))
                        print('\n')
                        print('Searched website found on page ' + str(self.page))
                    for i in range(0,i):
                        if count==0:
                            print('\n')
                            print('Top websites on top of the searched Website are : ')
                            print('\n')
                            count+=1
                        print(self.links_text[i])
            sum+=len(self.links_text)

            if counter!=0:
                break
            else:
                print('Not found on page ' + str(self.page))
                print('\n')
                click_next_page=self.driver.find_element_by_xpath('//*[@id="pnnext"]/span[2]')
                self.driver.execute_script('arguments[0].click();',click_next_page)
            self.page+=1
        self.driver.get(url='https://www.google.com')


name_of_website=''                      # Enter the website whose rank you want to predict
filepath='String.txt'
class_object=rank_predict()
with open(filepath) as fp:
    line=fp.readlines()
for i in range(0,len(line)):
    print('\n')
    print(line[i])
    string_to_search=line[i]
    class_object.search_google(string_to_search)
    class_object.search(name_of_website,string_to_search)
class_object.driver.quit()


