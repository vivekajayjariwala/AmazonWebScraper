import requests
from bs4 import BeautifulSoup as bs
import csv
"""to bypass error that Amazon provides when trying to scrape the html from the page"""
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


"""load webpage content of Amazon.ca with "Unlocked Cell Phones Smartphones" as the search filter"""
source = requests.get('https://www.amazon.ca/Unlocked-Cell-Phones-Smartphones/b?ie=UTF8&node=3379583011', headers = headers)
"""convert to beautiful soup object"""
webpage = bs(source.content, 'lxml') #lxml is a python library that helps in the handling of HTML and XML files for webscraping
"""print out html"""
#print((webpage.prettify())) #prints out the html script from the Beautiful Soup parsing and prettify() formats it properly

phoneNames = [] #an array to hold all the smartphone names as listed on Amazon
phonePrices = []  #an array to hold all the smartphone prices as listed on Amazon

for i in webpage.find_all(class_='a-size-base a-color-base'):
    string = i.text #find and find_all returns whole tag but since just the text is needed, it is converted to text
    phoneNames.append(string.strip()) #.strip function clears empty spaces before and after text

for i in webpage.find_all(class_='a-price-whole'):
    string = i.text #find and find_all returns whole tag but since just the text is needed, it is converted to text
    phonePrices.append(string.strip()) #.strip function clears empty spaces before and after text

file_name = 'Smartphones.csv' #title of excel file

#with open used to interact with a file.
# do not need to close file since it already
#'utf-8' prevents an error related with the 'charmap' codec

with open(file_name, "w", encoding="utf-8") as f:
    f.write = csv.writer(f)
    f.write.writerow(['No.', 'Smartphone Name', 'Price ($)']) #the headers of the excel file

    #for loop cycles through the arrays and prints out on each row in the excel file:
    #the index number (+1 so that it does not start at 0), the smartphone name, and corresponding smartphone price

    for i in range(len(phoneNames)):
        f.write.writerow([i+1, phoneNames[i], phonePrices[i]])

