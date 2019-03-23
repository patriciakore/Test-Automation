#!/usr/bin/python

import unittest
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#This test navigates to slashdot.org site, finds and prints the number of articles
#and unique images. It also navigates to polls site and votes for an option and prints
#which option the user voted for



class TestSlashdot(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get("https://slashdot.org/")


	#print number of articles and unique images of the articles on slashdot page
	def test_print_number_of_articles_and_images(self):

		articles = self.driver.find_element_by_id('firehoselist').find_elements_by_tag_name('article')
		print("The number of articles is: "+ str(len(articles)))

		my_images_list = []
		for article in articles:
			my_image = article.find_element_by_tag_name('img')
			my_image_src = my_image.get_attribute('src')
			if my_image_src not in my_images_list and my_image_src.startswith('https://'):
				my_images_list.append(my_image_src)

		for x in my_images_list:
			print(x)
		print("This is the number of unique images: "+ str(len(my_images_list)))


	#navigate to polls page and vote for a random option and print the option you voted for
	def test_vote_in_polls(self):

		self.driver.get('https://slashdot.org/polls')

		radio_buttons = self.driver.find_element_by_id('pollBooth').find_elements_by_tag_name('label')
		
		number_of_options = len(radio_buttons)
	       
		button_to_click_on = random.randint(0,number_of_options-1)

		radio_buttons[button_to_click_on].click()	

		my_poll_button = self.driver.find_element_by_class_name('poll-controls').find_element_by_class_name('btn-polls')

		my_label = radio_buttons[button_to_click_on].text

		print("The option I voted for is: "+ str(my_label))

		my_poll_button.click()	

		groups = self.driver.find_elements_by_class_name('poll-bar-group')
		  
		for x in groups:
			if my_label == x.find_element_by_class_name('poll-bar-label').text: 
				print("The number of people who voted for the: " + str(my_label)+ " option is: " + str(x.find_element_by_class_name('poll-bar-text').text))


	def tearDown(self):
		self.driver.quit()  


if __name__ == '__main__':
    unittest.main()
