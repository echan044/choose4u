import boto3
from selenium import webdriver
from os import path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

words=[]

if __name__ == "__main__":
    fileName='object.jpg'
    bucket='fooducrbucket3'
    
    client=boto3.client('rekognition','us-west-2')

    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':fileName}})

    print('Detected labels for ' + fileName)
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
        words.append(label['Name'])


'''
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

#create chrome instance
browser = webdriver.Chrome("C:\Users\TheEr\Downloads\chromedriver.exe", chrome_options=option)

for word in words:
    url = "http://nutritiondata.self.com/foods-" + word + "000000000000000000000.html"
    print(word)

    browser.get(url)

    browser.find_element_by_xpath("""//*[@id="search_header"]/table/tbody/tr[2]/td/a""").click()

    print(browser.find_element_by_xpath("""//*[@id="NUTRIENT_0"]""").text)

    #wb = browser.find_element_by_xpath("""//*[@id="header"]/table/tbody/tr/td/form/table/tbody/tr/td[1]/input""")
    #browser.execute_script("arguments[0].value='taco';", wb);
'''


