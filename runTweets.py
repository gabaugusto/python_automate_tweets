import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TwitterBot():
    def __init__(self,username,password):
        self.browser=webdriver.Firefox(executable_path=r'firefoxdriver/geckodriver.exe')
        self.username=username
        self.password=password

    def signIn(self):
        self.browser.get("https://www.twitter.com/login")
        time.sleep(5)
        usernameInput=self.browser.find_element_by_name("session[username_or_email]")
        passwordInput=self.browser.find_element_by_name("session[password]")
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)

    def TweetSomething(self):
        tweet = self.browser.find_element_by_xpath('''//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div
                                                    /div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div
                                                    /div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div
                                                    /div/div/div''')
        tweet.send_keys("""Hello World!""")
        tweet.send_keys(Keys.COMMAND, Keys.ENTER)    

#self.username="es_starly@gabrielaugusto.me"
#self.password="userTwitter@0"    

if __name__=="__main__":
    username= input("Enter your username: ")
    password= input("Enter your password: ")
    t=TwitterBot(username,password)
    t.signIn()
    t.TweetSomething()        