import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
import time 


class MoatTest(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Firefox()

    def run_test(self):
        setup()
        try_these()

    def test_try_these(self): 
        driver = self.driver
        try_these_link_text = []
        for i in range(0,5): 
            driver.get("https://www.moat.com")
            element = driver.find_element_by_class_name('random-brand')
            try_these_link_text.append(element.text)
 
        for index in range(0,4): 
            assert try_these_link_text[index] != try_these_link_text[index+1]

    # Verify that the "Recently Seen Ads" are no more than half an hour old.
    def test_recently_seen_ads(self): 
        driver = self.driver
        driver.get("https://www.moat.com")
        element = driver.find_element_by_class_name('recently_seen_ads')
        min_ago = element.text
        clean_min_ago = min_ago.split('\n')
        for i in clean_min_ago: 
            minutes = i.split('min ago')
            assert int(minutes[0]) < 30


    # Verify that the ad counts are correct, even when they are over 100.
    def test_ad_count(self): 
        driver = self.driver
        driver.get("https://www.moat.com")
        # Click on the ad
        ad = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[4]/div/div[1]/span/a[1]')
        ad.click()
        # keep clicking on the next 100 button while true. 
        while True:
            elements = driver.find_elements_by_class_name('btn')
            if len(elements)>0:
                elements[0].click()
                time.sleep(1)
            else:
                break
        query_summary = driver.find_element_by_class_name('query-summary')
        ad_containers = driver.find_elements_by_class_name('adcontainer')
        query_count = query_summary.text
        query_count = query_count.split('ads')
        query_count = query_count[0].replace(',','')
        counting_ads = len(ad_containers)
        assert int(query_count) == counting_ads
        

    # Verify the "Share this Ad" feature.
    def test_ad_share(self): 
        driver = self.driver
        driver.get("http://www.moat.com/search/results?q=Avon")
        # Hover
        element = driver.find_element_by_class_name('adcontainer')
        hov = ActionChains(driver).move_to_element(element)
        hov.perform()
        time.sleep(3)
        #click
        element = driver.find_element_by_link_text('Share this ad')
        element.click()
        # Check share ad text
        element = driver.find_element_by_class_name('share-this-ad')
        link = element.get_attribute('value')
        assert link is not None

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__" :
    unittest.main()


