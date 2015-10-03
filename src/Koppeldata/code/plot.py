import math

def mean(numbers):
	if len(numbers)-1<=0:
		return 0
	return sum(numbers)/float(len(numbers))
 
def stdev(numbers):
	if len(numbers)-1<=0:
		return 0
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)

opinionscore={}
opinionfact={}
character_flooding={}


import json

with open("opinionscore.json","r") as json_file:
	opinionscore=json.load(json_file)

with open("opinionfact.json","r") as json_file:
	opinionfact=json.load(json_file)

with open("character_flooding.json","r") as json_file:
	character_flooding=json.load(json_file)


for key in opinionscore:
	l=[]
	for key2 in opinionscore[key]:
		if key2!="Age" and key2!="Sex":
			l.append(opinionscore[key][key2])
	opinionscore[key]["mean"]=mean(l)
	opinionscore[key]["stdev"]=stdev(l)

for key in opinionfact:
	o=0
	f=0
	for key2 in opinionfact[key]:
		if key2!="Age" and key2!="Sex":
			if opinionfact[key][key2]=="opinion":
				o+=1
			else:
				f+=1
	opinionfact[key]["number_of_opinion"]=o
	opinionfact[key]["number_of_fact"]=f

#18-24,25-34,35-49,50-64,65-xx
#M,F

age_wise={}
gender_wise={}

age_wise["opinionscore"]={}
age_wise["opinionfact_number_of_opinion"]={}
age_wise["opinionfact_number_of_fact"]={}
age_wise["character_flooding"]={}

for x in age_wise:
	age_wise[x]["0-17"]=[]
	age_wise[x]["18-24"]=[]
	age_wise[x]["25-34"]=[]
	age_wise[x]["35-49"]=[]
	age_wise[x]["50-64"]=[]
	age_wise[x]["65-xx"]=[]

gender_wise["opinionscore"]={}
gender_wise["opinionfact_number_of_opinion"]={}
gender_wise["opinionfact_number_of_fact"]={}
gender_wise["character_flooding"]={}

for x in gender_wise:
	gender_wise[x]["M"]=[]
	gender_wise[x]["F"]=[]


for key in opinionscore:
	gender=""
	agegroup=""
	if opinionscore[key]["Sex"]=="male":
		gender="M"
	else:
		gender="F"
	if opinionscore[key]["Age"]<=17:
		agegroup="0-17"
	elif opinionscore[key]["Age"]<=24:
		agegroup="18-24"
	elif opinionscore[key]["Age"]<=34:
		agegroup="25-34"
	elif opinionscore[key]["Age"]<=49:
		agegroup="35-49"
	elif opinionscore[key]["Age"]<=64:
		agegroup="50-64"
	else:
		agegroup="65-xx"
	age_wise["opinionscore"][agegroup].append(opinionscore[key]["mean"])
	gender_wise["opinionscore"][gender].append(opinionscore[key]["mean"])


for key in opinionfact:
	gender=""
	agegroup=""
	if opinionfact[key]["Sex"]=="male":
		gender="M"
	else:
		gender="F"
	if opinionfact[key]["Age"]<=17:
		agegroup="0-17"
	elif opinionfact[key]["Age"]<=24:
		agegroup="18-24"
	elif opinionfact[key]["Age"]<=34:
		agegroup="25-34"
	elif opinionfact[key]["Age"]<=49:
		agegroup="35-49"
	elif opinionfact[key]["Age"]<=64:
		agegroup="50-64"
	else:
		agegroup="65-xx"
	age_wise["opinionfact_number_of_opinion"][agegroup].append(opinionfact[key]["number_of_opinion"])
	gender_wise["opinionfact_number_of_opinion"][gender].append(opinionfact[key]["number_of_opinion"])
	age_wise["opinionfact_number_of_fact"][agegroup].append(opinionfact[key]["number_of_fact"])
	gender_wise["opinionfact_number_of_fact"][gender].append(opinionfact[key]["number_of_fact"])


for key in character_flooding:
	gender=""
	agegroup=""
	if character_flooding[key]["Sex"]=="male":
		gender="M"
	else:
		gender="F"
	if character_flooding[key]["Age"]<=17:
		agegroup="0-17"
	elif character_flooding[key]["Age"]<=24:
		agegroup="18-24"
	elif character_flooding[key]["Age"]<=34:
		agegroup="25-34"
	elif character_flooding[key]["Age"]<=49:
		agegroup="35-49"
	elif character_flooding[key]["Age"]<=64:
		agegroup="50-64"
	else:
		agegroup="65-xx"
	age_wise["character_flooding"][agegroup].append(len(character_flooding[key]["flooded_words"]))
	gender_wise["character_flooding"][gender].append(len(character_flooding[key]["flooded_words"]))


for key in age_wise:
	age_wise[key]["mean"]={}
	age_wise[key]["stdev"]={}
	for key2 in age_wise[key]:
		if key2!="mean" and key2!="stdev":
			print age_wise[key][key2]
			m=mean(age_wise[key][key2])
			s=stdev(age_wise[key][key2])
			age_wise[key]["mean"][key2]=m
			age_wise[key]["stdev"][key2]=s

for key in gender_wise:
	gender_wise[key]["mean"]={}
	gender_wise[key]["stdev"]={}
	for key2 in gender_wise[key]:
		if key2!="mean" and key2!="stdev":
			print gender_wise[key][key2]
			m=mean(gender_wise[key][key2])
			s=stdev(gender_wise[key][key2])
			gender_wise[key]["mean"][key2]=m
			gender_wise[key]["stdev"][key2]=s


fp=open("age_wise.json","w+")
json.dump(age_wise,fp,indent=4)
fp.close()

fp=open("gender_wise.json","w+")
json.dump(gender_wise,fp,indent=4)
fp.close()









import numpy as np
import matplotlib.pyplot as plt

for key in age_wise:
	N = 6

	menMeans = (age_wise[key]["mean"]["0-17"], age_wise[key]["mean"]["18-24"], age_wise[key]["mean"]["25-34"], age_wise[key]["mean"]["35-49"], age_wise[key]["mean"]["50-64"], age_wise[key]["mean"]["65-xx"])
	menStd =   (age_wise[key]["stdev"]["0-17"], age_wise[key]["stdev"]["18-24"], age_wise[key]["stdev"]["25-34"], age_wise[key]["stdev"]["35-49"], age_wise[key]["stdev"]["50-64"], age_wise[key]["stdev"]["65-xx"])

	ind = np.arange(N)  # the x locations for the groups
	width = 0.35       # the width of the bars

	fig, ax = plt.subplots()
	rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)

	# add some text for labels, title and axes ticks
	if key=="opinionfact_number_of_opinion":
		ax.set_ylabel("number of opinion")
		ax.set_title("number of opinion distribution over age-groups")
	elif key=="opinionfact_number_of_fact":
		ax.set_ylabel("number of fact")
		ax.set_title("number of fact distribution over age-groups")
	elif key=="character_flooding":
		ax.set_ylabel("character flooding")
		ax.set_title("character flooding distribution over age-groups")
	elif key=="opinionscore":
		ax.set_ylabel("opinion score")
		ax.set_title("opinion score distribution over age-groups")
	ax.set_xticks(ind+width)
	ax.set_xticklabels( ('0-17 years', '18-24 years', '25-34 years', '35-49 years', '50-64 years' ,'65-xx years') )

	# ax.legend( (rects1[0]), ('Men') )

	def autolabel(rects):
	    # attach some text labels
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%f'%float(height),
	                ha='center', va='bottom')

	autolabel(rects1)

	plt.show()

import numpy as np
import matplotlib.pyplot as plt

drawn={}
drawn["opinionfact_number_of_opinion"]=0
drawn["opinionfact_number_of_fact"]=0
drawn["character_flooding"]=0
drawn["opinionscore"]=0

for key in age_wise:

	if key=="opinionfact_number_of_opinion" or key=="opinionfact_number_of_fact" or key=="character_flooding" or key=="opinionscore":

		if drawn[key]==1:
			continue
		else:
			drawn[key]=1

		N = 6

		menMeans = (age_wise[key]["mean"]["0-17"], age_wise[key]["mean"]["18-24"], age_wise[key]["mean"]["25-34"], age_wise[key]["mean"]["35-49"], age_wise[key]["mean"]["50-64"], age_wise[key]["mean"]["65-xx"])
		menStd =   (age_wise[key]["stdev"]["0-17"], age_wise[key]["stdev"]["18-24"], age_wise[key]["stdev"]["25-34"], age_wise[key]["stdev"]["35-49"], age_wise[key]["stdev"]["50-64"], age_wise[key]["stdev"]["65-xx"])

		ind = np.arange(N)  # the x locations for the groups
		width = 0.35       # the width of the bars

		fig, ax = plt.subplots()
		rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)

		# add some text for labels, title and axes ticks
		if key=="opinionfact_number_of_opinion":
			ax.set_ylabel("number of opinion")
			ax.set_title("number of opinion distribution over age-groups")
		elif key=="opinionfact_number_of_fact":
			ax.set_ylabel("number of fact")
			ax.set_title("number of fact distribution over age-groups")
		elif key=="character_flooding":
			ax.set_ylabel("character flooding")
			ax.set_title("character flooding distribution over age-groups")
		elif key=="opinionscore":
			ax.set_ylabel("opinion score")
			ax.set_title("opinion score distribution over age-groups")
		ax.set_xticks(ind+width)
		ax.set_xticklabels( ('0-17 years', '18-24 years', '25-34 years', '35-49 years', '50-64 years' ,'65-xx years') )

		# ax.legend( (rects1[0]), ('Men') )

		def autolabel(rects):
		    # attach some text labels
		    for rect in rects:
		        height = rect.get_height()
		        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%f'%float(height),
		                ha='center', va='bottom')

		autolabel(rects1)

		plt.show()




for key in gender_wise:
	if key=="opinionfact_number_of_opinion" or key=="opinionfact_number_of_fact" or key=="character_flooding" or key=="opinionscore":
		N = 2

		menMeans = (gender_wise[key]["mean"]["M"], gender_wise[key]["mean"]["F"])
		menStd =   (gender_wise[key]["stdev"]["M"], gender_wise[key]["stdev"]["F"])

		ind = np.arange(N)  # the x locations for the groups
		width = 0.35       # the width of the bars

		fig, ax = plt.subplots()
		rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)

		# add some text for labels, title and axes ticks
		if key=="opinionfact_number_of_opinion":
			ax.set_ylabel("number of opinion")
			ax.set_title("number of opinion distribution over gender-groups")
		elif key=="opinionfact_number_of_fact":
			ax.set_ylabel("number of fact")
			ax.set_title("number of fact distribution over gender-groups")
		elif key=="character_flooding":
			ax.set_ylabel("character flooding")
			ax.set_title("character flooding distribution over gender-groups")
		elif key=="opinionscore":
			ax.set_ylabel("opinion score")
			ax.set_title("opinion score distribution over gender-groups")
		ax.set_xticks(ind+width)
		ax.set_xticklabels( ('Male', 'Female') )

		# ax.legend( (rects1[0]), ('Men') )

		def autolabel(rects):
		    # attach some text labels
		    for rect in rects:
		        height = rect.get_height()
		        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%f'%float(height),
		                ha='center', va='bottom')

		autolabel(rects1)

		plt.show()