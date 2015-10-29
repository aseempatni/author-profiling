import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.lines as mlines




ind = np.arange(1)
width = 0.3      # the width of the bars: can also be len(x) sequence


menMean = 0.010001
# x = [1.0,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0.0]
menstd = 0.000001
womenMean = 0.013116
womenstd = 0.000001


p1 = plt.bar(ind, [menMean],   width, color='r',yerr=[menMean])
p2 = plt.bar(ind+width, [womenMean],   width, color='y',yerr=[womenstd])
# p1, = plt.plot(menMean, x,color='r')
# p2, = plt.plot(womenMean,x,color='y')


plt.ylabel('Past/Future reference')
plt.title('Past/Future reference')
# plt.xlabel('# of types of POS tags')
plt.xticks([ind[0]+width/2,ind[0]+3*width/2], ['Male','Female'])
plt.legend( (p1, p2), ('Men', 'Women') )
plt.savefig('timereference_Gender.png')








ageGroup = ['18-24','25-34','35-49','50-64','65-xx']
ind = np.arange(1)  # the x locations for the groups

fig, ax = plt.subplots()

width = .2
color = {'18-24':'r','25-34':'y','35-49':'g','50-64':'b','65-xx':'k'}

legend_label = ['18-24','25-34','35-49','50-64','65-xx']


y1 = 0.004123
std1 = 0.000000
y2 = 0.006355
std2 = 0.000001
y3 = 0.011409
std3 =0.000001
y4 = 0.013781
std4 =0.000002
y5 = 0.020002
std5 =0.000002

p1 = plt.bar(ind,[y1],width,color = 'r',yerr=[std1])
p2 = plt.bar(ind+width,[y2],width,color = 'y',yerr=[std2])
p3 = plt.bar(ind+width*2,[y3],width,color = 'g',yerr=[std3])
p4 = plt.bar(ind+width*3,[y4],width,color = 'b',yerr=[std4])
p5 = plt.bar(ind+width*4,[y5],width,color = 'k',yerr=[std5])

# p1, = plt.plot(y1,x,color = 'r',linewidth=2.0)
# p2, = plt.plot(y2,x,color = 'y',linewidth=2.0)
# p3, = plt.plot(y3,x,color = 'g',linewidth=2.0)
# p4, = plt.plot(y4,x,color = 'b',linewidth=2.0)
# p5, = plt.plot(y5,x,color = 'k',linewidth=2.0)

# add some text for labels, title and axes ticks
plt.legend([p1,p2,p3,p4,p5],legend_label)
plt.ylabel('Past/Future reference')
plt.title('Past/Future reference')
# plt.xlabel('# of types of POS tags')
plt.xticks([ind[0]+width/2,ind[0]+3*width/2,ind[0]+5*width/2,ind[0]+7*width/2,ind[0]+9*width/2], legend_label)
# plt.legend((p1,p2,p3,p4,p5),legend_label )
# plt.title('HyperLinks')
plt.savefig('timereference_Age.png')
