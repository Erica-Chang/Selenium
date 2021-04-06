# http://selenium-python.readthedocs.org/en/latest/getting-started.html 
 


from selenium import webdriver
from selenium.ewbdriver.common.keys import Keys 


# I want to loop though all the web browsers. 
browsers = ["Firefox", "Google", "Safari", "IE"]

def setup():
	for browser in browsers:
		print webdriver.browser()

		#driver = webdriver.browser()
		#driver.get("http://www.moat.com/search/results?q=Georgetown+University&ad=11659700")


# Veryify that the try these links are random and that they work. 
def try_these(): 
	pass

# Verify that the "Recently Seen Ads" are no more than half an hour old.
def recently_seen_ads(): 
	pass

# Verify that the ad counts are correct, even when they are over 100.
def ad_count():
	pass

# Verify the "Share this Ad" feature.
def ad_share(): 
	pass


# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found" not in driver.page_source


def tear_down(): 
	driver.(close)


setup()