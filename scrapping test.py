import requests
from bs4 import BeautifulSoup
import lxml
cmp = ["BAJAJ"]
website = "https://www.flipkart.com/search?q=solar+water+heater+for+home&sid=j9e%2Cabm%2Cbfm&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_na&as-pos=1&as-type=RECENT&suggestionId=solar+water+heater+for+home%7CGeyser%2Fwater+heater&requestId=dd791b81-ef89-4f5d-a0ad-4382a748f1e3&as-searchtext=solar%20water"
website_url = requests.get(website)
soup = BeautifulSoup(website_url.text,"lxml")
item = soup.find_all("div",{"class":"_13oc-S"})
for items in item:
    title_element = items.find("div",{"class":"_4rR01T"}).text
    link = items.find("a")
    link_h = items.find("div",{"class":"_2kHMtA"})
    link_a = link_h.find("a")
    link_last = link_a["href"]
    amount = items.find("div",{"class":"_3tbKJL"}).text
    if any(cp in title_element for cp in cmp):
        print(title_element,amount,link_last)

