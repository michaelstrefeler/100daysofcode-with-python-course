import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        path = r'C:\Users\mstrefel\dev\Python\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=path)

    def test_index_page(self):
        driver = self.driver
        driver.get("http://pyplanet.herokuapp.com/")
        self.assertEqual("PyBites 100 Days of Django", driver.title)
        navbar = driver.find_element_by_id("login").get_attribute('innerHTML')
        main = driver.find_elements_by_tag_name('main')
        self.assertIn('Login', navbar)
        self.assertIn('Home', navbar)
        self.assertIsNotNone(main)
        assert "No results found." not in driver.page_source

    def test_articles_page(self):
        driver = self.driver
        driver.get("http://pyplanet.herokuapp.com/")
        driver.find_element_by_link_text('PyPlanet Article Sharer App').click()
        table = driver.find_elements_by_tag_name('table')[0]
        th = table.find_elements_by_tag_name('th')[0]
        tr = table.find_elements_by_tag_name('tr')
        self.assertIsNotNone(table)
        self.assertEqual("Title", th.get_attribute('innerHTML'))
        self.assertGreaterEqual(len(tr), 100)

    def test_article(self):
        driver = self.driver
        driver.get("http://pyplanet.herokuapp.com/pyplanet/2029")
        button = driver.find_elements_by_class_name('pure-button')
        self.assertIsNotNone(button)
        driver.find_element_by_class_name('pure-button').click()
        button = driver.find_elements_by_class_name('pure-button')
        self.assertEqual(button, [])

    def login(self):
        driver = self.driver
        driver.get("http://pyplanet.herokuapp.com/")
        user = 'guest'
        pwd = 'changeme'

        driver.find_element_by_link_text('Login').click()
        driver.find_element_by_id('id_username').send_keys(user)
        driver.find_element_by_id('id_password').send_keys(pwd + Keys.RETURN)

    def test_login_and_logout(self):
        self.login()
        driver = self.driver
        driver.get("http://pyplanet.herokuapp.com/")
        text = 'Welcome back, guest!'
        tweet = driver.find_elements_by_link_text('Tweet this')
        navbar = driver.find_element_by_id("login").get_attribute('innerHTML')
        logout_text = 'See you!'

        self.assertIn(text, navbar)
        driver.find_element_by_link_text('PyPlanet Article Sharer App').click()
        driver.find_element_by_partial_link_text('Codementor: Buildin').click()
        self.assertIsNotNone(tweet)
        driver.find_element_by_link_text('Logout').click()
        h1 = driver.find_element_by_tag_name('h1').get_attribute('innerHTML')
        self.assertEqual(logout_text, h1)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
