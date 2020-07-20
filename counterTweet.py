import gzip
import json
import glob


with gzip.open('Gender_Count_User_Demographics.gz','rt') as T1:
		demo_gender_temp = T1.read()
T1.close()


demo_gender = json.loads(demo_gender_temp)

#print(demo_gender)
overall_counts = {}
for h in demo_gender.keys():
	overall_counts[h] = sum(demo_gender[h])


#print(overall_counts)
print(len(overall_counts))

sort_demo = sorted(overall_counts.items(), key=lambda x: x[1], reverse=True)
sorted_dictionary = {}
for i in sort_demo:
	sorted_dictionary[i[0]] = i[1]
	#print(i[0])

#print(sorted_dictionary)

with gzip.open('Sorted_Dictionary.gz', 'wb') as f3:
	#fout.write(json.dumps(data).encode('utf-8'))
	f3.write(json.dumps(sorted_dictionary).encode('utf-8'))
f3.close()


# for i in sort_demo.keys():
# 	print(i, " : ", sort_demo[i])