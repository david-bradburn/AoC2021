# from selenium.webdriver import *;

def get_aoc_url(year : int, day: str):
    url = 'https://adventofcode.com/'

    # chrome = Chrome('./Dependencies/chromedriver') # create browser
    url_year = url + str(year)
    url_date = url_year + '/day/' + str(day)
    print(url_date)
    # chrome.get(url_date)
    return url_date

# get_aoc_url(2021, 18)