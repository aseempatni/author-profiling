import math

def mean(numbers):
	return sum(numbers)/float(len(numbers))
 
def stdev(numbers):
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)
 
def getStats(Al):
	ans=[]
	for i in range(len(Al[0])):
		numbers=[j[i] for j in Al]
		m=mean(numbers)
		sd=stdev(numbers)
		ans.append((m,sd))
	return ans

f=open('quote.csv','r')
l=f.read().split('\n')[1:-1]
M=[]
F=[]
A1=[]
A2=[]
A3=[]
A4=[]
A5=[]
for line in l:
	line1=line.split(',')
	rd=line1[3:]
	rd=[float(rd[0])/float(rd[1])]
	if line1[1][0]=='M':
		M.append(rd)
	else:
		F.append(rd)
	if line1[2][0]=='1':
		A1.append(rd)
	elif line1[2][0]=='2':
		A2.append(rd)
	elif line1[2][0]=='3':
		A3.append(rd)
	elif line1[2][0]=='5':
		A4.append(rd)
	else:
		A5.append(rd)
M=getStats(M)
F=getStats(F)
A1=getStats(A1)
A2=getStats(A2)
A3=getStats(A3)
A4=getStats(A4)
A5=getStats(A5)

import numpy as np
import matplotlib.pyplot as plt

N = 1
menMeans = tuple([i[0] for i in M])
menStd =   tuple([i[1] for i in M])

ind = np.arange(N)  # the x locations for the groups
width = 0.50       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)

womenMeans = tuple([i[0] for i in F])
womenStd =   tuple([i[1] for i in F])
rects2 = ax.bar(ind+width, womenMeans, width, color='y', yerr=womenStd)

# add some text for labels, title and axes ticks
ax.set_ylabel('#quotes/#sentences')
ax.set_title('Fraction of Quoted sentences by Gender')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('') )

ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )

def autolabel(rects):
	# attach some text labels
	for rect in rects:
		height = rect.get_height()
		ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),ha='center', va='bottom')


plt.savefig('Fraction of Quoted sentences by Gender.png')
plt.show()

plt.figure()
A1means=tuple([i[0] for i in A1])
A2means=tuple([i[0] for i in A2])
A3means=tuple([i[0] for i in A3])
A4means=tuple([i[0] for i in A4])
A5means=tuple([i[0] for i in A5])
A1std=tuple([i[1] for i in A1])
A2std=tuple([i[1] for i in A2])
A3std=tuple([i[1] for i in A3])
A4std=tuple([i[1] for i in A4])
A5std=tuple([i[1] for i in A5])
ind = np.arange(N)  # the x locations for the groups
width = 0.14       # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(ind, A1means, width, color='r', yerr=A1std)
rects2 = ax.bar(ind+width, A2means, width, color='g', yerr=A2std)
rects3 = ax.bar(ind+2*width, A3means, width, color='b', yerr=A3std)
rects4 = ax.bar(ind+3*width, A4means, width, color='y', yerr=A4std)
rects5 = ax.bar(ind+4*width, A5means, width, color='m', yerr=A5std)
ax.set_ylabel('#quotes/#sentences')
ax.set_title('Fraction of Quoted sentences by Age Groups')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('') )

ax.legend( (rects1[0], rects2[0],rects3[0],rects4[0],rects5[0]), ('18-24','25-34','35-49','50-64','65-xx') )

def autolabel(rects):
	# attach some text labels
	for rect in rects:
		height = rect.get_height()
		ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),ha='center', va='bottom')


plt.savefig('Fraction of Quoted sentences by Age Groups.png')
plt.show()

