import json 
import urllib
import re
import urllib.request

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

path = './'
fileName = "example"

htmlfile = urllib.request.urlopen("https://www.yelp.com/search?cflt=churches&find_loc=San+Diego%2C+CA")
htmltext = htmlfile.read().decode('utf-8')
regexName = '<a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="[^.]*" [^.]*" ><span >(.+?)</span></a>'
regexPhone = """<span class="biz-phone">
        (.+?)
    </span>"""
regexAddress = """<address>
        (.+?)
    </address>"""
    #<span id ="yfs_l84_[ 
    #use [^.]* ^ for new strand, . for any character, * repeat any number of times"
patternName = re.compile(regexName)
patternPhone = re.compile(regexPhone)
patternAddress = re.compile(regexAddress)
allName = re.findall(patternName,htmltext)
allPhone = re.findall(patternPhone, htmltext)
allAddress = re.findall(patternAddress, htmltext)
    #findall returns as an array ie. if apple has 3 prices, it would return all 3
    #can print all of price, or price[0] to remove the brackets

data = {}

for index, thing in enumerate(allName):
    allAddress[index] = allAddress[index].replace('<br>', ', ')

    data[thing] = {
        'name': allName[index], 
        'address': allAddress[index],
        'phone': allPhone[index]
    }

writeToJSONFile(path, fileName, data)
