#!/usr/bin/python

import json
from operator import itemgetter

with open('test_results.json') as json_data:
	test_results = json.load(json_data)


#get the list of different test suites and the number of the test suites
test_suites_list = test_results["test_suites"]
number_of_test_suites = len(test_suites_list)


#sort a list of dictionaries by key
def mySortedListByKey(mylist, myname):
	newlist = sorted(mylist, key=itemgetter(myname)) 
	return newlist
	

def printTestResults(suite_name, suite_results_list):
    
	pass_list = []
	fail_list = []
	blocked_list = []

	for test_case in suite_results_list:
		my_keys = test_case.keys()
		mynewlist=list(my_keys)
		my_test_name = mynewlist[0]
		if (my_test_name != 'test_name'):
				continue
		if test_case["status"] == "pass":
			pass_list.append(test_case)
		elif test_case["status"] == "fail":
			fail_list.append(test_case)
		elif test_case["status"] == "blocked":
			blocked_list.append(test_case)

	print("SUITE NAME: "+ str(suite_name.upper()))
	if (len(pass_list) != 0):
		print(*mySortedListByKey(pass_list,"test_name"), sep = '\n')
		print("\n")
	if (len(fail_list) != 0):
		print(*mySortedListByKey(fail_list,"test_name"), sep = '\n')
		print("\n")
	if (len(blocked_list) !=0):
		print(*mySortedListByKey(blocked_list,"test_name"), sep = '\n')


	time_list = []
	for test_case in suite_results_list:
		test_case_time = test_case["time"]
		if (test_case_time !='' and int(float(test_case_time)) > 10):
			time_list.append(test_case_time)
	if (len(time_list) !=0):
		print(len(time_list))
		print(sorted(time_list))
	else:
		print ("There was no test cases that took more than 10 seconds to execute")

#loop through test suite list and get the name of each suite and the test results list
for i in range(number_of_test_suites):
	suite_name = test_suites_list[i]["suite_name"]
	results_list = test_suites_list[i]["results"]
	printTestResults(suite_name, results_list)

