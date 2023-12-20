from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
class github_bot:
    
    chrome_driver_path="seleniumFile\chromedriver.exe"
    def __init__(self) -> None:
        options=webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        self.browser=webdriver.Chrome(options=options)
        self.baseurl="https://github.com/"
        self.username="Enesdrdnz"
        self.password="1a07d707e6606061E!"
    def SignIn(self):
        self.browser.get("https://github.com/login")
        username_input=self.browser.find_element(By.NAME,"login")
        pass_input=self.browser.find_element(By.NAME,"password")
        submit_input=self.browser.find_element(By.NAME,"commit")
        username_input.send_keys(self.username)
        time.sleep(2)
        pass_input.send_keys(self.password)
        time.sleep(2)
        submit_input.send_keys(Keys.ENTER)
    def load_followers(self):
        time.sleep(4)
        temporary_list={

        }
        followers_name=self.browser.find_elements(By.CSS_SELECTOR,".Link--secondary.pl-1")
        for i in range(len(followers_name)):
            temporary_list.update({
                i:{
                    "name":followers_name[i].text
                }
            })
        return(temporary_list)
    def get_Followers(self):
        self.browser.get("https://github.com/sadikturan")
        followers_button=self.browser.find_element(By.XPATH,"/html/body/div[1]/div[4]/main/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/a[1]")
        followers_button.click()
        time.sleep(4)
        self.load_followers()
        followers_list={
            
        }
        while True:
            count=len(followers_list)+1
            
            links=self.browser.find_element(By.CLASS_NAME,"pagination").find_elements(By.TAG_NAME,"a")
            if(len(links)==1):
                if(links[0].text=="Next"):
                    links[0].click()
                    temporary_result=self.load_followers()
                    print(temporary_result[1])
                    time.sleep(5)
                else:
                    break
            else:
                for link in links:
                    if(link.text =="Next"):
                        link.click()
                        temporary_result=self.load_followers()
                        print(temporary_result)
            for i in range(len(temporary_result)):
                followers_list.update({
                    count:{
                        "name":temporary_result[i]["name"]
                    }
                })
                count+=1
            print(followers_list)
            
    def __del__(self):
        pass