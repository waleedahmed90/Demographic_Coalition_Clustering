#/Users/WaleedAhmed/Documents/THESIS_DS_CODE/June++/dataReadCode_2/Counts_Demographics

import gzip
import json
import glob
import itertools
import time
import numpy as np



def percentages(templist):
	perc = [((i*100)/sum(templist)) for i in templist]
	return perc 


def stats(demo_gender, demo_race, demo_age):
	stats_gender = {}
	stats_race = {}
	stats_age = {}

	for h in demo_gender:
		stats_gender[h] = percentages(demo_gender[h]) 
		stats_race[h] = percentages(demo_race[h])
		stats_age[h] = percentages(demo_age[h])



	return stats_gender, stats_race, stats_age





if __name__== "__main__":
	start_time = time.time()

	path_gender = "/Users/WaleedAhmed/Documents/THESIS_DS_CODE/June++/dataReadCode_2/Counts_Demographics/Gender_Count_User_Demographics.gz"
	path_race = "/Users/WaleedAhmed/Documents/THESIS_DS_CODE/June++/dataReadCode_2/Counts_Demographics/Race_Count_User_Demographics.gz"
	path_age = "/Users/WaleedAhmed/Documents/THESIS_DS_CODE/June++/dataReadCode_2/Counts_Demographics/Age_Count_User_Demographics.gz"
	



	#Loading dictionaries of Promoter Counts Gender
	with gzip.open(path_gender,'rt') as T1:
		demo_gender_temp = T1.read()
	T1.close()

	demo_gender = json.loads(demo_gender_temp)
	
	#Loading dictionaries of Promoter Counts Race
	with gzip.open(path_race,'rt') as T2:
		demo_race_temp = T2.read()
	T2.close()

	demo_race = json.loads(demo_race_temp)
	
	#Loading dictionaries of Promoter Counts Age
	with gzip.open(path_age,'rt') as T3:
		demo_age_temp = T3.read()
	T3.close()

	demo_age = json.loads(demo_age_temp)



	Gender_perc, Race_perc, Age_perc = stats(demo_gender, demo_race, demo_age)

	with gzip.open('Gender_Percentage_User_Demographics.gz', 'wb') as f1:
		#fout.write(json.dumps(data).encode('utf-8'))
		f1.write(json.dumps(Gender_perc).encode('utf-8'))
	f1.close()
	
	with gzip.open('Race_Percentage_User_Demographics.gz', 'wb') as f2:
		#fout.write(json.dumps(data).encode('utf-8'))
		f2.write(json.dumps(Race_perc).encode('utf-8'))
	f2.close()
	
	with gzip.open('Age_Percentage_User_Demographics.gz', 'wb') as f3:
		#fout.write(json.dumps(data).encode('utf-8'))
		f3.write(json.dumps(Age_perc).encode('utf-8'))
	f3.close()

	print(Gender_perc["NYC"])
	print(Race_perc["NYC"])
	print(Age_perc["NYC"])


	# print(type(demo_gender))
	# print(len(demo_gender))
	# print(demo_gender["NYC"])

	# print(type(demo_race))
	# print(len(demo_race))
	# print(demo_race["NYC"])

	# print(type(demo_age))
	# print(len(demo_age))
	# print(demo_age["NYC"])



	print("Elapsed Time")
	print("--- %s seconds ---" % (time.time() - start_time))

	