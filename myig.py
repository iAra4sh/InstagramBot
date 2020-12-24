#Ican Do This

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
from docopt import docopt
from termcolor import colored
import stdiomask


usage = ''' 
Usage:
    myig.py --like <Hashtag>
    myig.py --unfollow <Count>
'''
args = docopt(usage)

class InstagramBot:
    
    def __init__(self , username , password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def CloseBrowser(self):
        self.driver.close()

    def Login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(3)
        username_box = driver.find_element_by_xpath("//input[@name='username']")
        username_box.clear()
        username_box.send_keys(self.username)
        time.sleep(1)

        password_box = driver.find_element_by_xpath("//input[@name='password']")
        password_box.clear()
        password_box.send_keys(self.password)
        time.sleep(4)

        
        login_btn = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
        login_btn.click()
        time.sleep(5)

        driver.get(f'https://www.instagram.com/{self.username}/')

    def like_photo(self , tag , scroll):

        driver = self.driver
        time.sleep(2)
        driver.get(f'https://www.instagram.com/explore/tags/{tag}/')  

        links_for_like = []

        for i in range(0,int(scroll)):
            try:
                driver.execute_script('window.scrollTo(0 , document.body.scrollHeight )')
                time.sleep(2)

                tag_view = driver.find_elements_by_tag_name('a')

                links_for_like = [elem.get_attribute('href') for elem in tag_view if '.com/p/' in elem.get_attribute('href')]
                links_for_like = set(links_for_like)
                links_for_like  = list(links_for_like)

                #save links to text file
                for l in links_for_like:
                    with open('Posts_Link.txt','a') as f:
                        f.write(l)

            except Exception:
                continue

        for link in links_for_like:
            driver.get(link)

            try:
                time.sleep(random.randint(1,4))
                driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click() 
                time.sleep(random.randint(1,4))

            except Exception:
                time.sleep(2)

    def unfollow(self , count):
        driver = self.driver
        following = driver.find_element_by_partial_link_text('following')
        following.click()

        time.sleep(2)
        for i in range(0,int(count)):
            driver.find_element_by_xpath('//button[text()="Following"]').click()
            driver.find_element_by_xpath('//button[text()="Unfollow"]').click()
            time.sleep(5)



username = input(colored('Please Enter Username : ','cyan'))
password = stdiomask.getpass(colored('Please Enter Password : ','magenta'))


if args['--like']:
    scroll = input(colored('Please Enter Scroll Count : ','yellow',))
    Hashtag = args['<Hashtag>']
    ig = InstagramBot(username , password)
    ig.Login()
    ig.like_photo(Hashtag,scroll)
    ig.CloseBrowser()
    

if args['--unfollow']:
    ig = InstagramBot(username , password)
    ig.Login()
    count = args['<Count>']
    ig.unfollow(count)
    ig.CloseBrowser()

