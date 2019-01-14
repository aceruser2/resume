# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/caizonghan/chromedriver')
driver.implicitly_wait(30)
driver.get('https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html')


driver.find_element_by_css_selector(
    "body > div.bbs-screen.bbs-content.center.clear > form > div:nth-child(2) > button").click()
driver.find_element_by_css_selector(
    "#main-container > div.r-list-container.action-bar-margin.bbs-screen > div:nth-child(2) > div.title > a").click()

soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup)
# date
# author
# title
# content
# board
