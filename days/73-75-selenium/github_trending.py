# A script that lists trending repositories on github
from selenium import webdriver

if __name__ == "__main__":
    path = r'C:\Users\mstrefel\dev\Python\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path)
    driver.get('https://github.com/explore')
    driver.find_elements_by_link_text('Trending repositories')[0].click()
    driver.close()
