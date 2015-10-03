fo=open("SentiWordNet_3.0.0_20130122.txt","r")

p={}
n={}


for line in fo:
	x=line.split("\t")
	a=0
	found=0
	for y in x:
		if y.find("#")!=-1:
			found=1
		else:
			if found==1:
				break
		a+=1
	y=x[a-1].split(" ")
	pos=x[a-3]
	neg=x[a-2]
	for z in y:
		if z.find("#")!=-1:
			end=z.find("#")
		if z[:end] not in p:
			p[z[:end]]=pos
		else:
			p[z[:end]]=max(pos,p[z[:end]])
		if z[:end] not in n:
			n[z[:end]]=neg
		else:
			n[z[:end]]=max(neg,n[z[:end]])

print len(p)
print len(n)

fo.close()





import json

opinion_score={}
opinion_fact={}
character_flooding={}

for i in range(1,251):

	opinion_score[i]={}
	opinion_fact[i]={}
	character_flooding[i]={}


	json_data={}
	with open("blogdata"+str(i)+".json") as json_file:
		json_data=json.load(json_file)
		fo=open("mpqa.txt","w+")
		for post in json_data["Posts"]:
			try:
				fo.write(post+"\n")	
			except:
				continue
		fo.close()

	opinion_score[i]["Age"]=json_data["Age"]
	opinion_fact[i]["Age"]=json_data["Age"]
	opinion_score[i]["Sex"]=json_data["Sex"]
	opinion_fact[i]["Sex"]=json_data["Sex"]
	character_flooding[i]["Sex"]=json_data["Sex"]
	character_flooding[i]["Age"]=json_data["Age"]

	fo=open("mpqa.txt","r")

	fo2=open("output_author_"+str(i)+".txt","w+")

	flooded_words=[]

	c=0
	for line in fo:
		x=line.split(" ")
		x[len(x)-1]=x[len(x)-1].rstrip("\n")
		linescore1=0.0
		linescore2=0.0
		wordcount=0.0
		for y in x:
			if y in p:
				try:
					linescore1+=float(p[y])
				except:
					linescore1+=0.0
			if y in n:
				try:
					linescore1+=float(n[y])
				except:
					linescore1+=0.0
			if (y in p) or (y in n):
				done=0
				try:
					if ((y in p) and (float(p[y])>0.0)):
						linescore2+=1.0
						done=1
				except:
					linescore2+=0.0
				try:
					if done!=1:
						if ((y in n) and (float(n[y])>0.0)):
							linescore2+=1.0
				except:
					linescore2+=0.0
			wordcount+=1.0
		print wordcount
		print linescore2
		linescore2=linescore2/wordcount
		fo2.write(line+str(linescore1/(2*wordcount))+"\n")
		opinion_score[i][c]=linescore1/(2*wordcount)
		if opinion_score[i][c]>=0.1:
			opinion_fact[i][c]="opinion"
		else:
			opinion_fact[i][c]="fact"
		number_of_flooded_words=0
		for y in x:
			flood=0
			for j in range(0,len(y)-2):
				if(y[j]==y[j+1] and y[j+1]==y[j+2] and y[j].isalpha()):
					flood=1
					break
			if flood==1:
				number_of_flooded_words+=1
				flooded_words.append(y)
		character_flooding[i][c]=number_of_flooded_words
		c+=1
	character_flooding[i]["flooded_words"]=flooded_words



	fo2.close()	

fp=open("opinionscore.json","w+")
json.dump(opinion_score,fp,indent=4)
fp.close()

fp=open("opinionfact.json","w+")
json.dump(opinion_fact,fp,indent=4)
fp.close()

fp=open("character_flooding.json","w+")
json.dump(character_flooding,fp,indent=4)
fp.close()