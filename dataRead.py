#/Users/WaleedAhmed/Documents/THESIS_DS_CODE/June++/dataReadCode_2/Hashtag_Demographics(3months)

import gzip
import json
import glob
import itertools
import time



def splitHashtag(hashtag):
	temp = hashtag.split("\t")	
	name = temp[0]
	demo = json.loads(temp[1])

	return name, demo

def splitDemographics(demog):
	gen_dem = demog["gender"] 
	rac_dem = demog["race"]
	age_dem = demog["age_group"]

	return gen_dem, rac_dem, age_dem

def countGender(gender_demo, valid_users_count):
	male = gender_demo["male"]*float(valid_users_count)
	female = gender_demo["female"]*float(valid_users_count)

	return [male, female]

def countRace(race_demo, valid_users_count):
	white = race_demo["white"]*float(valid_users_count)
	black = race_demo["black"]*float(valid_users_count)
	asian = race_demo["asian"]*float(valid_users_count)

	return [white, black, asian]

def countAge(age_demo, valid_users_count):
	adolescent = age_demo["-20"]*float(valid_users_count)
	old = age_demo["65+"]*float(valid_users_count)
	young = age_demo["20-40"]*float(valid_users_count)
	mid_aged = age_demo["40-65"]*float(valid_users_count)

	return [adolescent, old, young, mid_aged]

def addList(list1, list2):
	newList = [list1[i] + list2[i] for i in range(len(list1))] 
	return newList


if __name__== "__main__":
	start_time = time.time()
	###########################################################
	#Path to directory containing files
	path_hashtagsDemo = "/Users/WaleedAhmed/Documents/THESIS_DS_CODE/June++/dataReadCode_2/Hashtag_Demographics(3months)/*.gz"
	#Path String
	list_of_files = glob.glob(path_hashtagsDemo)
	print("Total Files: ", len(list_of_files))

	#F = list_of_files[0]

	DEMO_GENDER = {}
	DEMO_AGE = {}
	DEMO_RACE = {}

	#print(F)
	#reading the hashtags_demo file
	for F in list_of_files:
		with gzip.open(F, 'rt') as f:
			hashT_content = f.read()
		f.close()

		#splitting the hastags with \n
		hashtags_demo = hashT_content.split("\n") #a list containing information of the users demographics

		#total number of hashtags in current file (hashtags_demo)
		no_of_hashtags = len(hashtags_demo)

		for h in range(no_of_hashtags):
			if (len(hashtags_demo[h]) == 0):
				break

			#splitting the hashtag name and the demographics information
			hashtag_name, user_demographics = splitHashtag(hashtags_demo[h])
			#splitting the demographics
			gender_demo, race_demo, age_demo = splitDemographics(user_demographics["independent"])
			#count of valid users
			valid_users_count = user_demographics["valid_users_count"]

			#counting gender
			[male, female] = countGender(gender_demo, valid_users_count)
			gender_list = [male, female]
			#counting race
			[white, black, asian] = countRace(race_demo, valid_users_count)
			race_list = [white, black, asian]
			#counting age
			[adolescent, old, young, mid_aged] = countAge(age_demo, valid_users_count)
			age_list = [adolescent, old, young, mid_aged]

			if hashtag_name not in DEMO_GENDER:
				DEMO_GENDER[hashtag_name] = gender_list
				DEMO_RACE[hashtag_name] = race_list
				DEMO_AGE[hashtag_name] = age_list
			else:
				# temp_gen_list = DEMO_GENDER[hashtag_name]
				# temp_rac_list = DEMO_RACE[hashtag_name]
				# temp_age_list = DEMO_AGE[hashtag_name]

				DEMO_GENDER[hashtag_name] = addList(gender_list, DEMO_GENDER[hashtag_name])
				DEMO_RACE[hashtag_name] = addList(race_list, DEMO_RACE[hashtag_name])
				DEMO_AGE[hashtag_name] = addList(age_list, DEMO_AGE[hashtag_name])



	with gzip.open('Gender_Count_User_Demographics.gz', 'wb') as f1:
		#fout.write(json.dumps(data).encode('utf-8'))
		f1.write(json.dumps(DEMO_GENDER).encode('utf-8'))
	f1.close()
	
	with gzip.open('Race_Count_User_Demographics.gz', 'wb') as f2:
		#fout.write(json.dumps(data).encode('utf-8'))
		f2.write(json.dumps(DEMO_RACE).encode('utf-8'))
	f2.close()
	
	with gzip.open('Age_Count_User_Demographics.gz', 'wb') as f3:
		#fout.write(json.dumps(data).encode('utf-8'))
		f3.write(json.dumps(DEMO_AGE).encode('utf-8'))
	f3.close()
	
	print(DEMO_GENDER["NYC"])
	print(DEMO_RACE["NYC"])
	print(DEMO_AGE["NYC"])

	print(len(DEMO_GENDER))

	print(len(DEMO_RACE))

	print(len(DEMO_AGE))



	print("Elapsed Time")
	print("--- %s seconds ---" % (time.time() - start_time))

