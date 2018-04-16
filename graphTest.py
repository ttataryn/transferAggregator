import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
from matplotlib.dates import date2num
import numpy as np

# ## Number of Transfers by Year
# year = ["2017-18", "2016-17", "2015-16", "2014-15", "2013-14", "2012-2013"]
# numTransfers = [204, 203, 202, 193, 187, 185]
# y_pos = np.arange(len(year))
# axes = plt.gca()
# axes.set_ylim([140,220])
# plt.bar(y_pos, numTransfers, align='center', alpha=0.5, color='blue')
# plt.xticks(y_pos, year)
# plt.xlabel('EPL Season')
# plt.ylabel('Number of Incoming Transfers')

# plt.title('Number of Transfers by Year \n')

# plt.text(500,50, "Hello")
# plt.show()

# Expenditure by Year -- top clubs

n_groups = 7
transfers2013 = (130.35, 121.88, 116, 58.1, 49.25, 77.13, 31.8)
transfers2014= (118.98, 48.47, 88.3, 151.43, 118.98, 195.35, 40.16)
transfers2015= (90.5, 71, 214.9, 125.4, 26.5, 156, 49.18)
transfers2016= (132.8, 83.6, 213, 79.9, 107.04, 185, 85.9)
transfers2017 = (257.8, 121.5, 315.8, 168.03, 118.85, 164.4, 202.7)


# create plot
fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.15
opacity = 0.7
 
rects1 = plt.bar(index, transfers2013, bar_width,
                 alpha=opacity,
                 color='blue',
                 label='2013-14')
i=0
for rect in rects1:
        if i==0:
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width()/2.0, height, "*", ha='center', va='bottom')
	if i==2:
		height = rect.get_height()
		plt.text(rect.get_x() + rect.get_width()/2.0, height, "**", ha='center', va='bottom')
        elif i==3:
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width()/2.0, height, "*", ha='center', va='bottom')
        elif i==4:
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width()/2.0, height, "*", ha='center', va='bottom')

	i+=1
 
rects2 = plt.bar(index + bar_width, transfers2014, bar_width,
                 alpha=opacity,
                 color='green',
                 label='2014-15')
i=0
for rect in rects2:
	if i==0:
		height = rect.get_height()
		plt.text(rect.get_x() + rect.get_width()/2.0, height, "**", ha='center', va='bottom')
        if i==2 or (i== 4) or (i==5):
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width()/2.0, height, "*", ha='center', va='bottom')
	i+=1

rects3 = plt.bar(index + bar_width + .15, transfers2015, bar_width,
                 alpha=opacity,
                 color='gray',
                 label='2015-16')
i=0
for rect in rects3:
        if i==1 or (i== 2) or (i==4):
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width()/2.0, height, "*", ha='center', va='bottom')
        i+=1

rects4 = plt.bar(index + bar_width + .30, transfers2016, bar_width,
                 alpha=opacity,
                 color='red',
                 label='2016-17')
i=0
for rect in rects4:
	if i==0:
		height = rect.get_height()
		plt.text(rect.get_x() + rect.get_width()/2.0, height, "**", ha='center', va='bottom')
        if i==1 or (i== 2) or (i==3):
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width()/2.0, height, "*", ha='center', va='bottom')
	i+=1

rects5 = plt.bar(index + bar_width + .45, transfers2017, bar_width,
                 alpha=opacity,
                 color='black',
                 label='2017-18')
axes = plt.gca()
axes.set_ylim([20,350])
labels = ['2013-14', '2014-15', '2015-16','2016-17','2017-18']


title_string = "(** signifies Champion that year, * is a top 4 finish) \n"
plt.xlabel('Team')
plt.ylabel('Transfer (in millions)')
plt.title('Expenditures by Team from 2013-2018 \n')
plt.suptitle(title_string, x=.53, y=.92, fontsize=8)

plt.xticks(index + bar_width, ('Chelsea', 'Tottenham', 'Man City', 'Liverpool', 'Arsenal', 'Man United','Everton'))
plt.legend(labels)
 
plt.tight_layout()
plt.show()



## Days vs Number of transfers -- Individual Reporters

# Mark Ogden = 104 out of 1036
# Simon Stone = 106 out of 1857
# John Cross = 262 out of 1461
# David Ornstein = 87 out of 112
# John Percy = 57 out of 174
# Duncan Castles = 47 + out of 1231
# Ed Aarons = 109 out of 961
# Lyall Thomas = 88 out of 1417
# Paul Joyce = 30 out of 193
# James Ducker = 84 out of 561
# Keith Downie = 55out of 839




# ax = plt.subplot()
# rects= ax.bar(indices, numTweets, width=width, 
#         color='b', label='Total Number of Tweets')
# rects= ax.bar([i+.0001*width for i in indices], numRumors, 
#         width=width, color='red', alpha=0.6, label='Number of Rumors')

# labels = ['77.67%','32.76%','15.54%','14.97%']

# plt.xticks(indices+width/5., 
#            [reporterNames[i] for i in range(len(numTweets))], rotation = "vertical" )

# for rect, label in zip(rects, labels):
# 	if label == '77.67%':
# 		height = rect.get_height()
# 		ax.text(rect.get_x() + rect.get_width() / 2, height - 25, label,
#             ha='center', va='bottom', color="white")
# 	else:
# 		height = rect.get_height()
# 		ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
#             ha='center', va='bottom', color="white")
# plt.legend()
# plt.title("Number of Rumors vs Total Number of Tweets by Reporter")

# plt.show()




#---------------------------- Days vs Num Transfers -----------------------------------------
# dayOfTransferDict = {"Tues": 28, "Thu": 18, "Fri": 32, "Sat":12,"Sun":7,"Wed":28,"Mon": 25}
# plt.bar(range(len(dayOfTransferDict)), dayOfTransferDict.values(), color ="blue")
# plt.xticks(range(len(dayOfTransferDict)), list(dayOfTransferDict.keys()))
# plt.xlabel("Day of Transfer", fontsize=16)  
# plt.ylabel("Count", fontsize=16)  
# plt.show()